import mysql.connector #Using connector/python provided by oracle
from mysql.connector import errorcode

DB_NAME = 'BIRDWATCHDBV1'#database for storing the tables from various websites
DB_PORT = '3306'
TABLES = {}#Dictionary for storing create table instruction for each table, carwale already exists
# TABLES['CARWALE'] = (
#     "CREATE TABLE `CARWALE` ("
#     "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
#     "  `YEAR` int(4) NOT NULL,"
#     "  `MAKE` varchar(200) NOT NULL,"
#     "  `MODEL` varchar(200) NOT NULL,"
#     "  `TRIM` varchar(200) NOT NULL,"
#     "  `CITY` varchar(200),"
#     "  `PRICE` varchar(200) NOT NULL,"
#     "  PRIMARY KEY (`CAR_ID`)"
#     ") ENGINE=InnoDB")
'''
TABLES['IBB_Sell'] = (
    "CREATE TABLE `IBB_Sell` ("
    "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `YEAR` int(4) NOT NULL"
    "  `MAKE` varchar(16) NOT NULL,"
    "  `MODEL` varchar(16) NOT NULL,"
    "  `TRIM` varchar(16) ,NOT NULL"
    "  `KMS` int(5),"
    "  `PRICE` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`CAR_ID`)"
    ") ENGINE=InnoDB")

TABLES['IBB_Buy'] = (
    "CREATE TABLE `IBB_Sell` ("
    "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `YEAR` int(4) NOT NULL"
    "  `MAKE` varchar(16) NOT NULL,"
    "  `MODEL` varchar(16) NOT NULL,"
    "  `TRIM` varchar(16) ,NOT NULL"
    "  `KMS` int(5),"
    "  `PRICE` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`CAR_ID`)"
    ") ENGINE=InnoDB")
'''
TABLES['VARS'] = (
    "CREATE TABLE `VARS` ("
    "  `VAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `VAR_NAME` varchar(200) NOT NULL,"
    "  `VAR_VAL` int(10) NOT NULL,"
    "  PRIMARY KEY (`VAR_ID`)"
    ") ENGINE=InnoDB")
'''
TABLES['CARDEKHO'] = (
    "CREATE TABLE `CARDEKHO` ("
    "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `YEAR` int(4) NOT NULL"
    "  `MAKE and MODEL` varchar(16) NOT NULL,"
    "  `TRIM` varchar(16) NOT NULL,"
    "  `PRICE` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`CAR_ID`)"
    ") ENGINE=InnoDB")

TABLES['CARS24'] = (
    "CREATE TABLE `CARS24` ("
    "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `MAKE` varchar(16) NOT NULL,"
    "  `MODEL` varchar(16) NOT NULL,"
    "  `YEAR` int(4) NOT NULL"
    "  `TRIM` varchar(16) ,NOT NULL"
    "  `STATE` varchar(16),"
    "  `KMS` int(5),"
    "  `PRICE` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`CAR_ID`)"
    ") ENGINE=InnoDB")

TABLES['ZIGWHEELS_BUY'] = (
    "CREATE TABLE `CARS24` ("
    "  `CAR_ID` int(10) NOT NULL AUTO_INCREMENT,"
    "  `MAKE` varchar(16) NOT NULL,"
    "  `MODEL` varchar(16) NOT NULL,"
    "  `TRIM` varchar(16) ,NOT NULL"
    "  `YEAR` int(4) NOT NULL"
    "  `KMS` int(5),"
    "  `OWNERSHIP` int(2) NOT NULL,"

    "  `STATE` varchar(16),"
    "  `PRICE` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`CAR_ID`)"
    ") ENGINE=InnoDB")'''

cnx = mysql.connector.connect(user='root',password='toor',host='localhost', port = DB_PORT, database='TESTDB')#These are default settings
#cnx is a connection object, cursor used for executing SQL instructions
cursor = cnx.cursor()
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))#DB_NAME is global variable
        #makes it easier to switch between databases
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
#obtaining the handle to it, using database property of cnx obj, if it doesn't exist, create it by calling above function   
# create_database(cursor)
# cnx.database = DB_NAME
try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
#Now iterate over TABLES dictionary and create create tables
for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ")
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
