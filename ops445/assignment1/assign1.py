#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025

Program: assign1.py
Author: "Student Full Name" - "Student ID"

The python code in this file (assign1.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 2025-02-12
'''
import sys

def usage():
    
    print("Usage: assign1.py DD-MM-YYYY NN", end="")

def days_in_mon(year):
    "This def has the dictionary of all of the months and the max amount of days in each month"
    "the leap years for feburary are accounted for by calling the leap_year() function"
   

    
    feb_max = leap_year(year)

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mon_max
    # return dictionary_months
    

def valid_date(date):
    "This will check if the entered date is valid and if true it will send the dates to the functions that call for it"
    # return True or False 
   
    if len(date) != 10:
        return False
    try:
        str_day, str_month, str_year = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        if month < 1 or month > 12:
            return False
        mon_max = days_in_mon(year)
        if day < 1 or day > mon_max.get(month, 0):
            return False
    
        return True
    except ValueError:
        return False
def leap_year(year):
    "takes a year in YYYY format, and returns True if it's a leap year, False otherwise."
    
    lyear = year % 4 
    if lyear == 0:
        feb_max = 29 # this is a leap year
        
    else:
        feb_max = 28 # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year
    return feb_max

def after(today):
    "after takes a valid date string in DD-MM-YYYY format and returns"
    "a date string for the next day in DD-MM-YYYY format."
    if not valid_date(today):
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        mon_max = days_in_mon(year)

        tmp_day = day + 1 # next day

        
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    "Function will substract days from the date if the user inputs a negitive integer"
    if not valid_date(today):
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        mon_max = days_in_mon(year)

        tmp_day = day - 1 # before day

        # to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1
        if tmp_day < 1:
            tmp_month = month - 1
            if tmp_month < 1:
                tmp_month = 12
                year = year - 1
            tmp_day = mon_max[tmp_month]
            to_day = tmp_day
        else:
            tmp_month = month
            to_day = tmp_day
        to_month = tmp_month
       
        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date
   

def dbda(start_date, num_days):
    "Will loop and add/substract the dates depending on the number given"
    end_date = start_date
    # create a loop
    if num_days > 0:
        for _ in range(num_days):
            end_date = after(end_date)
    elif num_days <= 0:
        for _ in range(abs(num_days)):
            end_date = before(end_date)

    return end_date
    # call before() or after() as appropriate
    # return end_date


if __name__ == "__main__":
    "the main block where it uses sys.argv to accept inputs if the input is not valid it will call the usage function"
    if len(sys.argv) != 3:
        usage()  
        sys.exit(1)
    start_date = sys.argv[1]
    if not valid_date(start_date):
        usage()
        sys.exit(1)
    try:
        num_days = int(sys.argv[2])
        result = dbda(start_date, num_days)
        print(f"Resulting date: {result}")
    except ValueError:
        print('Error: Please use a number instead of a letter for the second input ')
    

