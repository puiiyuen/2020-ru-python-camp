# Author: Patrick
# Date: 2020/12/21

# Task/Requirement: A website requires the users to input username and password to register. Write a program to check the
# validity of password input by users. Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

import re

def main():
    password = input('Input a password to check: ')
    x = re.search(
        '^(?=.*\d)(?=.+[a-z])(?=.+[A-Z])(?=.+[\$\#\@]).{6,12}$', password)
    if (x == None):
        print('The password is NOT satisfied the criteria')
    else:
        print('The password is satisfied the criteria')


if __name__ == "__main__":
    main()

