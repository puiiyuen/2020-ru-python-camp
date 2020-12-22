# Author: Patrick
# Date: 2020/12/21

# Task/Requirement:
# Files are backed up with the following name format every day: yearmonthday_backup_appname.xyz,
# e.g. day1: 20190101_backup_prtg.zip
# day2: 20190102_backup_prtg.zip
# write a program which creates a string with the filename for all the days in all the months in a year

from calendar import monthrange
import datetime


def main():
    year = int(input("Input a year(e.g. 2020): "))
    appname = input("Input a app name(whatsapp): ")
    day_amount = 0
    backup_filename_list = []
    print("The filename for all days in all months in a year ",
          year, "of the backup of ", appname, ": ")
    for month in range(1, 13):
        day_amount = monthrange(year, month)
        for day in range(1, day_amount[1]+1):
            filename = datetime.datetime(year, month, day).strftime("%Y%m%d")
            filename += '_backup_'
            filename += appname
            filename += '.zip'
            backup_filename_list.append(filename)
            print(filename)
    # print(backup_filename_list)


if __name__ == "__main__":
    main()

# OUTPUT
# Input a year(e.g. 2020): 2020
# Input a app name(whatsapp): whatsapp
# The filename for all days in all months in a year  2020 of the backup of  whatsapp :
# 20200101_backup_whatsapp.zip
# 20200102_backup_whatsapp.zip
# 20200103_backup_whatsapp.zip
# 20200104_backup_whatsapp.zip
# 20200105_backup_whatsapp.zip
# 20200106_backup_whatsapp.zip
# ......
# 20201219_backup_whatsapp.zip
# 20201220_backup_whatsapp.zip
# 20201221_backup_whatsapp.zip
# 20201222_backup_whatsapp.zip
# 20201223_backup_whatsapp.zip
# 20201224_backup_whatsapp.zip
# 20201225_backup_whatsapp.zip
# 20201226_backup_whatsapp.zip
# 20201227_backup_whatsapp.zip
# 20201228_backup_whatsapp.zip
# 20201229_backup_whatsapp.zip
# 20201230_backup_whatsapp.zip
# 20201231_backup_whatsapp.zip
