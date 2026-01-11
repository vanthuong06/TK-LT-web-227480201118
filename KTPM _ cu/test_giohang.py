import pytest
from unittest.mock import Mock, patch
from giohang import GioHang, MatHang


@pytest.fixture
def gio_hang_rong():
    return GioHang()


@pytest.fixture
def gio_hang_co_du_lieu():
    gio_hang = GioHang()
    gio_hang.them_mat_hang(MatHang("Áo sơ mi", 200000))
    gio_hang.them_mat_hang(MatHang("Quần jean", 500000))
    gio_hang.them_mat_hang(MatHang("Giày thể thao", 800000))
    return gio_hang


@pytest.fixture
def mat_hang_mau():
    return MatHang("Áo thun", 150000)


def test_tao_gio_hang(gio_hang_rong):
    gio_hang_moi = gio_hang_rong.tao_gio_hang()
    assert isinstance(gio_hang_moi, GioHang)
    assert gio_hang_moi.dem_so_mat_hang() == 0


def test_them_mat_hang_thanh_cong(gio_hang_rong, mat_hang_mau):
    result = gio_hang_rong.them_mat_hang(mat_hang_mau)
    assert result is True
    assert gio_hang_rong.dem_so_mat_hang() == 1


def test_them_mat_hang_khong_hop_le(gio_hang_rong):
    result = gio_hang_rong.them_mat_hang("không phải MatHang")
    assert result is False
    assert gio_hang_rong.dem_so_mat_hang() == 0


def test_them_nhieu_mat_hang(gio_hang_rong):
    mat_hang1 = MatHang("Sản phẩm 1", 100000)
    mat_hang2 = MatHang("Sản phẩm 2", 200000)
    mat_hang3 = MatHang("Sản phẩm 3", 300000)
    
    gio_hang_rong.them_mat_hang(mat_hang1)
    gio_hang_rong.them_mat_hang(mat_hang2)
    gio_hang_rong.them_mat_hang(mat_hang3)
    
    assert gio_hang_rong.dem_so_mat_hang() == 3


def test_dem_so_mat_hang_gio_rong(gio_hang_rong):
    assert gio_hang_rong.dem_so_mat_hang() == 0


def test_dem_so_mat_hang_gio_co_du_lieu(gio_hang_co_du_lieu):
    assert gio_hang_co_du_lieu.dem_so_mat_hang() == 3


def test_xem_cac_mat_hang_gio_rong(gio_hang_rong):
    danh_sach = gio_hang_rong.xem_cac_mat_hang()
    assert isinstance(danh_sach, list)
    assert len(danh_sach) == 0


def test_xem_cac_mat_hang_gio_co_du_lieu(gio_hang_co_du_lieu):
    danh_sach = gio_hang_co_du_lieu.xem_cac_mat_hang()
    assert isinstance(danh_sach, list)
    assert len(danh_sach) == 3
    assert all(isinstance(mh, MatHang) for mh in danh_sach)


def test_xem_cac_mat_hang_tra_ve_ban_sao(gio_hang_co_du_lieu):
    danh_sach1 = gio_hang_co_du_lieu.xem_cac_mat_hang()
    danh_sach2 = gio_hang_co_du_lieu.xem_cac_mat_hang()
    assert danh_sach1 is not danh_sach2
    assert danh_sach1 == danh_sach2


def test_xoa_mat_hang_thanh_cong(gio_hang_co_du_lieu):
    mat_hang_can_xoa = MatHang("Áo sơ mi", 200000)
    result = gio_hang_co_du_lieu.xoa_mat_hang(mat_hang_can_xoa)
    assert result is True
    assert gio_hang_co_du_lieu.dem_so_mat_hang() == 2


def test_xoa_mat_hang_khong_ton_tai(gio_hang_co_du_lieu):
    mat_hang_khong_ton_tai = MatHang("Sản phẩm không tồn tại", 100000)
    result = gio_hang_co_du_lieu.xoa_mat_hang(mat_hang_khong_ton_tai)
    assert result is False
    assert gio_hang_co_du_lieu.dem_so_mat_hang() == 3


def test_xoa_mat_hang_gio_rong(gio_hang_rong, mat_hang_mau):
    result = gio_hang_rong.xoa_mat_hang(mat_hang_mau)
    assert result is False


def test_tinh_tong_tien_gio_rong(gio_hang_rong):
    assert gio_hang_rong.tinh_tong_tien() == 0


def test_tinh_tong_tien_gio_co_du_lieu(gio_hang_co_du_lieu):
    tong_tien = gio_hang_co_du_lieu.tinh_tong_tien()
    assert tong_tien == 1500000


def test_tinh_tong_tien_sau_khi_them(gio_hang_rong):
    gio_hang_rong.them_mat_hang(MatHang("SP1", 100000))
    gio_hang_rong.them_mat_hang(MatHang("SP2", 200000))
    assert gio_hang_rong.tinh_tong_tien() == 300000


def test_tinh_tong_tien_sau_khi_xoa(gio_hang_co_du_lieu):
    mat_hang_xoa = MatHang("Áo sơ mi", 200000)
    gio_hang_co_du_lieu.xoa_mat_hang(mat_hang_xoa)
    assert gio_hang_co_du_lieu.tinh_tong_tien() == 1300000


def test_them_mat_hang_voi_mock(gio_hang_rong):
    mock_mat_hang = Mock(spec=MatHang)
    mock_mat_hang.ten = "Mock Product"
    mock_mat_hang.gia = 100000
    
    result = gio_hang_rong.them_mat_hang(mock_mat_hang)
    assert result is True
    assert gio_hang_rong.dem_so_mat_hang() == 1


def test_tinh_tong_tien_voi_mock(gio_hang_rong):
    mock_mat_hang1 = Mock()
    mock_mat_hang1.gia = 100000
    
    mock_mat_hang2 = Mock()
    mock_mat_hang2.gia = 200000
    
    gio_hang_rong._danh_sach_mat_hang = [mock_mat_hang1, mock_mat_hang2]
    
    tong_tien = gio_hang_rong.tinh_tong_tien()
    assert tong_tien == 300000


@patch.object(GioHang, 'them_mat_hang')
def test_them_mat_hang_voi_patch(mock_them_mat_hang, gio_hang_rong):
    mock_them_mat_hang.return_value = True
    
    mat_hang = MatHang("Test", 100000)
    result = gio_hang_rong.them_mat_hang(mat_hang)
    
    assert result is True
    mock_them_mat_hang.assert_called_once_with(mat_hang)


def test_xem_cac_mat_hang_voi_mock(gio_hang_rong):
    mock_mat_hang1 = Mock(spec=MatHang)
    mock_mat_hang2 = Mock(spec=MatHang)
    
    gio_hang_rong._danh_sach_mat_hang = [mock_mat_hang1, mock_mat_hang2]
    
    danh_sach = gio_hang_rong.xem_cac_mat_hang()
    assert len(danh_sach) == 2
    assert danh_sach[0] is mock_mat_hang1
    assert danh_sach[1] is mock_mat_hang2

