create database TimeTable;
use TimeTable;
drop database TimeTable;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Create the Admin table
CREATE TABLE Admin (
  admin_id INT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Year table
CREATE TABLE Year (
  year_id INT PRIMARY KEY,
  year_name VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Semester table
CREATE TABLE Semester (
  semester_id INT PRIMARY KEY,
  semester_name VARCHAR(50),
  year_id INT,
  FOREIGN KEY (year_id) REFERENCES Year(year_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Batch table
CREATE TABLE Batch (
  batch_id INT PRIMARY KEY,
  batch_name VARCHAR(50),
  semester_id INT,
  FOREIGN KEY (semester_id) REFERENCES Semester(semester_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Group table
CREATE TABLE BatchGroup (
  group_id INT PRIMARY KEY,
  group_name VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the GroupBatch table
CREATE TABLE GroupBatch (
  group_id INT,
  batch_id INT,
  PRIMARY KEY (group_id, batch_id),
  FOREIGN KEY (group_id) REFERENCES BatchGroup(group_id),
  FOREIGN KEY (batch_id) REFERENCES Batch(batch_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Courses table
CREATE TABLE Courses (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(50),
  course_code VARCHAR(50),
  credit_hours INT
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Teachers table
CREATE TABLE Teachers (
  teacher_id INT PRIMARY KEY,
  teacher_name VARCHAR(50),
  subject VARCHAR(50)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- Create the Classes table
CREATE TABLE Classes (
  class_id INT PRIMARY KEY,
  class_name VARCHAR(50),
  subject VARCHAR(50),
  duration INT,
  teacher_id INT,
  batch_id INT,
  course_id INT,
  FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
  FOREIGN KEY (batch_id) REFERENCES Batch(batch_id),
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Rooms table
CREATE TABLE Rooms (
  room_id INT PRIMARY KEY,
  room_name VARCHAR(50),
  capacity INT
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create the Schedule table
CREATE TABLE Schedule (
  schedule_id INT PRIMARY KEY,
  class_id INT,
  teacher_id INT,
  room_id INT,
  start_time DATETIME,
  end_time DATETIME,
  FOREIGN KEY (class_id) REFERENCES Classes(class_id),
  FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
  FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


