-- MySQL dump 10.13  Distrib 5.7.22, for macos10.13 (x86_64)
--
-- Host: localhost    Database: UserTest_db
-- ------------------------------------------------------
-- Server version	5.7.22

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
-- Table structure for table `user_duplicates`
--

DROP TABLE IF EXISTS `user_duplicates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_duplicates` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `username` varchar(35) DEFAULT NULL,
  `visits` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_duplicates`
--

LOCK TABLES `user_duplicates` WRITE;
/*!40000 ALTER TABLE `user_duplicates` DISABLE KEYS */;
INSERT INTO `user_duplicates` VALUES (1,'test3',43),(3,'newName',43),(5,'seePrint',42),(6,'john',43),(8,'Jean',80),(48,'Benny',48),(55,'Lucky Man',70),(84,'JollyBee',44),(87,'Person',42),(88,'Jamison',42),(89,'Parson',44),(92,'Jason',42),(93,'George',43),(94,'one',42),(96,'Hello',42),(97,'aaabbb',42),(98,'lunch',42),(99,'Bob',43),(101,'Chris',43),(103,'Gregg',47),(108,'Jphlkjlkj',43),(109,'Jarvis',43),(110,'Fang',35),(111,'Megan',25),(112,'newName2',16),(113,'newName3',16),(114,'newName4',16),(115,'newName5',16),(116,'newName6',16),(117,'newName7',16),(118,'newName8',15),(119,'newName9',15),(120,'June',15),(121,'July',14),(122,'August',11),(123,'Ana',11),(124,'Ben',10),(125,'September',9),(126,'October',8),(127,'Barney',6),(128,'November',5),(129,'December',2),(130,'Blueberry',1);
/*!40000 ALTER TABLE `user_duplicates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userdata` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `username` text,
  `email` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES (1,'Ana','ana@test.test'),(2,'Ana','ana@test.test'),(3,'BenP','benp@test.tst');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-29 13:54:28
