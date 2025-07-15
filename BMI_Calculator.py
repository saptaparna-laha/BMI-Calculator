print("One click to calculate. One step to better health.")
# BMI Calculator
input_weight = input("Enter your weight in kg: ")
input_height = input("Enter your height in meters: ")

weight = float(input_weight)
height = float(input_height)
if weight <= 0 or height <= 0:
    raise ValueError("Weight and height must be positive numbers.")
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
if 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
if 25 <= bmi < 29.9:
    print("You are overweight.")        