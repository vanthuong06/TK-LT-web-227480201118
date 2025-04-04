-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 04, 2025 at 09:13 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quanlyhocsinh`
--

-- --------------------------------------------------------

--
-- Table structure for table `giaovien`
--

CREATE TABLE `giaovien` (
  `ma_gv` int(11) NOT NULL,
  `ten_gv` varchar(100) NOT NULL,
  `gioi_tinh` enum('Nam','Nữ') DEFAULT 'Nam',
  `ngay_sinh` date DEFAULT NULL,
  `so_dien_thoai` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dia_chi` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `giaovien`
--

INSERT INTO `giaovien` (`ma_gv`, `ten_gv`, `gioi_tinh`, `ngay_sinh`, `so_dien_thoai`, `email`, `dia_chi`) VALUES
(1, 'Nguyễn Văn A', 'Nam', '1980-05-10', '0912345678', 'nguyenvana@gmail.com', 'TP. HCM'),
(2, 'Trần Thị B', 'Nữ', '1985-09-20', '0987654321', 'tranthib@gmail.com', 'Hà Nội'),
(3, 'Lê Văn C', 'Nam', '1978-12-15', '0901234567', 'levanc@gmail.com', 'Đà Nẵng');

-- --------------------------------------------------------

--
-- Table structure for table `hocsinh`
--

CREATE TABLE `hocsinh` (
  `ma_hs` int(11) NOT NULL,
  `ten_hs` varchar(100) NOT NULL,
  `gioi_tinh` enum('Nam','Nữ') DEFAULT 'Nam',
  `ngay_sinh` date DEFAULT NULL,
  `lop` varchar(20) DEFAULT NULL,
  `dia_chi` text DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hocsinh`
--

INSERT INTO `hocsinh` (`ma_hs`, `ten_hs`, `gioi_tinh`, `ngay_sinh`, `lop`, `dia_chi`, `email`) VALUES
(1, 'Phạm Minh D', 'Nam', '2005-04-01', '12A1', 'Cần Thơ', 'phamminhd@gmail.com'),
(2, 'Ngô Thị E', 'Nữ', '2006-07-15', '11B2', 'Vĩnh Long', 'ngothie@gmail.com'),
(3, 'Trần Văn F', 'Nam', '2005-09-10', '12A2', 'TP. HCM', 'tranvanf@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `monhoc`
--

CREATE TABLE `monhoc` (
  `ma_mh` int(11) NOT NULL,
  `ten_mh` varchar(100) NOT NULL,
  `ma_gv` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `monhoc`
--

INSERT INTO `monhoc` (`ma_mh`, `ten_mh`, `ma_gv`) VALUES
(1, 'Toán học', 1),
(2, 'Vật lý', 2),
(3, 'Hóa học', 3),
(4, 'Tiếng Anh', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `giaovien`
--
ALTER TABLE `giaovien`
  ADD PRIMARY KEY (`ma_gv`);

--
-- Indexes for table `hocsinh`
--
ALTER TABLE `hocsinh`
  ADD PRIMARY KEY (`ma_hs`);

--
-- Indexes for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`ma_mh`),
  ADD KEY `ma_gv` (`ma_gv`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `giaovien`
--
ALTER TABLE `giaovien`
  MODIFY `ma_gv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hocsinh`
--
ALTER TABLE `hocsinh`
  MODIFY `ma_hs` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `monhoc`
--
ALTER TABLE `monhoc`
  MODIFY `ma_mh` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD CONSTRAINT `monhoc_ibfk_1` FOREIGN KEY (`ma_gv`) REFERENCES `giaovien` (`ma_gv`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
