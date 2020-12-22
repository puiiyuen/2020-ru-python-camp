# Author: Patrick
# Date: 2020/12/21
# Task/Requirement: Write a program that computes the net amount of a bank account based on a
# transaction log from console input. The transaction log format is shown as following:
# D 300
# D 300
# D 100
# W 200

def main():
    balance = 0.0
    op = 'd'
    amount = 0.0
    print("---Welcome to Ryerson Bank---")
    print("* Your account balance is: ", balance)

    while(op == 'd' or op == 'D' or op == 'w' or op == "W"):
        op = input(
            "Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : ")

        if op == 'd' or op == 'D':
            amount = float(input("Input the amount for the transaction: "))
            balance += amount
            print("Your account balance is", balance)
        elif op == 'w' or op == "W":
            amount = float(input("Input the amount for the transaction: "))
            if amount > balance:
                print("* Sorry, your balance is not enough.")
                print("* Please try again.")
            else:
                balance -= amount
                print("* Your account balance is", balance)
        else:
            break

    print("Your account balance is", balance)
    print("---Thank you for using Ryerson Bank---")


if __name__ == "__main__":
    main()

# Output:
# ---Welcome to Ryerson Bank---
# * Your account balance is:  0.0
# Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : D
# Input the amount for the transaction: 300
# Your account balance is 300.0
# Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : D
# Input the amount for the transaction: 300
# Your account balance is 600.0
# Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : D
# Input the amount for the transaction: 100
# Your account balance is 700.0
# Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : W
# Input the amount for the transaction: 200
# * Your account balance is 500.0
# Input 'D' for Deposit, 'W' for Withdraw, others for ending the transaction : e
# Your account balance is 500.0
# ---Thank you for using Ryerson Bank---