def convert_length(value, from_unit, to_unit):
    # Length conversion logic
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'miles': 1609.34
    }
    
    # Convert to meters first, then convert to the target unit
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Temperature conversion logic
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit conversion (no conversion)

def convert_weight(value, from_unit, to_unit):
    # Weight conversion logic
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    
    # Convert to grams first, then convert to the target unit
    value_in_grams = value * weight_units[from_unit]
    return value_in_grams / weight_units[to_unit]

def unit_converter():
    print("Welcome to the Unit Converter!")
    
    while True:
        print("\nSelect conversion type:")
        print("1. Length")
        print("2. Temperature")
        print("3. Weight")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Length Conversion
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from (meters, kilometers, centimeters, millimeters, inches, feet, miles): ").lower()
            to_unit = input("Enter the unit to convert to (meters, kilometers, centimeters, millimeters, inches, feet, miles): ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == '2':
            # Temperature Conversion
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ").capitalize()
            to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ").capitalize()
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == '3':
            # Weight Conversion
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from (grams, kilograms, milligrams, pounds, ounces): ").lower()
            to_unit = input("Enter the unit to convert to (grams, kilograms, milligrams, pounds, ounces): ").lower()
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}.")

        elif choice == '4':
            print("Exiting the Unit Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    unit_converter()
