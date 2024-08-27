def identify_car_class(cursor, car_class_id):
    car_type_tuple = ("Economy", "Full", "Luxury", "Sport", "Muscle", "Super", "Industrial")
    print(car_type_tuple[car_class_id])
    return

def identify_car_frame(cursor, frame_id):
    car_frame_id = ("Sedan", "Coupe", "Convertible", "SUV", "Truck", "Van", "Station Wagon", "Hatchback")
    print(car_frame_id[frame_id])
    return

def identify_car_cabin_size(cursor, cabin_size_id):
    cabin_size_tuple = ("Small", "Medium", "Full")
    print(cabin_size_tuple[cabin_size_id])
    return

def identify_car_engine(cursor, engine_id):
    engine_tuple = ("Gasoline", "Electric", "Hydrogen")
    print(engine_tuple[engine_id])
    return

def identify_drivetrain(cursor, drivetrain_id):
    drivetrain_tuple = ("FWD", "RWD", "AWD", "4WD")
    print(drivetrain_tuple[drivetrain_id])
    return

def identify_trim(cursor, trim_id):
    trim_tuple = ("Base", "Partically Loaded", "Fully Loaded")
    print(trim_tuple[trim_id])
    return

def identify_car_type_id(cursor, car_type_id):
    query = ("SELECT * FROM cartype WHERE cartypeid = %s")
    cursor.execute(query, (car_type_id,))
    result = cursor.fetchone()
    print(result)

    identify_car_class(cursor, result[1])
    identify_car_frame(cursor, result[2])
    identify_car_cabin_size(cursor, result[3])
    identify_car_engine(cursor, result[4])
    identify_drivetrain(cursor, result[5])
    identify_trim(cursor, result[6])
    return

def identify_brand(brand_id):
    brand_tuple = ("Audi", "BMW", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge", "Ford", "GMC", "Honda", "Hummer",
                   "Hyundai", "Infiniti", "Jeep", "Kia" , "LandRover", "Lexus", "Lincoln", "Mazda", "Mercedes-Benz",
                   "Mitsubishi", "Nissan", "Peugeot", "Porsche", "Regal", "Subaru", "Toyota", "Volkswagen", "Volvo")
    print(brand_tuple[brand_id])
    return

# used to print out long Excel files to a list.
def extract_excel_data(file_name, sheet_name, column_name):
    #excel_data_df = pd.read_excel('CarInfo.xlsx', sheet_name='CarModel')
    #print(excel_data_df['Car Model'].tolist())
    excel_data_df = pd.read_excel(file_name, sheet_name=sheet_name)
    print(excel_data_df[column_name].tolist())
    return

# could just read excel file and print out the car model based on car_model_id. This method having it in a tuple however, should be faster as it is already integrated into the ram
def identify_model(car_model_id):
    car_model_tuple = ('Audi A3', 'Audi A4', 'Audi A5', 'Audi A7', 'Audi A8', 'Audi e-tron GT', 'Audi Q3', 'Audi Q4', 'Audi Q5',
     'Audi Q7', 'Audi Q8', 'Audi Q8', 'Audi SQ5', 'Audi SQ7', 'Audi SQ8', 'Audi SQ8', 'Audi TT', 'BMW 2-Series',
     'BMW 3-Series', 'BMW 4-Series', 'BMW 5-Series', 'BMW 7-Series', 'BMW 8-Series', 'BMW i4', 'BMW i5', 'BMW i7',
     'BMW M4', 'BMW M5', 'BMW X1', 'BMW X2', 'BMW X3', 'BMW X4', 'BMW X5', 'BMW X6', 'BMW X7', 'BMW Z4',
     'Buick Electra E5', 'Buick Enclave', 'Buick Envision', 'Buick Regal', 'Buick Regal', 'Cadillac CT4',
     'Cadillac CT5', 'Cadillac Escalade', 'Cadillac ESV', 'Cadillac XT4', 'Cadillac XT5', 'Cadillac XT6',
     'Chevrolet Blazer', 'Chevrolet Bolt', 'Chevrolet Camaro', 'Chevrolet Colorado', 'Chevrolet Corvette',
     'Chevrolet Equinox', 'Chevrolet Malibu', 'Chevrolet Silverado 1500', 'Chevrolet Suburban', 'Chevrolet Tahoe',
     'Chevrolet TrailBlazer', 'Chevrolet Traverse', 'Chevrolet Trax', 'Chrysler 300', 'Chrysler Grand Caravan',
     'Chrysler Pacifica', 'Dodge Challenger', 'Dodge Charger', 'Dodge Durango', 'Dodge Hornet', 'Ford Bronco',
     'Ford E-Transit', 'Ford Edge', 'Ford Escape', 'Ford Expedition', 'Ford Explorer', 'Ford F-150', 'Ford Mach-E',
     'Ford Maverick', 'Ford Mustang', 'Ford Ranger', 'Ford Super-Duty', 'Ford Transit', 'GMC Acadia', 'GMC AT4',
     'GMC Canyon', 'GMC Hummer', 'GMC Sierra 1500', 'GMC Terrain', 'GMC Yukon', 'Honda Accord', 'Honda Civic',
     'Honda CR-V', 'Honda HR-V', 'Honda Odyssey', 'Honda Passport', 'Honda Pilot', 'Honda Prologue', 'Honda Ridgeline',
     'Hyundai Elantra', 'Hyundai Ioniq 5', 'Hyundai Ioniq 6', 'Hyundai Kona', 'Hyundai Palisade', 'Hyundai Santa Cruz',
     'Hyundai Santa Fe', 'Hyundai Sonata', 'Hyundai Tucson', 'Hyundai Venue', 'Infiniti Q50', 'Infiniti QX50',
     'Infiniti QX55', 'Infiniti QX60', 'Infiniti QX80', 'Kia Carnival', 'Kia EV6', 'Kia EV9', 'Kia Forte', 'Kia K4',
     'Kia K5', 'Kia Niro', 'Kia Seltos', 'Kia Sorento', 'Kia Soul', 'Kia Sportage', 'Kia Telluride', 'Lexus ES',
     'Lexus GX', 'Lexus IS', 'Lexus LC', 'Lexus LS', 'Lexus LX', 'Lexus NX', 'Lexus RC', 'Lexus RX', 'Lexus RZ',
     'Lexus TX', 'Lexus UXh', 'Lincoln Aviator', 'Lincoln Corsair', 'Lincoln Nautilus', 'Lincoln Navigator',
     'Mazda CX-30', 'Mazda CX-50', 'Mazda CX-50', 'Mazda CX-70', 'Mazda CX-90', 'Mazda MX-5', 'Mazda3',
     'Mercedes C-Class', 'Mercedes CLA', 'Mercedes CLE', 'Mercedes CLE', 'Mercedes E-Class', 'Mercedes EQB',
     'Mercedes EQE', 'Mercedes EQS', 'Mercedes G-Class', 'Mercedes GLA', 'Mercedes GLB', 'Mercedes GLC', 'Mercedes GLE',
     'Mercedes GLS', 'Mercedes GT', 'Mercedes S-Class', 'Mercedes SL', 'Mitsubishi Eclipse', 'Mitsubishi Mirage',
     'Mitsubishi Outlander', 'Mitsubishi RVR', 'Nissan Altima', 'Nissan Ariya', 'Nissan Armada', 'Nissan Frontier',
     'Nissan GTR', 'Nissan Kicks', 'Nissan Leaf', 'Nissan Murano', 'Nissan Pathfinder', 'Nissan Rogue', 'Nissan Sentra',
     'Nissan Versa', 'Nissan Z', 'Subaru Ascent', 'Subaru BRZ', 'Subaru Crosstrek', 'Subaru Forester', 'Subaru Impreza',
     'Subaru Outback', 'Subaru Solterra', 'Toyota 4Runner', 'Toyota Camry', 'Toyota Corolla', 'Toyota Crown',
     'Toyota GR86', 'Toyota Hatchback', 'Toyota Highlander', 'Toyota LandCruiser', 'Toyota Mirai', 'Toyota Prime',
     'Toyota Prius', 'Toyota RAV4', 'Toyota Sequoia', 'Toyota Sienna', 'Toyota Supra', 'Toyota Tacoma', 'Toyota Tundra',
     'Toyota Venza', 'Volkswagen Atlas', 'Volkswagen Golf', 'Volkswagen ID.4', 'Volkswagen ID.7', 'Volkswagen ID.Buzz',
     'Volkswagen Jetta', 'Volkswagen Taos', 'Volkswagen Tiguan', 'Volvo EC40', 'Volvo EX30', 'Volvo EX40', 'Volvo EX90',
     'Volvo S60', 'Volvo S90', 'Volvo V60', 'Volvo XC60', 'Volvo XC90')
    print(car_model_tuple[car_model_id])
    return

def identify_color(color_id):
    color_tuple = ('Black', 'Blue', 'Brown', 'Gold', 'Gray', 'Green',
                   'Orange', 'Pink', 'Purple', 'Red', 'Silver', 'Tan',
                   'Teal', 'White', 'Yellow')
    print(color_tuple[color_id])
    return
