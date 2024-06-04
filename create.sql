-- create the database
create DATABASE staff;

-- create another user and give it a secure password
create user 'musa'@'localhost' identified by 'P@ssW0rd1234';

-- give permissions to the created user
grant all privileges on staff.* to 'musa'@'localhost';

-- use the created database
use staff;

-- create the table to store the user information
create table editorial(id int(3) auto_increment primary key, name varchar(30) , email varchar(30));

