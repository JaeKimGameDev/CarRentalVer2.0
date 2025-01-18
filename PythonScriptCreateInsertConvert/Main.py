import random
import IdentifyData
import InsertDataToTables
import CreateTables
import mysql.connector
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    MYSQLpassword = os.getenv("MYSQLpassword")
    database_name = os.getenv("DatabaseName")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=MYSQLpassword,
        database=database_name
    )

    #CreateTables
    # CreateDatabase(mydb, database_name)
    # ShowAllDB(mydb)
    # CreateTables(mydb)

    #Insert Data to Tables
    # try:
    #     createDataForCarType(cursor, mydb)
    #     createDataForBranch(cursor, mydb)
    #     createDataForEmployee(cursor, mydb)
    #     createDataForCustomer(cursor, mydb)
    #     createDataForCar(cursor, mydb)
    # except mysql.connector.Error as error:
    #     print(f"Error: {error}")
    # finally:
    #     cursor.close()
    #     mydb.close()
    #     print("Database connection closed")


    cursor = mydb.cursor()
    IdentifyData.identify_car_type_id(cursor, 20)
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")

    return

if __name__ == "__main__":
    main()