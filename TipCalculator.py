# MOSONIK FAITH CHEPKOECH SCT211-0044/2022
# Defining a function that wil act as the tip calculator
def tipCalculator(totalBill, tipPercentage, numPeople):
    tipAmount = (totalBill * tipPercentage) / 100
    total_with_tip = totalBill + tipAmount
    Amountperperson = total_with_tip / numPeople
    return Amountperperson

# the variables below will be used to store the user input
totalBill = float(input("Enter the total bill amount: sh"))
tipPercentage = float(input("Enter the tip percentage (10, 12, or 15): "))
numPeople = int(input("Enter the number of people splitting the bill: "))

if tipPercentage not in (10, 12, 15):
    print("Invalid tip percentage. Please enter 10, 12, or 15.")

# calling the function tipcalculator to calculate the amaount payable by each person
Amountperperson = tipCalculator(totalBill, tipPercentage, numPeople)
# Displaying the amount payable by each person
print("Each person should pay sh.{}".format(Amountperperson))