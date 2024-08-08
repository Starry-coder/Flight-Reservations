-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: flights
-- ------------------------------------------------------
-- Server version	5.1.33-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flights` (
  `f_id` char(4) NOT NULL,
  `f_company` varchar(30) DEFAULT NULL,
  `f_startdate` char(10) DEFAULT NULL,
  `f_starttime` char(8) DEFAULT NULL,
  `f_reachtime` char(8) DEFAULT NULL,
  `f_enddate` char(10) DEFAULT NULL,
  `f_price` varchar(30) DEFAULT NULL,
  `f_startloc` varchar(50) DEFAULT NULL,
  `f_endloc` varchar(50) DEFAULT NULL,
  `f_returndate` char(10) DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES ('AA01','Air Asia','2021-12-24','14:00:00','17:00:00','2021-12-24','Rs. 6999','Ahmedabad','Jaipur',NULL),('AI01','Air India','2021-12-24','08:00:00','10:00:00','2021-12-24','Rs. 7999','Ahmedabad','Jaipur',NULL),('AI02','Air India','2022-12-24','13:30:00','15:00:00','2022-12-24','Rs. 5749','Ahmedabad','Jaipur','2022-12-25'),('IG01','Indigo','2021-12-24','22:30:00','23:50:00','2021-12-24','Rs. 6999','Ahmedabad','Jaipur',NULL),('SJ01','Spice Jet','2021-12-24','06:00:00','07:30:00','2021-12-24','Rs. 9999','Ahmedabad','Jaipur',NULL),('TES1','Test Flight','2021-12-24','10:00:00','12:00:00','2021-12-24','Rs. 9999','Ahmedabad','Jaipur','2021-12-25'),('TES2','Test Flight','2021-12-24','01:30:00','03:00:00','2021-12-24','Rs 4569','Ahmedabad','Jaipur','2021-12-25'),('VT01','Vistara','2021-12-24','05:30:00','07:30:00','2021-12-24','Rs. 7299','Ahmedabad','Jaipur',NULL);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `usr_id` char(6) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `pas` varchar(30) NOT NULL,
  `phno` bigint(20) NOT NULL,
  `address` varchar(150) NOT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`usr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('AK1502','Aryan Kumar','aarryyaann1502051@gmail.com','Aryan123',9979894244,'Mahaveer Nagar, Jaipur',16),('VR0001','Vyom Rathore','rathorevyom04@gmail.com','Vyom123',9649944555,'Vaishali Nagar, Jaipur',16);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passengers`
--

DROP TABLE IF EXISTS `passengers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `passengers` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `phno` char(10) NOT NULL,
  `f_id` char(4) NOT NULL,
  `f_startdate` char(10) NOT NULL,
  `f_starttime` char(8) NOT NULL,
  `f_startloc` varchar(50) NOT NULL,
  `f_endloc` varchar(50) NOT NULL,
  `seattype` varchar(20) DEFAULT NULL,
  `tripytpe` varchar(20) DEFAULT NULL,
  `f_returndate` char(10) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passengers`
--

LOCK TABLES `passengers` WRITE;
/*!40000 ALTER TABLE `passengers` DISABLE KEYS */;
INSERT INTO `passengers` VALUES (10,'Vyom Rathore','6775878780','VT01','2021-12-24','05:30:00','Ahmedabad','Jaipur','Business Class','One Way',NULL),(18,'Preeti Lilhore','9979894245','SJ01','2021-12-24','05:30:00','Ahmedabad','Jaipur','Business Class','One Way',NULL),(19,'Aryan Kumar','9979894244','AI01','2021-12-24','22:30:00','Ahmedabad','Jaipur','Economy','One Way',NULL);
/*!40000 ALTER TABLE `passengers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-21  6:01:15
