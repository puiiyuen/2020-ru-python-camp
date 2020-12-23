# Author: Patrick
# Date: 2020/12/21
# Task/Requirement: Write a program which adds, subtracts, multiplies and divides two variables

# function: addition 
# parameter: x: number, y: number
def add(x, y):
    return x+y

# function: substraction 
# parameter: x: number, y: number
def substract(x, y):
    return x-y

# function: multiplication 
# parameter: x: number, y: number
def multiplies(x, y):
    return x*y

# function: division 
# parameter: x: number, y: number
def divides(x, y):
    return x/y


def main():
    x = float(input("Input x: "))
    y = float(input("Input y: "))

    print("The results are: ")
    print("x+y=", add(x, y))
    print("x-y=", substract(x, y))
    print("x*y=", multiplies(x, y))
    print("x/y=", divides(x, y))


if __name__ == "__main__":
    main()
