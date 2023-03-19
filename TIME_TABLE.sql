create database TimeTable;
use TimeTable;

drop database TimeTable;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


-- Create the Admin table
CREATE TABLE Admin (
  admin_id VARCHAR(30) PRIMARY KEY,
  username VARCHAR(50) ,
  password VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



INSERT INTO `Admin` (`admin_id`,`username`, `password`) VALUES
('ADCSE01','admin', 'pass123');

drop table Program;
-- Create the Program table
CREATE TABLE Program (
    Program_name VARCHAR(50) PRIMARY KEY
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `Program`(`Program_name`) VALUES
('BTECH'),
('BBA'),
('BAJMC');

-- Create the Semester table
CREATE TABLE Semester (
  semester_id INT PRIMARY KEY
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Semester`(`semester_id`) VALUES
('1'),
('2'),
('3'),
('4'),
('5'),
('6');

drop table Courses;

-- Create the Courses table
CREATE TABLE Courses (
  course_code varchar(50) PRIMARY KEY,
  course_name VARCHAR(100),
  frequency INT,
  Program_name VARCHAR(100),
  semester_id INT,
  FOREIGN KEY (semester_id) REFERENCES Semester(semester_id),
  FOREIGN KEY (Program_name) REFERENCES Program(Program_name)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Courses` (`course_code`,`course_name`,`frequency`, `Program_name`, `semester_id`) VALUES
('ECSE105L','Computational Thinking and Programming',3,'Btech',1),
('EMAT101L','Engineering Calculus',3,'Btech',1),
('EHSS103L','New Age Life Skills',2,'Btech', 1),
('EECE105L','Fundamentals of Electrical and Electronics Engineering',1,'Btech',2),
('CSET104','Object Oriented Programming using Java',3,'Btech','2'),
('CSET105','Digital Design',2,'Btech','2'),
('ECSE219L','Statistical Machine Learning',2,'Btech','3'),
('ECSE215L','Data Structures using C++',3,'Btech','3'),
('ECSE217L','Microprocessors and Computer Architecture',2,'Btech','3'),
('CSET207','Computer Networks',3,'Btech','4'),
('CSET210','Design Thinking & Innovation',3,'Btech','4');


-- Create the Teachers table
CREATE TABLE Professor (
  Professor_id VARCHAR(50) PRIMARY KEY,
  Professor_name VARCHAR(200),
  course_code VARCHAR(50),
  Phone_number INT,
  Email_ID VARCHAR(200),
  FOREIGN KEY (course_code) REFERENCES Courses(course_code)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Professor` (`Professor_id`,`Professor_name`, `course_code`, Phone_number, `Email_ID`) VALUES
('T016', 'Prof. Shamshad Husain', 'CSET210', 12345678, 'shamshadhusain@gmail.com'),
('T015', 'Dr. Faisal Talib', 'EECE105L', 12345678, 'faisaltalib@gmail.com'),
('T014', 'Dr. Mohd. Sharique', 'ECSE215L', 12345678, 'mohdsharique@gmail.com'),
('T013', 'Mr. Faisal Alam', 'ECSE217L', 12345678, 'faisalalam@gmail.com'),
('T011', 'Mr. Asad Mohammed Khan', 'EECE105L', 12345678, 'asadmohammedkhan@gmail.com'),
('T012', 'Mr. Muneeb Hasan Khan', 'CSET207', 12345678, 'muneebhasankhan@gmail.com'),
('T007', 'Mr. Misbahur Rahman Warsi', 'EECE105L', 12345678, 'mrwarsi@gmail.com'),
('T008', 'Mr. Izharauddin', 'CSET104', 12345678, 'izharuddin@gmail.com'),
('T009', 'Mr. Tameem Ahmad', 'ECSE215L', 12345678, 'tameemahmad@gmail.com'),
('T010', 'Mr. Nadeem Akhtar', 'ECSE219L', 12345678, 'nadeemakhtar@gmail.com'),
('T006', 'Dr. Saiful Islam', 'CSET210', 12345678, 'saifulislam@gmail.com'),
('T005', 'Dr. Rashid Ali', 'ECSE217L', 12345678, 'rashidali@gmail.com'),
('T004', 'Prof. M.M. Sufyan Beg', 'EECE105L', 12345678, 'mmsufyanbeg@gmail.com'),
('T002', 'Prof. Nesar Ahmad', 'CSET104', 12345678, 'nesarahmad@gmail.com'),
('T003', 'Prof. Ash Mohammad Abbas', 'ECSE215L', 12345678, 'ashmabbas@gmail.com'),
('T001', 'Prof. Mohammad Sarosh Umar', 'ECSE219L', 12345678, 'saroshumar@gmail.com');

SELECT DISTINCT Courses.course_code, Courses.course_name, Professor.Professor_id, Professor.Professor_name
FROM Courses
INNER JOIN Professor ON Courses.course_code = Professor.course_code;


-- Create the LAB table
CREATE TABLE Labs (
  Lab_id VARCHAR(10) PRIMARY KEY,
  Lab_capacity INT
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Labs`(`Lab_id`,`Lab_capacity`) VALUES
('201-B-LA','30'),
('103-B-LA','30'),
('105-B-LA','30'),
('302-N-LA','25'),
('209-N-LA','25'),
('212-A-LA','30'),
('310-A-LA','30'),
('211-B-LA','30'),
('111-B-LA','30'),
('311-B-LA','30'),
('112-N-LA','25'),
('304-A-LA','30');


-- Create the Lecture table
CREATE TABLE Lecture (
  lecture_id INT PRIMARY KEY,
  lecture_capacity INT
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Lecture`(`lecture_id`,`lecture_capacity`) VALUES
('101-N-LH','150'),
('103-B-LH','200'),
('102-B-LH','90'),
('302-N-LH','100'),
('201-N-LH','150'),
('205-A-LH','200'),
('308-A-LH','120'),
('204-B-LH','60'),
('301-B-LH','60'),
('101-B-LH','90'),
('102-N-LH','150'),
('304-A-LH','90');
