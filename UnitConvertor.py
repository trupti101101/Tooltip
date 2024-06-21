def length_conversion(value, from_unit, to_unit):
    conversions = {
        "meter": {"meter": 1, "kilometer": 0.001, "mile": 0.000621371},
        "kilometer": {"meter": 1000, "kilometer": 1, "mile": 0.621371},
        "mile": {"meter": 1609.34, "kilometer": 1.60934, "mile": 1},
    }
    return value * conversions[from_unit][to_unit]

def weight_conversion(value, from_unit, to_unit):
    conversions = {
        "gram": {"gram": 1, "kilogram": 0.001, "pound": 0.00220462},
        "kilogram": {"gram": 1000, "kilogram": 1, "pound": 2.20462},
        "pound": {"gram": 453.592, "kilogram": 0.453592, "pound": 1},
    }
    return value * conversions[from_unit][to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        return value * 9/5 + 32 if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32

def convert(value, from_unit, to_unit, conversion_type):
    if conversion_type == "length":
        return length_conversion(value, from_unit, to_unit)
    elif conversion_type == "weight":
        return weight_conversion(value, from_unit, to_unit)
    elif conversion_type == "temperature":
        return temperature_conversion(value, from_unit, to_unit)
    else:
        raise ValueError("Invalid conversion type")

def main():
    print("\n==Welcome To Unit Converter==")
    
    while True:
        print("Choose conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")

        conversion_choice = input("Enter your choice (1/2/3): ")
        if conversion_choice == '1':
            conversion_type = "length"
            units = {1: "meter", 2: "kilometer", 3: "mile"}
        elif conversion_choice == '2':
            conversion_type = "weight"
            units = {1: "gram", 2: "kilogram", 3: "pound"}
        elif conversion_choice == '3':
            conversion_type = "temperature"
            units = {1: "celsius", 2: "fahrenheit", 3: "kelvin"}
        else:
            print("Invalid choice")
            continue

        print(f"Available units for {conversion_type} conversion:")
        for key, unit in units.items():
            print(f"{key}. {unit}")
        
        try:
            from_unit_key = int(input("Enter the number for the unit to convert from: "))
            to_unit_key = int(input("Enter the number for the unit to convert to: "))
            from_unit = units[from_unit_key]
            to_unit = units[to_unit_key]
        except (ValueError, KeyError):
            print("Invalid units")
            continue

        try:
            value = float(input("Enter the value to convert: "))
        except ValueError:
            print("Invalid value")
            continue

        try:
            result = convert(value, from_unit, to_unit, conversion_type)
            print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
        except ValueError as e:
            print(e)
        
        continue_choice = input("Do you want to perform another conversion? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Thank you for using the Unit Converter!")
            break

if __name__ == "__main__":
    main()
