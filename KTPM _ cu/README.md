# Đề thi Kết thúc học phần - Kiểm thử và ĐBCL Phần mềm

## Mô tả
Dự án Python thực hiện 3 câu hỏi về kiểm thử phần mềm:
- Câu 1: Kiểm thử hàm tam giác sử dụng bảng quyết định và lớp tương đương
- Câu 2: Thiết kế và kiểm thử lớp giỏ hàng sử dụng pytest fixture và Mock
- Câu 3: Kiểm thử chức năng tìm kiếm web bằng Selenium và lưu kết quả vào SQL Server

## Cài đặt

### 1. Cài đặt Python packages
```bash
pip install selenium
pip install pytest
pip install pyodbc
```

Hoặc cài đặt tất cả từ file requirements.txt:
```bash
pip install -r requirements.txt
```

### 2. Cài đặt ChromeDriver
- Tải ChromeDriver từ: https://chromedriver.chromium.org/
- Đặt vào PATH hoặc cùng thư mục với project
- Hoặc sử dụng webdriver-manager:
```bash
pip install webdriver-manager
```

### 3. Cài đặt ODBC Driver (cho Câu 3)
- Tải và cài đặt **ODBC Driver 17 for SQL Server** từ Microsoft
- Link tải: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

### 4. Cấu hình SQL Server (cho Câu 3)
- Cài đặt SQL Server Express hoặc SQL Server
- Cập nhật connection string trong file `test_selenium_search.py` (dòng 14-18):
```python
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAYGVPM1\\SQLEXPRESS;'  # Thay đổi theo server của bạn
    'DATABASE=QLSV;'                 # Thay đổi theo database của bạn
    'Trusted_Connection=yes;'
)
```

## Chạy chương trình

### Câu 1: Test hàm tam giác
```bash
python test_tamgiac.py
```
Kết quả sẽ được lưu vào file `ketqua.html`

### Câu 2: Test giỏ hàng
```bash
pytest test_giohang.py -v
```

### Câu 3: Test tìm kiếm Selenium
```bash
python test_selenium_search.py
```

## Cấu trúc project
```
.
├── tamgiac.py              # Hàm tam giác (Câu 1)
├── test_tamgiac.py         # Test cases cho hàm tam giác
├── giohang.py              # Lớp giỏ hàng (Câu 2)
├── test_giohang.py         # Test cases cho giỏ hàng
├── test_selenium_search.py # Test Selenium (Câu 3)
├── requirements.txt        # Dependencies
└── README.md              # File này
```

## Lưu ý
- Câu 3 yêu cầu có ChromeDriver và trình duyệt Chrome
- Câu 3 yêu cầu SQL Server nếu muốn lưu kết quả vào database
- Có thể comment phần database trong Câu 3 nếu chỉ muốn test Selenium

