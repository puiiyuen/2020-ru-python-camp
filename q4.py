# Author: Patrick
# Date: 2020/12/21
# Task/Requirement: Write a program which sorts an array in ascending and descending order

def main():
    arr = [3,5,42,455,67,67,4,-1,-55]
    print("The array is: ",arr)
    print("sort ascending: ", sorted(arr))
    print("sort descending: ", sorted(arr,reverse=True))

if __name__ == "__main__":
    main()