def calculate_bmi(weight, height):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))

    BMI = weight / (height ** 2)
    print("BMI = ", round(BMI, 2))
    print("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Under weight")
    elif BMI > 25.0:
        print("Over weight")
    else:
        print("Normal weight")
    

calculate_bmi(weight=57,height=1.73)
print("==========")
calculate_bmi(weight=97,height=1.73)
print("==========")
calculate_bmi(weight=37,height=1.73)