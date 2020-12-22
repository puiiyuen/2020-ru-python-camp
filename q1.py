# Author: Patrick
# Date: 2020/12/21
# Task/Requirement: Write a program which adds, subtracts, multiplies and divides two variables

def add(x, y):
    return x+y


def substract(x, y):
    return x-y


def multiplies(x, y):
    return x*y


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
