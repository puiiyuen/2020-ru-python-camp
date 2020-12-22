# Author: Patrick
# Date: 2020/12/21

# Task/Requirement: You have two variable; a = 5 and b = 3, Swap the integers such that a = 3
# and b = 5, without creating additional variables

def main():
    a = 5
    b = 3
    print("Before swap: a =", a, " b =", b)
    a, b = b, a
    print("After swap: a =", a, " b =", b)


if __name__ == "__main__":
    main()
