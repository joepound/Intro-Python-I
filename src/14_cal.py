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

ERROR_MSG = 'Invalid arguments (expected numbers in format "month [year]")'

try:
    # First system argument is the file being accessed (ex.: "14_cal.py"),
    # so disregard it.
    if len(sys.argv) < 4:
        if len(sys.argv) == 3:
            month = sys.argv[1]
            year = sys.argv[2]
            TextCalendar(6).prmonth(int(year), int(month))
        elif len(sys.argv) == 2:
            month = sys.argv[1]
            year = datetime.now().year
            TextCalendar(6).prmonth(year, int(month))
        else:
            month = datetime.now().month
            year = datetime.now().year
            TextCalendar(6).prmonth(year, month)
    else:
        raise Exception("")
except Exception as error:
    print(ERROR_MSG)
    if error != "":
        print(f"\nTrace:\n{error}")
