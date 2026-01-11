import unittest
from tamgiac import tamgiac
from HTMLTestRunner import HTMLTestRunner


class TestTamGiac(unittest.TestCase):
    def test_tam_giac_deu(self):
        self.assertEqual(tamgiac(3, 3, 3), 'Tam giác đều')
        self.assertEqual(tamgiac(5, 5, 5), 'Tam giác đều')
        self.assertEqual(tamgiac(10, 10, 10), 'Tam giác đều')
    
    def test_tam_giac_can_a_bang_b(self):
        self.assertEqual(tamgiac(5, 5, 8), 'Tam giác cân')
        self.assertEqual(tamgiac(4, 4, 6), 'Tam giác cân')
    
    def test_tam_giac_can_a_bang_c(self):
        self.assertEqual(tamgiac(5, 8, 5), 'Tam giác cân')
        self.assertEqual(tamgiac(4, 6, 4), 'Tam giác cân')
    
    def test_tam_giac_can_b_bang_c(self):
        self.assertEqual(tamgiac(8, 5, 5), 'Tam giác cân')
        self.assertEqual(tamgiac(6, 4, 4), 'Tam giác cân')
    
    def test_tam_giac_thuong(self):
        self.assertEqual(tamgiac(3, 4, 5), 'Tam giác thường')
        self.assertEqual(tamgiac(5, 6, 7), 'Tam giác thường')
        self.assertEqual(tamgiac(7, 8, 9), 'Tam giác thường')
    
    def test_khong_phai_tam_giac_canh_bang_0(self):
        self.assertEqual(tamgiac(0, 0, 0), 'Không phải là tam giác')
        self.assertEqual(tamgiac(0, 1, 1), 'Không phải là tam giác')
        self.assertEqual(tamgiac(1, 0, 1), 'Không phải là tam giác')
        self.assertEqual(tamgiac(1, 1, 0), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_canh_am(self):
        self.assertEqual(tamgiac(-1, -1, -1), 'Không phải là tam giác')
        self.assertEqual(tamgiac(-1, 2, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(2, -1, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(2, 3, -1), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_a_bang_b_cong_c(self):
        self.assertEqual(tamgiac(5, 2, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(10, 4, 6), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_b_bang_a_cong_c(self):
        self.assertEqual(tamgiac(2, 5, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(4, 10, 6), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_c_bang_a_cong_b(self):
        self.assertEqual(tamgiac(2, 3, 5), 'Không phải là tam giác')
        self.assertEqual(tamgiac(4, 6, 10), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_a_lon_hon_b_cong_c(self):
        self.assertEqual(tamgiac(10, 2, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(15, 4, 5), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_b_lon_hon_a_cong_c(self):
        self.assertEqual(tamgiac(2, 10, 3), 'Không phải là tam giác')
        self.assertEqual(tamgiac(4, 15, 5), 'Không phải là tam giác')
    
    def test_khong_phai_tam_giac_c_lon_hon_a_cong_b(self):
        self.assertEqual(tamgiac(2, 3, 10), 'Không phải là tam giác')
        self.assertEqual(tamgiac(4, 5, 15), 'Không phải là tam giác')
    
    def test_bien_tam_giac_deu_nho_nhat(self):
        self.assertEqual(tamgiac(1, 1, 1), 'Tam giác đều')
    
    def test_bien_tam_giac_can_nho_nhat(self):
        self.assertEqual(tamgiac(2, 2, 1), 'Tam giác cân')
    
    def test_bien_tam_giac_thuong_nho_nhat(self):
        self.assertEqual(tamgiac(2, 3, 4), 'Tam giác thường')


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTamGiac)
    
    with open('ketqua.html', 'w', encoding='utf-8') as f:
        runner = HTMLTestRunner(
            stream=f,
            title='Kết quả kiểm thử hàm tamgiac()',
            description='Sử dụng bảng quyết định và lớp tương đương',
            verbosity=2
        )
        result = runner.run(suite)
    
    print(f"\nĐã chạy {result.testsRun} test cases")
    print(f"Thành công: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Thất bại: {len(result.failures)}")
    print(f"Lỗi: {len(result.errors)}")
    print(f"\nKết quả đã được lưu vào file: ketqua.html")

