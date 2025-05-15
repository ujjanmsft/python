# Welcome to the BMI Calculator!
def get_user_data():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    return weight, height

# Calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30: 
        return "overweight"
    else:
        return "Obese"
    
def run_bmi_calculator():
    weight, height = get_user_data()
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f"\nYour BMI is: {bmi}")
    print(f"You are classified as: {category}")

run_bmi_calculator()

