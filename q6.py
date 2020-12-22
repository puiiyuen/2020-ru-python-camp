# Author: Patrick
# Date: 2020/12/21
# Find all numbers between 2000 and 3200, which are divisible by 7 but are not a multiple of 5

def main():
    result = []
    for i in range(2000, 3200+1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)

    print("The numbers betoween 2000 and 3200, which are divisible by 7 but are not a multiple of 5", result)


if __name__ == "__main__":
    main()
