# Procedure description: Procedure to return number of books written by a specific author.

# I am not sure what was going on here. I worked for several hours and seemed to have a heck of a time
# getting MySQL to work with having an IN and an OUT variable. (I think the first error below was a typo on my end).
# But I could not get it to work with having both an input and output variables. I searched for troubleshooting tips online and
# did not find anything useful. Often when I would recode for having just the output variable, MySQL would then tell me that
# the procedure already existed.

# select correct database
use homelibrary;

-- delimiter //
-- create procedure proc_booksinOUT(IN inName varchar, OUT bookCount INT)
-- begin
--   select count(title) INTO bookCount
--   from books b, author a
--   where b.isbn = a.isbn and a.name = inName;
-- end //
-- delimiter;
--
-- set @theNum = 0;
-- set @varName = 'Adam Kay';
-- call proc_inOut(@varName, @theNum);
-- select @theNum as 'num books';

-- Output from command line from running above:
-- ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', OUT bookCount INT)
-- begin
--   select count(title) INTO bookCount
--   from books b, ' at line 1
-- ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'delimiter;
-- set @theNum = 0;
-- set @varName = 'Adam Kay';
-- call proc_inOut(@varName,' at line 1
-- mysql> source C:\Users\farrj\Documents\Scripts\COMP3421\Week07\Assign07Proc.sql
-- Query OK, 0 rows affected (0.00 sec)

delimiter //
create procedure proc_bookCount(IN inName varchar, OUT bookCount INT)
begin
  select count(title) INTO bookCount
  from books b, wrote w
  where b.isbn = w.isbn and w.name = inName;
end //
delimiter ;

-- set @theNum = 0;
-- set @theName = 'Adam Kay';
-- call proc_bookCount(@theName, @theNum);
-- select @theNum as 'num books';

-- Output from command line from running above:
--
-- ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ', OUT bookCount INT)
-- begin
--   select count(title) INTO bookCount
--   from books b, ' at line 1
-- Query OK, 0 rows affected (0.00 sec)

delimiter //
create procedure proc_bookCount(OUT bookCount INT)
begin
  select count(*) INTO bookCount
  from wrote w
  where w.name = 'Adam Kay';
end //
delimiter ;
