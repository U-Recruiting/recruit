-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-11-13 09:52:39
-- 服务器版本： 5.6.30
-- PHP Version: 7.1.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `recruit4`
--

-- --------------------------------------------------------

--
-- 表的结构 `index_job_label2`
--

CREATE TABLE `index_job_label2` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `parent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `index_job_label2`
--

INSERT INTO `index_job_label2` (`id`, `name`, `parent_id`) VALUES
(1, '软件', 1),
(2, '运营', 1),
(3, '硬件', 1),
(4, '设计', 1),
(5, '通信', 1),
(6, '产品', 1),
(7, '商务', 2),
(8, '销售', 2),
(9, '公关', 2),
(10, '客服', 2),
(11, '市场', 2),
(12, '电子', 3),
(13, '电气', 3),
(14, '人力资源', 4),
(15, '猎头', 4),
(16, '行政', 4),
(17, '外语', 5),
(18, '外贸', 5),
(19, '金融', 6),
(20, '投资', 6),
(21, '法务', 6),
(22, '银行', 6),
(23, '保险', 6),
(24, '财会', 6),
(25, '广告', 7),
(26, '编辑', 7),
(27, '设计', 7),
(28, '媒体', 7),
(29, '艺术', 7),
(30, '教育', 8),
(31, '咨询', 8),
(32, '建筑房产', 9),
(33, '机械制造', 9),
(34, '体育快消', 9),
(35, '生物医疗', 9),
(36, '物流采购', 9),
(37, '食品材料', 9),
(38, '能源环保', 9),
(39, 'NGO公益', 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `index_job_label2`
--
ALTER TABLE `index_job_label2`
  ADD PRIMARY KEY (`id`),
  ADD KEY `index_job_label2_parent_id_86d2ad3c_fk_index_job_label1_id` (`parent_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `index_job_label2`
--
ALTER TABLE `index_job_label2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- 限制导出的表
--

--
-- 限制表 `index_job_label2`
--
ALTER TABLE `index_job_label2`
  ADD CONSTRAINT `index_job_label2_parent_id_86d2ad3c_fk_index_job_label1_id` FOREIGN KEY (`parent_id`) REFERENCES `index_job_label1` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
