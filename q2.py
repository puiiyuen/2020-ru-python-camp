# Author: Patrick
# Date: 2020/12/21
# Task/Requirement: Write a program which finds the Factorial of a number

# function: factorial
# parameter: n: postitve integer
# recursively call the function
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


def main():
    n = int(input("Input a integer: "))
    print("The factorial of ", n, "is", factorial(n))


if __name__ == "__main__":
    main()
