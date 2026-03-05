-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2026 at 01:43 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `osp`
--
CREATE DATABASE IF NOT EXISTS `osp` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `osp`;

-- --------------------------------------------------------

--
-- Table structure for table `booth`
--

DROP TABLE IF EXISTS `booth`;
CREATE TABLE `booth` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `user` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `event` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `table_count` int(11) DEFAULT NULL,
  `chair_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `booth`
--

TRUNCATE TABLE `booth`;
--
-- Dumping data for table `booth`
--

INSERT INTO `booth` (`uid`, `disabled`, `user`, `first_name`, `last_name`, `event`, `status`, `email`, `telephone`, `note`, `table_count`, `chair_count`) VALUES
(1, 0, 1, 'Max', 'Mustermann', 1, 1, 'max@mustermann.de', '0221 000000', '', 2, 2),
(2, 0, 1, 'Peter', 'Lustig', 2, 1, 'peter@lustig.de', '0221 000000', '', 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
CREATE TABLE `event` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `name` varchar(255) NOT NULL,
  `date` date DEFAULT NULL,
  `slots` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `event`
--

TRUNCATE TABLE `event`;
--
-- Dumping data for table `event`
--

INSERT INTO `event` (`uid`, `disabled`, `name`, `date`, `slots`) VALUES
(1, 0, 'Tag der Ausbildung Tag 1', '2026-02-05', 20),
(2, 0, 'Tag der Ausbildung Tag 2', '2026-02-06', 20);

-- --------------------------------------------------------

--
-- Table structure for table `lecture`
--

DROP TABLE IF EXISTS `lecture`;
CREATE TABLE `lecture` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `user` int(11) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `event` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `note` varchar(255) DEFAULT NULL,
  `topic` varchar(255) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `lecture`
--

TRUNCATE TABLE `lecture`;
--
-- Dumping data for table `lecture`
--

INSERT INTO `lecture` (`uid`, `disabled`, `user`, `first_name`, `last_name`, `event`, `status`, `email`, `telephone`, `note`, `topic`, `duration`) VALUES
(1, 0, 1, 'Max', 'Mustermann', 1, 1, 'max@musterman.de', '0221 000000', '', 'Meine Lesung', 2),
(2, 0, 1, 'Peter', 'Lustig', 1, 1, 'peter@lustig.de', '0221 000000', '', 'Lektüre Beispiel', 3);

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
CREATE TABLE `notification` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `user` int(11) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `deleted` tinyint(1) DEFAULT NULL,
  `headline` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `notification`
--

TRUNCATE TABLE `notification`;
--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`uid`, `disabled`, `user`, `message`, `timestamp`, `deleted`, `headline`) VALUES
(1, 0, 1, 'Test Message', '2026-03-05 11:56:48', 0, 'Überschrift'),
(2, 0, 1, 'Zweite Test Message', '2026-03-05 11:56:48', 0, 'Headline');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `role`
--

TRUNCATE TABLE `role`;
--
-- Dumping data for table `role`
--

INSERT INTO `role` (`uid`, `disabled`, `name`) VALUES
(1, 0, 'Ausbildungsbetriebe'),
(2, 0, 'Organisatonsteam'),
(3, 0, 'Lehrer');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
CREATE TABLE `status` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `status`
--

TRUNCATE TABLE `status`;
--
-- Dumping data for table `status`
--

INSERT INTO `status` (`uid`, `disabled`, `name`) VALUES
(1, 0, 'In Bearbeitung'),
(2, 0, 'Abgelehnt'),
(3, 0, 'Angenommen');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `disabled` int(11) NOT NULL DEFAULT 0,
  `company` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `role` int(11) DEFAULT NULL,
  `donation` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Truncate table before insert `user`
--

TRUNCATE TABLE `user`;
--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `disabled`, `company`, `email`, `password_hash`, `role`, `donation`) VALUES
(1, 0, 'Stadt Köln', 'ausbildung@stadt-koeln.de', '2705e745988460eb71c071d4b12f46ee', 1, 0),
(2, 0, 'GSO', 'a.feser@gso.schule.koeln', '2705e745988460eb71c071d4b12f46ee', 2, 0),
(3, 0, 'GSO', 'm.bauer@gso.schule.koeln', '2705e745988460eb71c071d4b12f46ee', 2, 0),
(4, 0, 'GSO', 'b.wolf@gso.schule.koeln', '2705e745988460eb71c071d4b12f46ee', 3, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booth`
--
ALTER TABLE `booth`
  ADD PRIMARY KEY (`uid`),
  ADD KEY `user` (`user`),
  ADD KEY `event` (`event`),
  ADD KEY `status` (`status`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `lecture`
--
ALTER TABLE `lecture`
  ADD PRIMARY KEY (`uid`),
  ADD KEY `status` (`status`),
  ADD KEY `user` (`user`),
  ADD KEY `event` (`event`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`uid`),
  ADD KEY `User` (`user`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `Name` (`name`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`),
  ADD UNIQUE KEY `Email` (`email`),
  ADD KEY `Role` (`role`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booth`
--
ALTER TABLE `booth`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `lecture`
--
ALTER TABLE `lecture`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booth`
--
ALTER TABLE `booth`
  ADD CONSTRAINT `booth_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`uid`),
  ADD CONSTRAINT `booth_ibfk_2` FOREIGN KEY (`event`) REFERENCES `event` (`uid`),
  ADD CONSTRAINT `booth_ibfk_3` FOREIGN KEY (`status`) REFERENCES `status` (`uid`);

--
-- Constraints for table `lecture`
--
ALTER TABLE `lecture`
  ADD CONSTRAINT `lecture_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`uid`),
  ADD CONSTRAINT `lecture_ibfk_2` FOREIGN KEY (`status`) REFERENCES `status` (`uid`),
  ADD CONSTRAINT `lecture_ibfk_3` FOREIGN KEY (`event`) REFERENCES `event` (`uid`);

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`uid`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role`) REFERENCES `role` (`uid`);
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
