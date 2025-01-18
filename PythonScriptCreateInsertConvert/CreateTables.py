from dotenv import load_dotenv
import os
import mysql.connector

# prints out all databases on the MySQL
def ShowAllDB(mydb):
  cursor = mydb.cursor()
  cursor.execute("SHOW DATABASES")
  for x in cursor:
    print(x)
  return

def CreateTables(mydb):
  cursor = mydb.cursor()
  try:
    cursor.execute(
      "CREATE TABLE CarType ("
      "CarTypeID INT AUTO_INCREMENT PRIMARY KEY,"
      "CarClass TINYINT,"
      "CarFrame TINYINT,"
      "CabinSize TINYINT,"
      "Engine TINYINT,"
      "DriveTrain TINYINT,"
      "Trim TINYINT,"
      "DailyCost NUMERIC(9, 2),"
      "WeeklyCost NUMERIC(9, 2),"
      "MonthlyCost NUMERIC(9, 2))")
    print("CarType table created successfully")
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  try:
    cursor.execute(
      "CREATE TABLE CarMISC ("
      "CarVIN VARCHAR(17) PRIMARY KEY, "
      "CarTypeID INT, "
      "Brand SMALLINT, "
      "ModelName INT, "
      "YearMade SMALLINT, "
      "Color TINYINT, "
      "Mileage INT, "
      "LastTuneUp DATE, "
      "BranchID SMALLINT, "
      "CarInCycle TINYINT, "
      "FOREIGN KEY (CarTypeID) REFERENCES CarType(CarTypeID)"
      ")"
    )
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  try:
    cursor.execute(
      "CREATE TABLE BranchTable ("
      "BranchID SMALLINT PRIMARY KEY, "
      "BranchName VARCHAR(50), "
      "AreaCode SMALLINT, "
      "ContactNumber MEDIUMINT, "
      "Street VARCHAR(100), "
      "PostalCode CHAR(6), "
      "City MEDIUMINT, "
      "Province SMALLINT, "
      "Country TINYINT"
      ")"
    )
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  try:
    cursor.execute(
      "CREATE TABLE EmployeeTable ("
      "EmployeeID INT PRIMARY KEY, "
      "BranchID SMALLINT, "
      "OperatorID BIGINT, "
      "FirstName VARCHAR(50), "
      "LastName VARCHAR(50), "
      "Street VARCHAR(100), "
      "PostalCode CHAR(6), "
      "DOB DATE, "
      "AreaCode SMALLINT, "
      "ContactNumber MEDIUMINT, "
      "Password VARCHAR(64), "
      "Active BIT, "
      "FOREIGN KEY (BranchID) REFERENCES BranchTable(BranchID)"
      ")"
    )
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  try:
    cursor.execute(
      "CREATE TABLE CustomerTable ("
      "CustomerID INT PRIMARY KEY, "
      "OperatorID BIGINT, "
      "FirstName VARCHAR(50), "
      "LastName VARCHAR(50), "
      "Street VARCHAR(100), "
      "PostalCode CHAR(6), "
      "DOB DATE, "
      "AreaCode SMALLINT, "
      "ContactNumber MEDIUMINT, "
      "Password VARCHAR(64)"
      ")"
    )
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  try:
    cursor.execute(
      "CREATE TABLE RentalTransactions ("
      "TransactionID INT PRIMARY KEY, "
      "RentalCost NUMERIC(9, 2), "
      "RentedFrom DATE, "
      "RentedTo DATE, "
      "EmployeeID INT, "
      "CustomerID INT, "
      "CarVIN VARCHAR(17), "
      "BranchPickUp SMALLINT, "
      "BranchDropOff SMALLINT, "
      "FOREIGN KEY (EmployeeID) REFERENCES EmployeeTable(EmployeeID), "
      "FOREIGN KEY (CustomerID) REFERENCES CustomerTable(CustomerID), "
      "FOREIGN KEY (CarVIN) REFERENCES CarMISC(CarVIN), "
      "FOREIGN KEY (BranchPickUp) REFERENCES BranchTable(BranchID), "
      "FOREIGN KEY (BranchDropOff) REFERENCES BranchTable(BranchID)"
      ")"
    )
  except mysql.connector.Error as err:
    print(f"Error: {err}")

  return

def CreateDatabase(mydb, database_name):
  cursor = mydb.cursor()
  try:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database '{database_name}' checked/created successfully.")
  except mysql.connector.Error as err:
    print(f"Error: {err}")
  cursor.close()

  return