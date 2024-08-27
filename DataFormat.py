insetCarTypeData = (
    "INSERT INTO CarType (CarTypeID, CarType, CarFrame, CabinSize, Engine, DriveTrain, Trim, DailyCost, WeeklyCost, MonthlyCost) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
insertCarData = (
    "INSERT INTO Car (CarVIN, CarTypeID, Brand, ModelName, YearMade, Color, Mileage, LastTuneUp, BranchID, CarInCycle) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
insertBranchData = (
    "INSERT INTO Branch (BranchID, BranchName, AreaCode, ContactNumber, Street, PostalCode, City, Province, Country) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
insertEmployeeData = (
    "INSERT INTO Employee (EmployeeID, BranchID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password, Active) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
insertCustomerData = (
    "INSERT INTO Customer (CustomerID, OperatorID, FirstName, LastName, Street, PostalCode, DOB, AreaCode, ContactNumber, Password) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
insertRentalTransactionData = (
    "INSERT INTO RentalTransaction (TransactionID, RentalCost, RentedFrom, RentedTo, EmployeeID, CustomerID, CarVIN, BranchPickUp, BranchDropOff) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")