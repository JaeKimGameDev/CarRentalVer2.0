import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
MYSQLpassword = os.getenv("MYSQLpassword")
database_name = os.getenv("DatabaseName")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=MYSQLpassword,
    database=database_name
)
cursor = mydb.cursor()

def insertCarTypeData(car_type_id, car_type, car_frame, cabin_size, engine, drivetrain, trim, daily_cost, weekly_cost, monthly_cost):
    try:
        mySql_insert_query = ("INSERT INTO CarType "
                              "(CarTypeID, CarType, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
                                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (car_type_id, car_type, car_frame, cabin_size, engine, drivetrain, trim, daily_cost, weekly_cost, monthly_cost)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertManyCarTypeData(many_cars):
    try:
        mySql_insert_query = ("INSERT INTO CarType "
                              "(CarTypeID, CarType, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        cursor.executemany(mySql_insert_query, many_cars)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertCarData(car_vin, car_type_id, brand, model_name, year_made, color, mileage, last_tune_up, branch_id, car_in_cycle):
    try:
        mySql_insert_query = ("INSERT INTO Car "
                              "(CarVIN, CarTypeID, Brand, ModelName, YearMade, Color, Mileage, LastTuneUp, BranchID, CarInCycle) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (car_vin, car_type_id, brand, model_name, year_made, color, mileage, last_tune_up, branch_id, car_in_cycle)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertBranchData(branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country):
    try:
        mySql_insert_query = ("INSERT INTO Branch "
                              "(BranchID, BranchName, AreaCode, ContactNumber, Street, PostalCode, City, Province, Country) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertEmployeeData(employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password):
    try:
        mySql_insert_query = ("INSERT INTO Employee "
                              "(EmployeeID, BranchID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password) " 
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertCustomerData(customer_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password):
    try:
        mySql_insert_query = ("INSERT INTO Customer "
                              "(CustomerID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (customer_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def insertRentalTransactionData(transaction_id, rental_cost, rented_from, rented_to, employee_id, customer_id, car_vin, branch_pickup, branch_dropoff):
    try:
        mySql_insert_query = ("INSERT INTO RentalTransaction "
                              "(TransactionID, RentalCost, RentedFrom, RentedTo, EmployeeID, CustomerID, CarVIN, BranchPickUp, BranchDropOff) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (transaction_id, rental_cost, rented_from, rented_to, employee_id, customer_id, car_vin, branch_pickup, branch_dropoff)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    return

def createDataForCarType():
    car_type_id = 0
    daily_cost = 10
    weekly_cost = 60
    monthly_cost = 200

    #insertCarTypeData(car_type_id, car_type, car_frame, cabin_size, engine, drivetrain, trim, daily_cost, weekly_cost, monthly_cost)
    for i in range(7):
        car_type = i
        for k in range(8):
            car_frame = k
            for t in range(3):
                cabin_size = t
                for y in range(3):
                    engine = y
                    for u in range(3):
                        drivetrain = u
                        for o in range(3):
                            trim = o
                            insertCarTypeData(car_type_id, car_type, car_frame, cabin_size, engine, drivetrain, trim,
                                              daily_cost, weekly_cost, monthly_cost)
                            car_type_id += 1
    return

def main():
    createDataForCarType()

    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")

    return

if __name__ == "__main__":
    main()