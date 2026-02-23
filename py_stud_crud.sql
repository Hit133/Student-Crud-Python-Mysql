create database student_db;
use student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks INT
);
insert into students(name,age,course,marks) values("Tanush",20,"BCA",90);
select * from students;

select * from students;

show tables;