"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
from calendar import TextCalendar
from datetime import datetime

ERROR_MSG = 'Invalid arguments (expected numbers in format "[month] [year]")'
START_DAY = 6  # Start weeks on Sunday

console_args = sys.argv[1:]

try:
    arg_count = len(console_args)
    if arg_count == 0:
        present_datetime = datetime.now()
        month = present_datetime.month
        year = present_datetime.year
        TextCalendar(START_DAY).prmonth(year, month)
    elif arg_count == 1:
        month = console_args[0]
        year = datetime.now().year
        TextCalendar(START_DAY).prmonth(year, int(month))
    elif arg_count == 2:
        # pylint: disable=unbalanced-tuple-unpacking
        month, year = console_args
        TextCalendar(START_DAY).prmonth(int(year), int(month))
    else:
        raise Exception("")
except Exception as error:
    print(ERROR_MSG if error.__str__() == "" else f"\nTrace:\n'{error}'")
