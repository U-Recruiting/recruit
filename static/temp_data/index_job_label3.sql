-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-11-13 09:52:49
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
-- 表的结构 `index_job_label3`
--

CREATE TABLE `index_job_label3` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `parent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `index_job_label3`
--

INSERT INTO `index_job_label3` (`id`, `name`, `parent_id`) VALUES
(1, '数据库', 1),
(2, 'C#/.NET', 1),
(3, 'Hadoop', 1),
(4, 'Android', 1),
(5, '算法', 1),
(6, 'IT运维', 1),
(7, 'Python云计算/大数据', 1),
(8, 'Node.js数据挖掘', 1),
(9, 'PHP', 1),
(10, 'Ruby/Perl测试', 1),
(11, 'Java', 1),
(12, 'C/C++', 1),
(13, '前端', 1),
(14, '新媒体', 2),
(15, '内容运营', 2),
(16, '编辑', 2),
(17, 'SEO产品运营', 2),
(18, '嵌入式', 3),
(19, '集成电路', 3),
(20, 'Flash', 4),
(21, 'UI/UE特效', 4),
(22, '网页/美工', 4),
(23, '2D/3D', 4),
(24, '物联网', 5),
(25, '射频', 5),
(26, '通信', 5),
(27, '用户研究', 6),
(28, '产品经理', 6),
(29, '商务', 7),
(30, '招投标', 7),
(31, '销售', 8),
(32, '推广', 8),
(33, '公关', 9),
(34, '媒介', 9),
(35, '客户服务', 10),
(36, '销售支持', 10),
(37, '渠道', 11),
(38, '分析/调研', 11),
(39, '策划', 11),
(40, '品牌', 11),
(41, '市场', 11),
(42, '光电', 12),
(43, '半导体/芯片', 12),
(44, '电子工程', 12),
(45, '电气设计', 13),
(46, '电气工程', 13),
(47, '人事/HR企业文化', 14),
(48, '招聘', 14),
(49, '内容运营', 14),
(50, '猎头', 15),
(51, '行政', 16),
(52, '前台', 16),
(53, '助理', 16),
(54, '英语', 17),
(55, '日语', 17),
(56, '翻译', 17),
(57, '报关员', 18),
(58, '外贸专员', 18),
(59, '基金', 19),
(60, '证券', 19),
(61, '风控', 19),
(62, '金融', 19),
(63, '分析师', 20),
(64, '投资', 20),
(65, '合规', 21),
(66, '律师', 21),
(67, '法务', 21),
(68, '客户经理', 22),
(69, '部门经理', 22),
(70, '贷款', 22),
(71, '大堂经理', 22),
(72, '业务', 23),
(73, '保单', 23),
(74, '审计', 24),
(75, '税务', 24),
(76, '财务', 24),
(77, '会计/出纳', 24),
(78, '创意', 25),
(79, '策划', 25),
(80, 'AE', 25),
(81, '编辑/采编', 26),
(82, '校对/排版', 26),
(83, '美工设计', 27),
(84, '工业设计', 27),
(85, '平面设计', 27),
(86, '视觉设计', 27),
(87, '记者', 28),
(88, '主持/播音', 28),
(89, '编导', 28),
(90, '演艺', 29),
(91, '摄影', 29),
(92, '教务', 30),
(93, '教师', 30),
(94, '幼教', 30),
(95, '培训', 30),
(96, '课程', 30),
(97, '咨询/顾问', 31),
(98, '城规/市政', 32),
(99, '工程造价', 32),
(100, '建筑', 32),
(101, '土木', 32),
(102, '园林', 32),
(103, '地产开发/策划', 32),
(104, '房产销售', 32),
(105, '给排水', 32),
(106, '物业管理', 32),
(107, '质量', 33),
(108, '机械设计', 33),
(109, '生产', 33),
(110, '安全', 33),
(111, '设备', 33),
(112, '自动化', 33),
(113, '体育', 34),
(114, '快消', 34),
(115, '医生', 35),
(116, '医药', 35),
(117, '生物', 35),
(118, '护理', 35),
(119, '采购', 36),
(120, '供应链', 36),
(121, '物流', 36),
(122, '材料', 37),
(123, '食品', 37),
(124, '矿产', 38),
(125, '能源', 38),
(126, '环保', 38),
(127, '志愿者', 39);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `index_job_label3`
--
ALTER TABLE `index_job_label3`
  ADD PRIMARY KEY (`id`),
  ADD KEY `index_job_label3_parent_id_002771a7_fk_index_job_label2_id` (`parent_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `index_job_label3`
--
ALTER TABLE `index_job_label3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;
--
-- 限制导出的表
--

--
-- 限制表 `index_job_label3`
--
ALTER TABLE `index_job_label3`
  ADD CONSTRAINT `index_job_label3_parent_id_002771a7_fk_index_job_label2_id` FOREIGN KEY (`parent_id`) REFERENCES `index_job_label2` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
