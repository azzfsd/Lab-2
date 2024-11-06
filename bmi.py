def calculate_bmi(weight, height):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
 
    #Calculate the BMI   
    BMI = weight / (height ** 2)
    print("BMI = ", round(BMI, 2))

    #Print BMI
    print("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Under weight")
        return -1
    elif BMI > 25.0:
        print("Over weight")
        return 1
    else:
        print("Normal weight")
        return 0
    

result = calculate_bmi(weight=57, height=1.73)
print("Result = ", result)