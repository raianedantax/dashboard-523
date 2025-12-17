CREATE DATABASE  IF NOT EXISTS `dashboard` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dashboard`;
-- MySQL dump 10.13  Distrib 8.0.43, for macos15 (arm64)
--
-- Host: 127.0.0.1    Database: dashboard
-- ------------------------------------------------------
-- Server version	9.4.0

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
-- Table structure for table `aluno`
--

DROP TABLE IF EXISTS `aluno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno` (
  `matricula` varchar(20) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matricula`),
  UNIQUE KEY `Matricula_UNIQUE` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `aluno_turma`
--

DROP TABLE IF EXISTS `aluno_turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aluno_turma` (
  `aluno_matricula` varchar(20) NOT NULL,
  `turma_id` varchar(3) NOT NULL,
  `turma_ano` int NOT NULL,
  PRIMARY KEY (`aluno_matricula`,`turma_id`,`turma_ano`),
  KEY `fk_aluno_has_turma_aluno_idx` (`aluno_matricula`),
  KEY `fk_aluno_turma_turma1_idx` (`turma_id`,`turma_ano`),
  CONSTRAINT `fk_aluno_has_turma_aluno` FOREIGN KEY (`aluno_matricula`) REFERENCES `aluno` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `area_do_conhecimento`
--

DROP TABLE IF EXISTS `area_do_conhecimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area_do_conhecimento` (
  `id` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `boletim`
--

DROP TABLE IF EXISTS `boletim`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boletim` (
  `aluno_matricula` varchar(20) NOT NULL,
  `disciplina_id` int NOT NULL,
  `turma_id` varchar(3) NOT NULL,
  `turma_ano` int NOT NULL,
  `bimestre1` decimal(4,2) DEFAULT NULL,
  `bimestre2` decimal(4,2) DEFAULT NULL,
  `recusem1` decimal(4,2) DEFAULT NULL,
  `bimestre3` decimal(4,2) DEFAULT NULL,
  `bimestre4` decimal(4,2) DEFAULT NULL,
  `recusem2` decimal(4,2) DEFAULT NULL,
  `recfinal` decimal(4,2) DEFAULT NULL,
  `final` decimal(4,2) DEFAULT NULL,
  `faltas` int DEFAULT NULL,
  `faltaspercent` int DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`aluno_matricula`,`disciplina_id`,`turma_id`,`turma_ano`),
  KEY `fk_boletim_aluno1_idx` (`aluno_matricula`),
  KEY `fk_boletim_disciplina1_idx` (`disciplina_id`),
  KEY `fk_boletim_turma1_idx` (`turma_id`,`turma_ano`),
  CONSTRAINT `fk_boletim_aluno1` FOREIGN KEY (`aluno_matricula`) REFERENCES `aluno` (`matricula`),
  CONSTRAINT `fk_boletim_disciplina1` FOREIGN KEY (`disciplina_id`) REFERENCES `disciplina` (`id`),
  CONSTRAINT `fk_boletim_turma1` FOREIGN KEY (`turma_id`, `turma_ano`) REFERENCES `turma` (`id`, `ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `id` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `id` int NOT NULL,
  `sigla` varchar(15) NOT NULL,
  `descricao` varchar(45) NOT NULL,
  `horas` int DEFAULT NULL,
  `area_do_conhecimento_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`),
  UNIQUE KEY `sigla_UNIQUE` (`sigla`),
  KEY `fk_disciplina_area_do_conhecimento1_idx` (`area_do_conhecimento_id`),
  CONSTRAINT `fk_disciplina_area_do_conhecimento1` FOREIGN KEY (`area_do_conhecimento_id`) REFERENCES `area_do_conhecimento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `disciplina_curso_serie`
--

DROP TABLE IF EXISTS `disciplina_curso_serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina_curso_serie` (
  `disciplina_id` int NOT NULL,
  `curso_id` int NOT NULL,
  `serie_id` int NOT NULL,
  PRIMARY KEY (`disciplina_id`,`curso_id`,`serie_id`),
  KEY `fk_disciplina_has_curso_curso1_idx` (`curso_id`),
  KEY `fk_disciplina_has_curso_disciplina1_idx` (`disciplina_id`),
  KEY `fk_disciplina_has_curso_serie1_idx` (`serie_id`),
  CONSTRAINT `fk_disciplina_has_curso_curso1` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`),
  CONSTRAINT `fk_disciplina_has_curso_disciplina1` FOREIGN KEY (`disciplina_id`) REFERENCES `disciplina` (`id`),
  CONSTRAINT `fk_disciplina_has_curso_serie1` FOREIGN KEY (`serie_id`) REFERENCES `serie` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `serie`
--

DROP TABLE IF EXISTS `serie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `serie` (
  `id` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `turma`
--

DROP TABLE IF EXISTS `turma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turma` (
  `id` varchar(3) NOT NULL,
  `ano` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  `curso_id` int NOT NULL,
  `serie_id` int NOT NULL,
  `turma_id` varchar(3) DEFAULT NULL,
  `turma_ano` int DEFAULT NULL,
  `turno_id` int NOT NULL,
  PRIMARY KEY (`id`,`ano`),
  KEY `fk_turma_curso1_idx` (`curso_id`),
  KEY `fk_turma_serie1_idx` (`serie_id`),
  KEY `fk_turma_turma1_idx` (`turma_id`,`turma_ano`),
  KEY `fk_turma_turno1_idx` (`turno_id`),
  CONSTRAINT `fk_turma_curso1` FOREIGN KEY (`curso_id`) REFERENCES `curso` (`id`),
  CONSTRAINT `fk_turma_serie1` FOREIGN KEY (`serie_id`) REFERENCES `serie` (`id`),
  CONSTRAINT `fk_turma_turno1` FOREIGN KEY (`turno_id`) REFERENCES `turno` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `turno`
--

DROP TABLE IF EXISTS `turno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turno` (
  `id` int NOT NULL,
  `descricao` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `descricao_UNIQUE` (`descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-11 10:57:25
