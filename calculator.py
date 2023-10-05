#MOSONIK FAITH CHEPKOECH SCT211-0044/2022
Name = input("Enter your name")
print("Hello" + " " + Name)
#method 1
# a = (input("enter the first number"))
# b = (input("Enter the second number"))

# sum1 = eval(f"{a} + {b}")
# print("The sum of {} and {} is {}".format(a, b, sum1))

#method 2
# FirstNumber = (int(input('Enter the first number ')))
# SecondNumber = (int(input('Enter the second number ')))

# sum2 = c + d
# print("The sum of {} and {} is {}".format(c, d, sum2))

# we import datetime in order to help us to find the currrent date and time using the now() function
import datetime
# this is for defining the function to use when calculating the age 
def calculateAge(birthYear, birthMonth, birthDay):
    currentDate = datetime.datetime.now()
    birthDate = datetime.datetime(birthYear, birthMonth, birthDay)
    age = currentDate - birthDate
    #// is for oprarations that produce just the integer quotient
    years = age.days // 365
    #% Is used in oprations for finding a remainder
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    return years, months, days
# asking the user to input their birth year,date and day
birthYear = int(input("Enter your year of birth: "))
birthMonth = int(input("Enter your month of birth (1-12): "))
birthDay = int(input("Enter your day of birth (1-31): "))
# calling the function to calculate age and passing the arguments
years, months, days = calculateAge(birthYear, birthMonth, birthDay)

# printing the output on the screen
print("{}, you are {} years, {} months and {} days old".format(Name, years, months, days))
