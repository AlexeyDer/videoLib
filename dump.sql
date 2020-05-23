-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: videoLib
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Dumping data for table `film_info`
--

LOCK TABLES `film_info` WRITE;
/*!40000 ALTER TABLE `film_info` DISABLE KEYS */;
INSERT INTO `film_info` VALUES (1,'The Shawshank Redemption','Drama','Frank Darabont','USA','Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler, Clancy Brown Gil Bellows James Whitmore','Banker Andy Dufresne is convicted of murdering his wife and her lover and is sentenced to two consecutive life sentences at the Shawshank State Penitentiary. He is befriended by Ellis \"Red\" Redding,an inmate and prison.'),(2,'The Intouchables','Drama','Nicolas Duval Adassovsky, Yann Zenou','France','François Cluzet, Omar Sy','At night in Paris, Driss is driving Philippe\'s Maserati Quattroporte at high speed. They are chased through the streets by the police and eventually cornered. Driss claims the quadriplegic Philippe must be urgently driven to the emergency room;'),(3,'Joker','Drama','Todd Phillips','USA','Joaquin Phoenix, Robert De Niro, Zazie Beetz ,Frances Conroy','Fleck lives with his mother, Penny, in Gotham City. Gotham is rife with crime and unemployment, leaving swathes of the population disenfranchised and impoverished. Arthur suffers from a medical disorder that causes him to laugh at inappropriate times'),(4,'Heroes','Drama','David Foster','United States','Henry Winkler, Sally Field, Harrison Ford, Val Avery','At the bus station,he accidentally meets Carol Bell,a woman unsure of her engagement to man towards whom she has confused feelings.Initially annoyed by Jack, Carol gradually warms to him as they set off on a trip through America'),(5,'Spider-Man','action','Sam Raimi','United States','Tobey Maguire, Willem Dafoe ,Kirsten Dunst, James Franco, Cliff Robertson, Rosemary Harris','Peter Parker (Toby Maguire) is a simple schoolboy, an ordinary nerd, suffering from unrequited love for his classmate, charming Mary Jane Watson (Kirsten Dunst). Relations with peers do not add up, classmates either do not notice him or mock him.');
/*!40000 ALTER TABLE `film_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `given`
--

LOCK TABLES `given` WRITE;
/*!40000 ALTER TABLE `given` DISABLE KEYS */;
INSERT INTO `given` VALUES (1,'Ivanov Petr Ivanovich','02.02.20','Harry Potter'),(2,'Stepanov Danil Alexeevich','06.05.2020','indiana jones');
/*!40000 ALTER TABLE `given` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ivanov Petr Ivanovich','Lenina 10'),(2,'Stepanov Danil Alexeevich','Pushkina 20'),(3,'Demidov Karl Osipovich','Borisa Bogatkova 15'),(4,'Merkulov Vladislav Andreevich','Bazovaya 15'),(5,'Makarov Daril Andreevich','Lenina 86'),(6,'Osipov Nikita Vladislavovich','Svoboda 7'),(7,'Morozov Maxim Aduardovich','Kirova 8'),(8,'Dolmatov Dmitriy Petrovich','Smolina 26'),(9,'Mihailiv Petr Igorevich','Stalina 5'),(10,'Borisov Andrey Filipovich','Nevskiy Prospect 11');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-23 18:42:41
