# Create a new database, but drop it if it already exists
drop database if exists homeLibrary;
create database homeLibrary;
show databases;

# Start using the new database
use homeLibrary;

# See which database we are using
select 'running statement "select database":' as ' ';
select database();

# Create new tables(relations) for database, but drop them first if they already exist.
select 'running 10 checks for existing tables/relations:' as ' ';
drop table if exists Books;
drop table if exists Author;
drop table if exists Series;
drop table if exists Subject;
drop table if exists Person;
drop table if exists Wrote;
drop table if exists partOf;
drop table if exists isAbout;
drop table if exists timesRead;
drop table if exists Loaned;

select 'creating 10 tables/relations:' as ' ';

create table Books(
  isbn varchar(20),
  title varchar(30) NOT NULL,
  pages int,
  Primary Key(isbn)
);

create table Author(
  name varchar(20),
  Primary Key(name)
);

create table Series(
  name varchar(20),
  summary varchar(140) NOT NULL,
  placement int,
  outOf int,
  Primary Key(name)
);

create table Subject(
  subject varchar(20),
  summary varchar(140) NOT NULL,
  Primary Key(subject)
);

create table Person(
  name varchar(20),
  dateOut DATE,
  dateReturned DATE,
  Primary Key(name)
);

create table Wrote(
  isbn varchar(20),
  name varchar(20),
  Primary Key(isbn, name)
);

create table partOf(
  isbn varchar(20),
  name varchar(20),
  Primary Key(isbn, name)
);

create table isAbout(
  isbn varchar(20),
  subject varchar(20),
  Primary Key(isbn, subject)
);

create table timesRead(
  isbn varchar(20),
  timesRead int,
  rating int,
  Primary Key(isbn)
);

create table Loaned(
  isbn varchar(20),
  name varchar(20),
  Primary Key(isbn, name)
);

# Check descriptions for all tables
select 'running "describe Foo" for 10 tables/relations' as ' ';
describe Books;
describe Author;
describe Series;
describe Subject;
describe Person;
describe Wrote;
describe partOf;
describe isAbout;
describe timesRead;
describe Loaned;

# Execute three insert commands into one of the relations
select 'running 3 inserts on Books table:' as ' ';
insert into Books values("978-0-345-54505-3", "Dawn of the Jedi", 317);
insert into Books values("978-0-345-51135-5", "Revan", 343);
insert into Books values("978-0-345-80678-9", "The Shining", 659);

select * from Books;
