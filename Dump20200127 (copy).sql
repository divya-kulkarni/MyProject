-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `command`
--

DROP TABLE IF EXISTS `command`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `command` (
  `cno` int(11) NOT NULL,
  `CommandID` int(11) DEFAULT NULL,
  `TokenID` int(11) DEFAULT NULL,
  `PositionInCommand` int(11) DEFAULT NULL,
  PRIMARY KEY (`cno`),
  KEY `CommandID` (`CommandID`),
  KEY `TokenID` (`TokenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `command`
--

LOCK TABLES `command` WRITE;
/*!40000 ALTER TABLE `command` DISABLE KEYS */;
INSERT INTO `command` VALUES (1,1,1,1),(2,1,2,2),(3,1,3,3),(4,1,24,4),(5,1,24,5),(6,2,1,1),(7,2,4,2),(8,2,26,3),(9,2,3,4),(10,3,1,1),(11,3,5,2),(12,3,25,3),(13,3,24,4),(14,3,3,5),(15,3,24,6),(16,4,1,1),(17,4,21,2),(18,4,25,3),(19,4,24,4),(20,4,3,5),(21,4,24,6),(22,5,6,1),(23,5,24,2),(24,5,3,3),(25,5,7,4),(26,6,6,1),(27,6,24,2),(28,6,3,3),(29,6,8,4),(30,7,6,1),(31,7,24,2),(32,7,3,3),(33,7,9,4),(34,8,6,1),(35,8,24,2),(36,8,3,3),(37,8,10,4),(38,9,6,1),(39,9,24,2),(40,9,3,3),(41,9,7,4),(42,9,11,5),(43,9,24,6),(44,9,15,7),(45,10,6,1),(46,10,24,2),(47,10,3,3),(48,10,8,4),(49,10,11,5),(51,10,15,7),(52,2,24,5),(53,11,6,1),(54,11,24,2),(55,11,12,3),(56,11,11,4),(57,11,24,5),(58,11,15,6),(59,12,6,1),(60,12,24,2),(61,12,13,3),(62,12,15,4),(63,12,24,5),(64,12,15,6),(65,13,6,1),(66,13,24,2),(67,13,3,3),(68,13,7,4),(69,13,11,5),(70,13,24,6),(71,13,14,7),(72,14,6,1),(73,14,24,2),(74,14,3,3),(75,14,8,4),(76,14,11,5),(77,14,24,6),(78,14,14,7),(79,15,5,2),(80,14,24,3),(81,15,12,4),(82,15,11,2),(83,15,24,6),(84,15,14,7),(85,16,6,1),(86,16,24,2),(87,16,13,3),(88,16,11,4),(89,16,24,5),(90,16,14,6),(91,17,6,1),(92,17,24,2),(93,17,3,3),(94,17,7,4),(95,17,11,5),(96,17,24,6),(97,17,14,7),(98,18,6,1),(99,18,24,2),(100,18,3,3),(101,18,8,4),(102,18,11,5),(103,18,24,6),(104,18,14,7),(105,19,6,1),(106,19,24,2),(107,19,12,3),(108,19,11,4),(109,19,24,5),(110,19,14,6),(111,20,6,1),(112,20,24,2),(113,20,13,3),(114,20,11,4),(115,20,24,5),(116,20,14,6);
/*!40000 ALTER TABLE `command` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commandmaster`
--

DROP TABLE IF EXISTS `commandmaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commandmaster` (
  `CommandID` int(11) NOT NULL,
  `CommandName` varchar(50) DEFAULT NULL,
  `CommandType` int(11) DEFAULT NULL,
  PRIMARY KEY (`CommandID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commandmaster`
--

LOCK TABLES `commandmaster` WRITE;
/*!40000 ALTER TABLE `commandmaster` DISABLE KEYS */;
INSERT INTO `commandmaster` VALUES (1,'CHNG_TITLE',1),(2,'CHNG_BG',1),(3,'CHNG_WID_DIV',1),(4,'CHNG_HT_DIV',1),(5,'MOV_DIV_LFT',1),(6,'MOV_DIV_RGHT',1),(7,'MOV_DIV_TOP',1),(8,'MOV_DIV_BTM',1),(9,'MOV_DIV_LFT_PRCNT',1),(10,'MOV_DIV_RGHT_PRCNT',1),(11,'MOV_DIV_UP_PRCNT',1),(12,'MOV_DIV_DWN_PRCNT',1),(13,'MOV_DIV_LFT_PXL',1),(14,'MOV_DIV_RGHT_PXL',1),(15,'MOV_DIV_UP_PXL',1),(16,'MOV_DIV_DWN_PXL',1),(17,'MOV_H1_LFT_PXL',1),(18,'MOV_H1_RGHT_PXL',1),(19,'MOV_H1_UP_PXL',1),(20,'MOV_H1_DWN_PXL',1);
/*!40000 ALTER TABLE `commandmaster` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commandtoken`
--

DROP TABLE IF EXISTS `commandtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commandtoken` (
  `cno` int(11) NOT NULL,
  `CommandID` int(11) DEFAULT NULL,
  `TokenID` int(11) DEFAULT NULL,
  `PositionInCommand` int(11) DEFAULT NULL,
  PRIMARY KEY (`cno`),
  KEY `CommandID` (`CommandID`),
  KEY `TokenID` (`TokenID`),
  CONSTRAINT `commandtoken_ibfk_1` FOREIGN KEY (`CommandID`) REFERENCES `commandmaster` (`CommandID`),
  CONSTRAINT `commandtoken_ibfk_2` FOREIGN KEY (`TokenID`) REFERENCES `token` (`TokenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commandtoken`
--

LOCK TABLES `commandtoken` WRITE;
/*!40000 ALTER TABLE `commandtoken` DISABLE KEYS */;
INSERT INTO `commandtoken` VALUES (1,1,1,1),(2,1,2,2),(3,1,3,3),(4,1,24,4),(5,1,24,5),(6,2,1,1),(7,2,4,2),(8,2,26,3),(9,2,3,4),(10,3,1,1),(11,3,5,2),(12,3,25,3),(13,3,24,4),(14,3,3,5),(15,3,24,6),(16,4,1,1),(17,4,21,2),(18,4,25,3),(19,4,24,4),(20,4,3,5),(21,4,24,6),(22,5,6,1),(23,5,24,2),(24,5,3,3),(25,5,7,4),(26,6,6,1),(27,6,24,2),(28,6,3,3),(29,6,8,4),(30,7,6,1),(31,7,24,2),(32,7,3,3),(33,7,9,4),(34,8,6,1),(35,8,24,2),(36,8,3,3),(37,8,10,4),(38,9,6,1),(39,9,24,2),(40,9,3,3),(41,9,7,4),(42,9,11,5),(43,9,24,6),(44,9,15,7),(45,10,6,1),(46,10,24,2),(47,10,3,3),(48,10,8,4),(49,10,11,5),(51,10,15,7),(52,2,24,5),(53,11,6,1),(54,11,24,2),(55,11,12,3),(56,11,11,4),(57,11,24,5),(58,11,15,6),(59,12,6,1),(60,12,24,2),(61,12,13,3),(62,12,15,4),(63,12,24,5),(64,12,15,6),(65,13,6,1),(66,13,24,2),(67,13,3,3),(68,13,7,4),(69,13,11,5),(70,13,24,6),(71,13,14,7),(72,14,6,1),(73,14,24,2),(74,14,3,3),(75,14,8,4),(76,14,11,5),(77,14,24,6),(78,14,14,7),(79,15,5,2),(80,14,24,3),(81,15,12,4),(82,15,11,2),(83,15,24,6),(84,15,14,7),(85,16,6,1),(86,16,24,2),(87,16,13,3),(88,16,11,4),(89,16,24,5),(90,16,14,6),(91,17,6,1),(92,17,24,2),(93,17,3,3),(94,17,7,4),(95,17,11,5),(96,17,24,6),(97,17,14,7),(98,18,6,1),(99,18,24,2),(100,18,3,3),(101,18,8,4),(102,18,11,5),(103,18,24,6),(104,18,14,7),(105,19,6,1),(106,19,24,2),(107,19,12,3),(108,19,11,4),(109,19,24,5),(110,19,14,6),(111,20,6,1),(112,20,24,2),(113,20,13,3),(114,20,11,4),(115,20,24,5),(116,20,14,6);
/*!40000 ALTER TABLE `commandtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commandtype`
--

DROP TABLE IF EXISTS `commandtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commandtype` (
  `ctno` int(11) NOT NULL,
  `commandid` int(11) DEFAULT NULL,
  `commandtype` int(11) DEFAULT NULL,
  PRIMARY KEY (`ctno`),
  KEY `commandid` (`commandid`),
  CONSTRAINT `commandtype_ibfk_1` FOREIGN KEY (`commandid`) REFERENCES `commandtoken` (`CommandID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commandtype`
--

LOCK TABLES `commandtype` WRITE;
/*!40000 ALTER TABLE `commandtype` DISABLE KEYS */;
INSERT INTO `commandtype` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,10,1);
/*!40000 ALTER TABLE `commandtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token` (
  `TokenID` int(11) NOT NULL,
  `Value` varchar(50) DEFAULT NULL,
  `TypeID` int(11) DEFAULT NULL,
  PRIMARY KEY (`TokenID`),
  KEY `TypeID` (`TypeID`),
  CONSTRAINT `token_ibfk_1` FOREIGN KEY (`TypeID`) REFERENCES `tokentype` (`TypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES (1,'CHANGE',1),(2,'TITLE',2),(3,'TO',4),(4,'BACKGROUND',9),(5,'WIDTH',9),(6,'MOVE',1),(7,'LEFT',5),(8,'RIGHT',5),(9,'TOP',5),(10,'BOTTOM',5),(11,'BY',6),(12,'UPWARDS',4),(13,'DOWNWARDS',4),(14,'PIXELS',8),(15,'PERCENT',8),(16,'ADD',1),(17,'DIV',2),(18,'MARGIN',2),(19,'CENTER',5),(20,'HEADER ONE',2),(21,'HEIGHT',9),(22,'ABOVE',5),(23,'BELOW',5),(24,'UNDEFINED',9),(25,'OF',8),(26,'COLOUR',10);
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tokentype`
--

DROP TABLE IF EXISTS `tokentype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tokentype` (
  `TypeID` int(11) NOT NULL,
  `TypeName` varchar(50) DEFAULT NULL,
  `significance` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`TypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tokentype`
--

LOCK TABLES `tokentype` WRITE;
/*!40000 ALTER TABLE `tokentype` DISABLE KEYS */;
INSERT INTO `tokentype` VALUES (1,'ACTION','Add specified thing in HTML'),(2,'ELEMENT','Specifies HTML tag'),(3,'ID','Specifies ID of element'),(4,'DIRECTION','Specifies the direction of action'),(5,'POSITION','Specifies where element is to be placed'),(6,'PREPOSITION','Precedes value'),(7,'VALUE','Precedes value'),(8,'UNIT','Can be pixels or %'),(9,'ATTRIBUTE1','Attribute to be changed of an HTML element'),(10,'ATTRIBUTE2','Attribute to be changed of an HTML element');
/*!40000 ALTER TABLE `tokentype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-27 13:19:15
