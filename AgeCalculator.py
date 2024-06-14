from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_calculator():
    while True:
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        try:
            age = calculate_age(dob)
            print(f"Your age is: {age}")
            break
        except ValueError:
            print("Invalid input. Please enter the date in YYYY-MM-DD format.")
    
    # Ask the user if they want to continue
    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
    
    if continue_prompt == 'yes':
        age_calculator()  # Restart the process
    else:
        print("Thank you for using Age Calculator!")

if __name__ == "__main__":
    print("==|Welcome To Age Calculator|==")
    age_calculator()
