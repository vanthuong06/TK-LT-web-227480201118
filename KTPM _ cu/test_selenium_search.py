from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pyodbc


def save_to_sql_server(data):
    """Lưu danh sách `data` vào bảng KetQuaTimKiem trong SQL Server.
    
    Mỗi phần tử của `data` là một tuple (ten_bai, link)
    """
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MAYGVPM1\\SQLEXPRESS;'
        'DATABASE=QLSV;'
        'Trusted_Connection=yes;'
    )
    
    cursor = conn.cursor()
    # Tạo bảng nếu chưa tồn tại
    cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='KetQuaTimKiem' and xtype='U')
    CREATE TABLE KetQuaTimKiem (
        STT INT PRIMARY KEY IDENTITY(1,1),
        TenBai NVARCHAR(500),
        Link NVARCHAR(1000)
    )
    ''')
    conn.commit()
    
    # Chèn dữ liệu vào bảng
    for row in data:
        cursor.execute("INSERT INTO KetQuaTimKiem (TenBai, Link) VALUES (?, ?)", (row[0], row[1]))
    conn.commit()
    conn.close()


# Khởi tạo WebDriver
driver = webdriver.Chrome()
driver.get("https://nld.com.vn/")
driver.maximize_window()
title = driver.title
print(title)

# Tìm ô tìm kiếm theo ID và nhập từ khóa
search_bar = driver.find_element(by=By.ID, value="txt-search")
search_bar.click()

search_bar = driver.find_element(by=By.ID, value="txt-search")
search_bar.send_keys("Tổng Bí thư Tô Lâm")
search_bar.send_keys(Keys.ENTER)
time.sleep(5)

extracted_data = []
search_title_elements = driver.find_elements(by=By.CLASS_NAME, value="box-cat-item")
for element in search_title_elements:
    try:
        title_li = element.find_element(by=By.CLASS_NAME, value="h3").text
        link = element.find_element(By.CSS_SELECTOR, value="h3>a").get_attribute("href")
        print(title_li)
        print(link)
        print("-----")
        extracted_data.append((title_li, link))
    except NoSuchElementException:
        pass

driver.quit()

# Lưu dữ liệu vào SQL Server
save_to_sql_server(extracted_data)
print("Dữ liệu đã được lưu vào SQL Server.")

