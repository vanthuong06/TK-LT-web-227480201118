"""
Câu 2: Lớp giỏ hàng với các phương thức quản lý
"""


class MatHang:
    """Lớp đại diện cho một mặt hàng"""
    
    def __init__(self, ten, gia):
        """
        Khởi tạo mặt hàng
        
        Args:
            ten: Tên mặt hàng
            gia: Giá mặt hàng
        """
        self.ten = ten
        self.gia = gia
    
    def __repr__(self):
        return f"MatHang(ten='{self.ten}', gia={self.gia})"
    
    def __eq__(self, other):
        if isinstance(other, MatHang):
            return self.ten == other.ten and self.gia == other.gia
        return False


class GioHang:
    """Lớp quản lý giỏ hàng"""
    
    def __init__(self):
        """Khởi tạo giỏ hàng rỗng"""
        self._danh_sach_mat_hang = []
    
    def tao_gio_hang(self):
        """
        Tạo giỏ hàng mới (khởi tạo lại giỏ hàng)
        
        Returns:
            GioHang: Giỏ hàng mới
        """
        self._danh_sach_mat_hang = []
        return self
    
    def them_mat_hang(self, mat_hang):
        """
        Thêm mặt hàng vào giỏ hàng
        
        Args:
            mat_hang: Đối tượng MatHang cần thêm
        
        Returns:
            bool: True nếu thêm thành công
        """
        if isinstance(mat_hang, MatHang):
            self._danh_sach_mat_hang.append(mat_hang)
            return True
        return False
    
    def dem_so_mat_hang(self):
        """
        Đếm số lượng mặt hàng trong giỏ
        
        Returns:
            int: Số lượng mặt hàng
        """
        return len(self._danh_sach_mat_hang)
    
    def xem_cac_mat_hang(self):
        """
        Xem danh sách các mặt hàng trong giỏ hàng
        
        Returns:
            list: Danh sách các mặt hàng
        """
        return self._danh_sach_mat_hang.copy()
    
    def xoa_mat_hang(self, mat_hang):
        """
        Xóa mặt hàng khỏi giỏ hàng
        
        Args:
            mat_hang: Đối tượng MatHang cần xóa
        
        Returns:
            bool: True nếu xóa thành công, False nếu không tìm thấy
        """
        if mat_hang in self._danh_sach_mat_hang:
            self._danh_sach_mat_hang.remove(mat_hang)
            return True
        return False
    
    def tinh_tong_tien(self):
        """
        Tính tổng tiền trong giỏ hàng
        
        Returns:
            float: Tổng tiền
        """
        return sum(mat_hang.gia for mat_hang in self._danh_sach_mat_hang)

