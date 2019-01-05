-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: Team19
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.16.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add permission',4,'add_permission'),(14,'Can change permission',4,'change_permission'),(15,'Can delete permission',4,'delete_permission'),(16,'Can view permission',4,'view_permission'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add parent projects',7,'add_parentprojects'),(26,'Can change parent projects',7,'change_parentprojects'),(27,'Can delete parent projects',7,'delete_parentprojects'),(28,'Can view parent projects',7,'view_parentprojects'),(29,'Can add belong',8,'add_belong'),(30,'Can change belong',8,'change_belong'),(31,'Can delete belong',8,'delete_belong'),(32,'Can view belong',8,'view_belong'),(33,'Can add project',9,'add_project'),(34,'Can change project',9,'change_project'),(35,'Can delete project',9,'delete_project'),(36,'Can view project',9,'view_project'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add own',11,'add_own'),(42,'Can change own',11,'change_own'),(43,'Can delete own',11,'delete_own'),(44,'Can view own',11,'view_own'),(45,'Can add progress',12,'add_progress'),(46,'Can change progress',12,'change_progress'),(47,'Can delete progress',12,'delete_progress'),(48,'Can view progress',12,'view_progress');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$KsaMeAHwY1ZG$6obBWLQTlXJYBTU4L+CU1vmV6ihu/7PKU9AyAaZaEj8=','2018-11-04 16:09:13.906487',0,'yaxili','Yaxi','Li','yaxil@andrew.cmu.edu',0,1,'2018-11-04 07:22:24.593515'),(2,'pbkdf2_sha256$120000$cJcoBK4cH6Dn$eBHmVFnoSMM1EKH/h5JP+85QeGe0z+sQjF5tW1el9rY=','2018-11-04 15:26:17.613236',0,'juntaol','Juntao','Li','juntaol@andrew.cmu.edu',0,1,'2018-11-04 14:52:48.557006');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(4,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'timer','belong'),(10,'timer','group'),(11,'timer','own'),(7,'timer','parentprojects'),(12,'timer','progress'),(9,'timer','project');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-04 07:11:06.692031'),(2,'auth','0001_initial','2018-11-04 07:11:07.965488'),(3,'admin','0001_initial','2018-11-04 07:11:08.241511'),(4,'admin','0002_logentry_remove_auto_add','2018-11-04 07:11:08.252911'),(5,'admin','0003_logentry_add_action_flag_choices','2018-11-04 07:11:08.263285'),(6,'contenttypes','0002_remove_content_type_name','2018-11-04 07:11:08.454122'),(7,'auth','0002_alter_permission_name_max_length','2018-11-04 07:11:08.482843'),(8,'auth','0003_alter_user_email_max_length','2018-11-04 07:11:08.526951'),(9,'auth','0004_alter_user_username_opts','2018-11-04 07:11:08.537661'),(10,'auth','0005_alter_user_last_login_null','2018-11-04 07:11:08.623011'),(11,'auth','0006_require_contenttypes_0002','2018-11-04 07:11:08.633932'),(12,'auth','0007_alter_validators_add_error_messages','2018-11-04 07:11:08.653414'),(13,'auth','0008_alter_user_username_max_length','2018-11-04 07:11:08.681265'),(14,'auth','0009_alter_user_last_name_max_length','2018-11-04 07:11:08.715668'),(15,'sessions','0001_initial','2018-11-04 07:11:08.796799'),(16,'timer','0001_initial','2018-11-04 07:11:10.650809'),(17,'timer','0002_auto_20181104_0718','2018-11-04 07:18:18.046810'),(18,'timer','0003_auto_20181104_0800','2018-11-04 08:00:26.113246'),(19,'timer','0004_auto_20181104_0801','2018-11-04 08:02:04.341667'),(20,'timer','0005_auto_20181104_1041','2018-11-04 15:42:03.096408');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('zxxkljxd36y4eqlxh27ta9dsv4ut1s8i','Y2ZiNTg0ZjgxNTIzY2RlNDM3M2Q3M2NkOWJmYmUwYTMwMTI5M2EzODp7Il9hdXRoX3VzZXJfaGFzaCI6IjMyYjAyM2RmNGM2ZGZjNDk3M2M5MjAwZTgyOTE4YTFhMjM1YzA4NTUiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-11-18 16:09:13.919693');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_belong`
--

DROP TABLE IF EXISTS `timer_belong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_belong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupID_id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `groupID_id` (`groupID_id`),
  KEY `timer_belong_member_id_e91a2811_fk_auth_user_id` (`member_id`),
  CONSTRAINT `timer_belong_groupID_id_5dea128b_fk_timer_group_id` FOREIGN KEY (`groupID_id`) REFERENCES `timer_group` (`id`),
  CONSTRAINT `timer_belong_member_id_e91a2811_fk_auth_user_id` FOREIGN KEY (`member_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_belong`
--

LOCK TABLES `timer_belong` WRITE;
/*!40000 ALTER TABLE `timer_belong` DISABLE KEYS */;
INSERT INTO `timer_belong` VALUES (1,1,2),(2,2,1),(3,3,2),(4,4,1),(5,5,2);
/*!40000 ALTER TABLE `timer_belong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_group`
--

DROP TABLE IF EXISTS `timer_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupName` varchar(42) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_group`
--

LOCK TABLES `timer_group` WRITE;
/*!40000 ALTER TABLE `timer_group` DISABLE KEYS */;
INSERT INTO `timer_group` VALUES (1,'Group0'),(2,'Group1'),(3,'Group2'),(4,'Group3'),(5,'Group4');
/*!40000 ALTER TABLE `timer_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_own`
--

DROP TABLE IF EXISTS `timer_own`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_own` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupID_id` int(11) NOT NULL,
  `manager_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `groupID_id` (`groupID_id`),
  KEY `timer_own_manager_id_5e2d3fa3_fk_auth_user_id` (`manager_id`),
  CONSTRAINT `timer_own_groupID_id_ac9e9344_fk_timer_group_id` FOREIGN KEY (`groupID_id`) REFERENCES `timer_group` (`id`),
  CONSTRAINT `timer_own_manager_id_5e2d3fa3_fk_auth_user_id` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_own`
--

LOCK TABLES `timer_own` WRITE;
/*!40000 ALTER TABLE `timer_own` DISABLE KEYS */;
INSERT INTO `timer_own` VALUES (1,1,1),(2,2,2),(3,3,1),(4,4,2),(5,5,1);
/*!40000 ALTER TABLE `timer_own` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_parentprojects`
--

DROP TABLE IF EXISTS `timer_parentprojects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_parentprojects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_id` (`project_id`),
  KEY `timer_parentprojects_group_id_263460d8_fk_timer_group_id` (`group_id`),
  CONSTRAINT `timer_parentprojects_group_id_263460d8_fk_timer_group_id` FOREIGN KEY (`group_id`) REFERENCES `timer_group` (`id`),
  CONSTRAINT `timer_parentprojects_project_id_2dbcdf25_fk_timer_project_id` FOREIGN KEY (`project_id`) REFERENCES `timer_project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_parentprojects`
--

LOCK TABLES `timer_parentprojects` WRITE;
/*!40000 ALTER TABLE `timer_parentprojects` DISABLE KEYS */;
/*!40000 ALTER TABLE `timer_parentprojects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_progress`
--

DROP TABLE IF EXISTS `timer_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_progress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` date NOT NULL,
  `progress` double NOT NULL,
  `project_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `timer_progress_user_id_project_id_time_a101bca4_uniq` (`user_id`,`project_id`,`time`),
  KEY `timer_progress_project_id_0ae82760_fk_timer_project_id` (`project_id`),
  CONSTRAINT `timer_progress_project_id_0ae82760_fk_timer_project_id` FOREIGN KEY (`project_id`) REFERENCES `timer_project` (`id`),
  CONSTRAINT `timer_progress_user_id_67cf8eaf_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_progress`
--

LOCK TABLES `timer_progress` WRITE;
/*!40000 ALTER TABLE `timer_progress` DISABLE KEYS */;
INSERT INTO `timer_progress` VALUES (1,'2018-11-04',0.4,1,1),(2,'2018-11-04',0.6,1,2),(3,'2018-11-04',0.7,2,1),(4,'2018-11-04',0.3,2,2),(5,'2018-11-04',0.1,3,1),(6,'2018-11-04',0.9,3,2),(7,'2018-11-04',0.3,4,1),(8,'2018-11-04',0.8,4,2),(9,'2018-11-04',0.3,5,1),(10,'2018-11-04',0.1,5,2),(11,'2018-11-04',0.3,6,1),(12,'2018-11-04',0,6,2),(13,'2018-11-04',0.3,7,1),(14,'2018-11-04',0.9,7,2),(15,'2018-11-04',0.6,8,1),(16,'2018-11-04',0.6,8,2),(17,'2018-11-04',0.6,9,1),(18,'2018-11-04',0.6,9,2),(19,'2018-11-04',0.4,10,1),(20,'2018-11-04',0.2,10,2),(21,'2018-11-04',0.1,11,1),(22,'2018-11-04',0.8,11,2),(23,'2018-11-04',0.6,12,1),(24,'2018-11-04',0.8,12,2),(25,'2018-11-04',0.1,13,1),(26,'2018-11-04',0.1,13,2),(27,'2018-11-04',0,14,1),(28,'2018-11-04',0.2,14,2),(29,'2018-11-04',0.2,15,1),(30,'2018-11-04',0.6,15,2),(31,'2018-11-04',0.5,16,1),(32,'2018-11-04',0.1,16,2),(33,'2018-11-04',0.1,17,1),(34,'2018-11-04',0.5,17,2),(35,'2018-11-04',0.7,18,1),(36,'2018-11-04',0.9,18,2),(37,'2018-11-04',0.2,19,1),(38,'2018-11-04',0.5,19,2),(39,'2018-11-04',0,20,1),(40,'2018-11-04',0.6,20,2),(42,'2018-11-04',0,21,1),(43,'2018-11-04',0,21,2),(44,'2018-11-04',0,22,1),(45,'2018-11-04',0,22,2),(46,'2018-11-04',0,23,1),(47,'2018-11-04',0,23,2),(48,'2018-11-04',0,24,1),(49,'2018-11-04',0,24,2),(50,'2018-11-04',0,25,1),(51,'2018-11-04',0,25,2),(52,'2018-11-04',0,26,1),(53,'2018-11-04',0,26,2),(54,'2018-11-04',0,27,1),(55,'2018-11-04',0,27,2),(56,'2018-11-04',0,28,1),(57,'2018-11-04',0,28,2),(58,'2018-11-04',0,29,1),(59,'2018-11-04',0,29,2),(60,'2018-11-04',0,30,1),(61,'2018-11-04',0,30,2);
/*!40000 ALTER TABLE `timer_progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timer_project`
--

DROP TABLE IF EXISTS `timer_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timer_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectName` varchar(42) NOT NULL,
  `description` varchar(420) NOT NULL,
  `estimateTime` datetime(6) NOT NULL,
  `startTime` datetime(6) DEFAULT NULL,
  `finishTime` datetime(6) DEFAULT NULL,
  `priority` int(11) NOT NULL,
  `parentProject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `timer_project_parentProject_id_af5fc61b_fk_timer_project_id` (`parentProject_id`),
  CONSTRAINT `timer_project_parentProject_id_af5fc61b_fk_timer_project_id` FOREIGN KEY (`parentProject_id`) REFERENCES `timer_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timer_project`
--

LOCK TABLES `timer_project` WRITE;
/*!40000 ALTER TABLE `timer_project` DISABLE KEYS */;
INSERT INTO `timer_project` VALUES (1,'Project0','Our Demo Project0','2018-11-09 15:17:50.826561','2018-10-30 15:17:50.826561','2018-11-04 15:17:50.826561',3,NULL),(2,'Project1','Our Demo Project1','2018-11-09 15:17:50.847453','2018-10-26 15:17:50.847453',NULL,2,NULL),(3,'Project2','Our Demo Project2','2018-11-13 15:17:50.860047','2018-10-25 15:17:50.860047',NULL,4,NULL),(4,'Project3','Our Demo Project3','2018-11-12 15:17:50.872188','2018-10-26 15:17:50.872188',NULL,2,NULL),(5,'Project4','Our Demo Project4','2018-11-13 15:17:50.890358','2018-10-30 15:17:50.890358',NULL,4,NULL),(6,'Project5','Our Demo Project5','2018-11-11 15:17:50.909628','2018-10-29 15:17:50.909628','2018-11-04 15:17:50.909628',2,NULL),(7,'Project6','Our Demo Project6','2018-11-11 15:17:50.927931','2018-10-26 15:17:50.927931',NULL,5,NULL),(8,'Project7','Our Demo Project7','2018-11-13 15:17:50.946319','2018-10-27 15:17:50.946319',NULL,3,NULL),(9,'Project8','Our Demo Project8','2018-11-11 15:17:50.958391','2018-10-30 15:17:50.958391',NULL,5,NULL),(10,'Project9','Our Demo Project9','2018-11-13 15:17:50.976711','2018-10-28 15:17:50.976711',NULL,3,NULL),(11,'Project10','Our Demo Project10','2018-11-13 15:17:50.988601','2018-10-25 15:17:50.988601','2018-11-04 15:17:50.988601',5,NULL),(12,'Project11','Our Demo Project11','2018-11-14 15:17:51.001575','2018-10-30 15:17:51.001575',NULL,4,NULL),(13,'Project12','Our Demo Project12','2018-11-12 15:17:51.026929','2018-10-29 15:17:51.026929',NULL,3,NULL),(14,'Project13','Our Demo Project13','2018-11-09 15:17:51.039532','2018-10-30 15:17:51.039532',NULL,5,NULL),(15,'Project14','Our Demo Project14','2018-11-12 15:17:51.051521','2018-10-30 15:17:51.051521',NULL,4,NULL),(16,'Project15','Our Demo Project15','2018-11-11 15:17:51.063279','2018-10-25 15:17:51.063279',NULL,3,NULL),(17,'Project16','Our Demo Project16','2018-11-12 15:17:51.076793','2018-10-26 15:17:51.076793',NULL,1,NULL),(18,'Project17','Our Demo Project17','2018-11-09 15:17:51.089295','2018-10-28 15:17:51.089295',NULL,3,NULL),(19,'Project18','Our Demo Project18','2018-11-12 15:17:51.108247','2018-10-26 15:17:51.108247',NULL,4,NULL),(20,'Project19','Our Demo Project19','2018-11-11 15:17:51.125798','2018-10-30 15:17:51.125798',NULL,5,NULL),(21,'ProjectTODO0','Our Demo Project0','2018-11-26 15:25:05.259969',NULL,NULL,1,NULL),(22,'ProjectTODO1','Our Demo Project1','2018-11-28 15:25:05.275152',NULL,NULL,4,NULL),(23,'ProjectTODO2','Our Demo Project2','2018-11-28 15:25:05.287580',NULL,NULL,5,NULL),(24,'ProjectTODO3','Our Demo Project3','2018-12-01 15:25:05.312601',NULL,NULL,4,NULL),(25,'ProjectTODO4','Our Demo Project4','2018-11-29 15:25:05.327966',NULL,NULL,1,NULL),(26,'ProjectTODO5','Our Demo Project5','2018-11-29 15:25:05.340656',NULL,NULL,3,NULL),(27,'ProjectTODO6','Our Demo Project6','2018-11-30 15:25:05.352301',NULL,NULL,4,NULL),(28,'ProjectTODO7','Our Demo Project7','2018-11-29 15:25:05.364892',NULL,NULL,3,NULL),(29,'ProjectTODO8','Our Demo Project8','2018-11-28 15:25:05.377562',NULL,NULL,5,NULL),(30,'ProjectTODO9','Our Demo Project9','2018-12-01 15:25:05.401932',NULL,NULL,1,NULL);
/*!40000 ALTER TABLE `timer_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-05  0:33:53
