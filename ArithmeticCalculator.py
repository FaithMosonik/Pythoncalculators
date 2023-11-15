#MOSONIK FAITH CHEPKOECH SCT211-0044/2022
Name = input("Enter your name")
print("Hello" + " " + Name)
#method 1
# a = (input("enter the first number"))
# b = (input("Enter the second number"))

# sum1 = eval(f"{a} + {b}")
# print("The sum of {} and {} is {}".format(a, b, sum1))

# method 2
def sum(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2
  
FirstNumber = (int(input('Enter the first number ')))
SecondNumber = (int(input('Enter the second number ')))

print("The sum of {} and {} is {}".format(FirstNumber, SecondNumber, sum(FirstNumber, SecondNumber)))
