weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    bmi_range = "underweight"
    print("BMI:", round(bmi, 2), "- you're in the", bmi_range, "range.")
elif 18.5 <= bmi <= 24.9:
    bmi_range = "healthy weight"
    print("BMI:", round(bmi, 2), "- you're in the", bmi_range, "range.")
elif 25 <= bmi <= 29.9:
    bmi_range = "overweight"
    print("BMI:", round(bmi, 2), "- you're in the", bmi_range, "range.")
elif 30 <= bmi <= 39.9:
    bmi_range = "obese"
    print("BMI:", round(bmi, 2), "- you're in the", bmi_range, "range.")
elif bmi >= 40:
    bmi_range = "severely obese"
    print("BMI:", round(bmi, 2), "- you're in the", bmi_range, "range.")
else:
    print("Error, BMI could not be calculated.")
