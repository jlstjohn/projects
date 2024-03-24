# Start using the new database
show databases;
use homeLibrary;
show tables;

# Load data into tables
select 'loading data in table Books:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_books.csv' into table Books
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Author:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_authors.csv' into table Author
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Series:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_series.csv' into table Series
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Subject:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_subject.csv' into table Subject
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Person:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_person.csv' into table Person
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Wrote:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_wrote.csv' into table Wrote
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table partOf:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_partOf.csv' into table partOf
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table isAbout:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_isAbout.csv' into table isAbout
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table timesRead:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_read.csv' into table timesRead
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'loading data in table Loaned:' as '';
load data local infile 'C:/Users/farrj/Documents/Scripts/COMP3421/Database Project Resources/data_loaned.csv' into table Loaned
  fields terminated by ','
  lines terminated by '\n'
  ;

select 'show tables after data loading:' as '';
show tables;

select 'describing table name for each table' as '';
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

select 'running count(*) on Books' as '';
select count(*) from Books;

select 'running count(*) on Author' as '';
select count(*) from Author;

select 'running count(*) on Series' as '';
select count(*) from Series;

select 'running count(*) on Subject' as '';
select count(*) from Subject;

select 'running count(*) on Person' as '';
select count(*) from Person;

select 'running count(*) on Wrote' as '';
select count(*) from Wrote;

select 'running count(*) on partOf' as '';
select count(*) from partOf;

select 'running count(*) on isAbout' as '';
select count(*) from isAbout;

select 'running count(*) on timesRead' as '';
select count(*) from timesRead;

select 'running count(*) on Loaned' as '';
select count(*) from Loaned;


select 'running 10 select commands that will return <10 tuples' as '';
