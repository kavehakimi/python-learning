def calculate_bmi(weight,height):
    bmi = weight/(height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        catergory = "Underweight"
    elif bmi < 25:
        catergory = "Normal weight"
    elif bmi < 30:
        catergory = "Overweight"
    else:
        catergory = "Obesity"
    return catergory

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print("Your BMI is", round(bmi, 2))
print("Category:", category)
