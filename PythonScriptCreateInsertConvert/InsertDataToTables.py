from dotenv import load_dotenv
import os
import mysql.connector
import random

def insertCarTypeData(cursor, mydb, car_type_id, car_class, car_frame, cabin_size, engine, drivetrain, trim, daily_cost, weekly_cost, monthly_cost):
    try:
        mySql_insert_query = ("INSERT INTO CarType "
                              "(CarTypeID, CarClass, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (car_type_id, car_class, car_frame, cabin_size, engine, drivetrain, trim, daily_cost, weekly_cost, monthly_cost)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Record {car_type_id} inserted successfully into CarType table")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into CarType table: {error}")

    return

def insertManyCarTypeData(cursor, mydb, many_cars):
    try:
        mySql_insert_query = ("INSERT INTO CarType "
                              "(CarTypeID, CarClass, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.executemany(mySql_insert_query, many_cars)
        mydb.commit()
        print(f"{len(many_cars)} records inserted successfully into CarType table")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert records into CarType table: {error}")

    return

def insertCarData(cursor, mydb, car_vin, car_type_id, brand, model_name, year_made, color, mileage, last_tune_up,
                  branch_id, car_in_cycle):
    try:
        mySql_insert_query = ("INSERT INTO CarMISC "
                              "(CarVIN, CarTypeID, Brand, ModelName, YearMade, Color, Mileage, LastTuneUp, BranchID, CarInCycle) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (
        car_vin, car_type_id, brand, model_name, year_made, color, mileage, last_tune_up, branch_id, car_in_cycle)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Car with VIN {car_vin} inserted successfully into CarMISC table")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into CarMISC table: {error}")

    return

def insertBranchData(cursor, mydb, branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country):
    try:
        mySql_insert_query = ("INSERT INTO BranchTable "
                              "(BranchID, BranchName, AreaCode, ContactNumber, Street, PostalCode, City, Province, Country) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Branch {branch_id} inserted successfully into BranchTable")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into BranchTable: {error}")

    return

def insertEmployeeData(cursor, mydb, employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password, active):
    try:
        mySql_insert_query = ("INSERT INTO EmployeeTable "
                              "(EmployeeID, BranchID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password, Active) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (employee_id, branch_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password, active)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Employee {employee_id} inserted successfully into EmployeeTable")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into EmployeeTable: {error}")

    return

def insertCustomerData(cursor, mydb, customer_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password):
    try:
        mySql_insert_query = ("INSERT INTO CustomerTable "
                              "(CustomerID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (customer_id, operator_id, first_name, last_name, street, postal_code, dob, area_code, contact_number, password)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Customer {customer_id} inserted successfully into CustomerTable")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into CustomerTable: {error}")

    return

def insertRentalTransactionData(cursor, mydb, transaction_id, rental_cost, rented_from, rented_to, employee_id, customer_id, car_vin, branch_pickup, branch_dropoff):
    try:
        mySql_insert_query = ("INSERT INTO RentalTransactions "
                              "(TransactionID, RentalCost, RentedFrom, RentedTo, EmployeeID, CustomerID, CarVIN, BranchPickUp, BranchDropOff) "
                              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        record = (transaction_id, rental_cost, rented_from, rented_to, employee_id, customer_id, car_vin, branch_pickup, branch_dropoff)
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(f"Transaction {transaction_id} inserted successfully into RentalTransactions")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert into RentalTransactions: {error}")

    return

def createDataForCarType(cursor, mydb):
    daily_cost = 10
    weekly_cost = 60
    monthly_cost = 200
    records = []

    for i in range(7):
        for k in range(8):
            for t in range(3):
                for y in range(3):
                    for u in range(4):
                        for o in range(3):
                            records.append((i, k, t, y, u, o, daily_cost, weekly_cost, monthly_cost))

    try:
        cursor.executemany(
            "INSERT INTO CarType (CarClass, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            records
        )
        mydb.commit()
        print(f"{len(records)} records inserted into CarType")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert records into CarType: {error}")

    return

def createDataForBranch(cursor, mydb):
    branch_id = 0
    first_half_branch_name = "USA branch name test "
    second_half_branch_name = 0
    area_code = 100
    contact_number = 1000000
    street = "Somewhere in USA"
    zip_code = "zfive"  # Invalid ZIP code placeholder, fix if necessary
    city = 0
    state = 0
    country = 0

    for i in range(5000):
        branch_name = first_half_branch_name + str(second_half_branch_name)
        insertBranchData(cursor, mydb, branch_id, branch_name, area_code, contact_number, street, zip_code, city, state, country)
        branch_id += 1
        contact_number += 1
        city += 1
        if city > 700:
            city = 0
        state += 1
        if state > 50:
            state = 0
        second_half_branch_name += 1

    branch_id = 10000
    first_half_branch_name = "CANADA branch name test "
    second_half_branch_name = 0
    area_code = 200
    contact_number = 2000000
    street = "Somewhere in CANADA"
    postal_code = "T1T1T1"
    city = 1000
    province = 100
    country = 1

    for k in range(3000):
        branch_name = first_half_branch_name + str(second_half_branch_name)
        insertBranchData(cursor, mydb, branch_id, branch_name, area_code, contact_number, street, postal_code, city, province, country)
        branch_id += 1
        contact_number += 1
        city += 1
        if city > 1100:
            city = 1000
        province += 1
        if province > 109:
            province = 100
        second_half_branch_name += 1

    return

def createDataForEmployee(cursor, mydb):
    employee_id = 0
    branch_id = 0
    operator_id = 20000000
    street = "Some street for customer"
    postal_code = "T1T1T1"
    day = 0
    month = 1
    year = 1959
    area_code = 200
    contact_number = 5000000

    for i in range(1000):
        operator_id += 1
        first_name = f"first_name {i}"
        last_name = f"last_name {i}"
        password = f"password {i}"
        day += 1
        if day > 28:
            month += 1
            day = 1
            if month > 12:
                month = 1
                year += 1
        dob = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
        contact_number += 1

        insertEmployeeData(
            cursor, mydb, employee_id, branch_id, operator_id, first_name, last_name,
            street, postal_code, dob, area_code, contact_number, password, 1
        )

        employee_id += 1
        branch_id += 1
        if branch_id > 4999:
            branch_id = 0

    return

def createDataForCustomer(cursor, mydb):
    customer_id = 0
    operator_id = 10000000
    street = "Some street for customer"
    postal_code = "T1T1T1"
    day = 0
    month = 1
    year = 1959
    area_code = 200
    contact_number = 4000000

    for i in range(4000):
        operator_id += 1
        first_name = f"first_name {i}"
        last_name = f"last_name {i}"
        password = f"password {i}"
        day += 1
        if day > 28:
            month += 1
            day = 1
            if month > 12:
                month = 1
                year += 1
        dob = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
        contact_number += 1

        insertCustomerData(
            cursor, mydb, customer_id, operator_id, first_name, last_name,
            street, postal_code, dob, area_code, contact_number, password
        )

        customer_id += 1

    return

def createDataForCar(cursor, mydb):
    records = []
    for k in range(5000):
        car_vin = generate_unique_car_vin(cursor)
        records.append((
            car_vin,  # Unique VIN
            37,  # CarTypeID
            9,  # Brand
            9001,  # ModelName
            2024,  # YearMade
            4,  # Color
            6000,  # Mileage
            '2023-01-01',  # LastTuneUp
            k % 5000,  # BranchID
            1  # CarInCycle
        ))
    try:
        cursor.executemany(
            "INSERT INTO CarMISC (CarVIN, CarTypeID, Brand, ModelName, YearMade, Color, Mileage, LastTuneUp, BranchID, CarInCycle) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            records
        )
        mydb.commit()
        print(f"{len(records)} cars inserted successfully into CarMISC")
    except mysql.connector.Error as error:
        mydb.rollback()
        print(f"Failed to insert cars into CarMISC: {error}")

def generate_unique_car_vin(cursor):
    while True:
        vin = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=17))
        cursor.execute("SELECT COUNT(*) FROM CarMISC WHERE CarVIN = %s", (vin,))
        if cursor.fetchone()[0] == 0:
            return vin

    return False