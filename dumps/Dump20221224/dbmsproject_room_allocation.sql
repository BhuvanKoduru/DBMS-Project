-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: dbmsproject
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `room_allocation`
--

DROP TABLE IF EXISTS `room_allocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_allocation` (
  `730_830` varchar(10) DEFAULT NULL,
  `830_930` varchar(10) DEFAULT NULL,
  `930_1030` varchar(10) DEFAULT NULL,
  `1100_1150` varchar(10) DEFAULT NULL,
  `1150_1240` varchar(10) DEFAULT NULL,
  `1240_130` varchar(10) DEFAULT NULL,
  `230_330` varchar(10) DEFAULT NULL,
  `330_430` varchar(10) DEFAULT NULL,
  `430_530` varchar(10) DEFAULT NULL,
  `Day` varchar(5) NOT NULL,
  `Sem` int NOT NULL,
  PRIMARY KEY (`Day`,`Sem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_allocation`
--

LOCK TABLES `room_allocation` WRITE;
/*!40000 ALTER TABLE `room_allocation` DISABLE KEYS */;
INSERT INTO `room_allocation` VALUES (NULL,NULL,NULL,'IS103','IS103','IS103','IS103','IS103',NULL,'FRI',7),(NULL,NULL,NULL,'IS103','IS103','IS103','IS103','IS103','IS103','MON',7),(NULL,NULL,NULL,'IS002','IS002','IS002',NULL,NULL,NULL,'SAT',7),(NULL,'IS103','IS103',NULL,NULL,NULL,NULL,NULL,NULL,'THR',7),(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TUE',7),(NULL,NULL,NULL,'IS001','IS001','IS001','IS001','IS001','IS001','WED',7);
/*!40000 ALTER TABLE `room_allocation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-24 10:21:48
