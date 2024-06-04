# import the mysql connector to help connect with the 
# mysql server
import mysql.connector

# create the name and email variables to receive the user input
name = input("Please enter your name :")
email = input("Please enter your email : ")

# create the object to connect with the mysql db
# give the connect attributes for the created user (username , and password)
# the name of the database created
# this is as well  a configuration for the information of the database
mydb = mysql.connector.connect(
 host = "localhost",
 user = "musa",
 password = "P@ssW0rd1234",
 database = "staff"
)

# this allows insertion of data into the database
mycursor = mydb.cursor()

# this is the Mysql query to insert into the table created above
sql = "insert into editorial (name, email) values (%s , %s)"

# this defines the columns for the database
val = (name , email)

# create the cursor instance to help execute the above sql statements
mycursor.execute(sql,val)

# this confirms the changes made by the mycursor.execute
mydb.commit()

# indicates the success or failure 
print(mycursor.rowcount,"record inserted.")
