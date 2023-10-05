# MOSONIK FAITH CHEPKOECH SCT211-0044/2022
# Defining a function for calculating the BMI
 # BMI formula: weight (kg) / (height (m) * height (m))
def calculateBmi(height, weight):
    heightMeters = height / 100  # Convert height from cm to meters because user will be asked to enter height in cm
    BMI = weight / (heightMeters ** 2) #** operator is a power operator
    return BMI

def results(BMI):
    if BMI < 18.5:
        return("Underweight")
    elif 18.5 <= BMI < 24.9:
        return("Normal Weight")
    else:
        return("Overweight") 

height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = calculateBmi(height, weight)
BMI_interpretation = results(BMI)

print("Your BMI is {}, which falls into the category of {}.".format(BMI, BMI_interpretation))