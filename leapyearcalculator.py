#MOSONIK FAITH CHEPKOECH SCT211-0044/2022
# Defining a function for checking whether a year is leap or not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a leap year")

year = int(input("Enter a year: "))

is_leap_year(year) #calling the function for checking if a yearis leap or not