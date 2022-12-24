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
-- Table structure for table `is_tt`
--

DROP TABLE IF EXISTS `is_tt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `is_tt` (
  `730_830` varchar(10) DEFAULT NULL,
  `830_930` varchar(10) DEFAULT NULL,
  `930_1030` varchar(10) DEFAULT NULL,
  `1100_1150` varchar(10) DEFAULT NULL,
  `1150_1240` varchar(10) DEFAULT NULL,
  `1240_130` varchar(10) DEFAULT NULL,
  `230_330` varchar(10) DEFAULT NULL,
  `330_430` varchar(10) DEFAULT NULL,
  `430_530` varchar(10) DEFAULT NULL,
  `Day` varchar(10) NOT NULL,
  `Sem` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_tt`
--

LOCK TABLES `is_tt` WRITE;
/*!40000 ALTER TABLE `is_tt` DISABLE KEYS */;
INSERT INTO `is_tt` VALUES (NULL,NULL,'OE','IS540','IS520','IS540','IS530','IS510','PE','MON',5),('IS530','IS510','OE','IS57L','IS57L','IS57L',NULL,NULL,NULL,'TUE',5),(NULL,NULL,'OE','PE','IS540','IS530','IS520','IS530','IS510','WED',5),(NULL,NULL,NULL,'IS540','IS520','PE',NULL,NULL,NULL,'THR',5),(NULL,NULL,'IS540','IS520','IS530','IS510','IS57/58L','IS57/58L','IS57/58L','FRI',5),(NULL,NULL,NULL,'IS58L','IS58L','IS58L',NULL,NULL,NULL,'SAT',5);
/*!40000 ALTER TABLE `is_tt` ENABLE KEYS */;
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
