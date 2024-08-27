import random

import IdentifyData

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv, dotenv_values
import pandas as pd

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

def insertEmployeeData(employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password, active):
    try:
        mySql_insert_query = ("INSERT INTO Employee "
                              "(EmployeeID, BranchID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password, Active) " 
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ")

        record = (employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password, active)
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
                    for u in range(4):
                        drivetrain = u
                        for o in range(3):
                            trim = o
                            insertCarTypeData(car_type_id, car_type, car_frame, cabin_size, engine, drivetrain, trim,
                                              daily_cost, weekly_cost, monthly_cost)
                            car_type_id += 1
    return

def createDataForBranch():
    branch_id=0
    first_half_branch_name="USA branch name test "
    second_half_branch_name=0
    area_code = 100
    contact_number = 1000000
    street="Somewhere in USA"
    # 5 digit zip code
    zip_code = "zfive"
    #700 cities
    city = 0
    # 50 states
    state=0
    country=0
    for i in range(5000):
        branch_name = first_half_branch_name + str(second_half_branch_name)
        insertBranchData(branch_id, branch_name, area_code, contact_number, street, zip_code, city, state, country)
        branch_id += 1
        contact_number += 1
        city+=1
        if (city > 700):
            city=0
        state+=1
        if (state > 50):
            state=0
        second_half_branch_name+=1

    # start Canada at 10,000 for USA branches to keep adding onto the tail end, adding consistency
    branch_id = 10000
    first_half_branch_name="CANADA branch name test "
    second_half_branch_name=0
    area_code = 200
    contact_number = 2000000
    street="Somewhere in CANADA"
    # Postal Code
    postal_code = "T1T1T1"
    # 100 cities
    city = 1000
    # 10 Provinces
    province=100
    country=1
    for k in range(3000):
        branch_name = first_half_branch_name + str(second_half_branch_name)
        insertBranchData(branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country)
        branch_id += 1
        contact_number += 1
        city+=1
        if (city > 1100):
            city=1000
        province+=1
        if (province > 109):
            province=100
        second_half_branch_name+=1

    return

def createDataForEmployee():
    # insertEmployeeData(employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code,
    #                    contact_number, password, active):
    employee_id=0
    branch_id=0
    operator_id = 20000000
    street="Some street for customer"
    postal_code="T1T1T1"
    #YYYY-MM-DD
    # range days up to 28, months to 12, years from 1960
    day=0
    month=1
    year=1959
    area_code=200
    contact_number=5000000
    for i in range(1000):
        operator_id+=1
        first_name="first_name " + str(i)
        last_name="last_name " + str(i)
        password="password " + str(i)
        day+=1
        if (day > 28):
            month+=1
            day=1
            if (month > 12):
                month=1
                year+=1
        dob = str(year) + "-" + str(month) + "-" + str(day)
        contact_number+=1

        insertEmployeeData(employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password, 1)
        employee_id+=1
        branch_id+=1
        if (branch_id > 4999):
            branch_id=0

    return

def createDataForCustomer():
    customer_id=0
    operator_id=10000000
    street="Some street for customer"
    postal_code="T1T1T1"
    #YYYY-MM-DD
    # range days up to 28, months to 12, years from 1960
    day=0
    month=1
    year=1959
    area_code=200
    contact_number=4000000
    for i in range(4000):
        operator_id+=1
        first_name="first_name " + str(i)
        last_name="last_name " + str(i)
        password="password " + str(i)
        day+=1
        if (day > 28):
            month+=1
            day=1
            if (month > 12):
                month=1
                year+=1
        dob = str(year) + "-" + str(month) + "-" + str(day)
        contact_number+=1

        insertCustomerData(customer_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password)
        customer_id+=1

    return

def createDataForCar():
    for k in range(5000):
        CarVIN = []
        CarVIN.append(str(random.randint(0, 9)))
        for i in range(4):
            CarVIN.append(chr(65 + random.randint(0, 25)))
        for i in range(2):
            CarVIN.append(str(random.randint(0, 9)))
        for i in range(4):
            CarVIN.append(chr(65 + random.randint(0, 25)))
        for i in range(6):
            CarVIN.append(str(random.randint(0, 9)))
        CarVIN = ''.join(CarVIN)

        insertCarData(CarVIN, 37, 9, 9001, 2024, 4, 6000, 5000, k, 1)

    return

def main():
    #createDataForCarType()
    #createDataForBranch()
    #createDataForEmployee()
    #createDataForCustomer()
    #createDataForCar()
    #identify_model()
    #print(IdentifyData.identify_color(1))
    
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")

    return

if __name__ == "__main__":
    main()