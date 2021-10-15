#importing the datetime module
from datetime import datetime

#creating a date using year, month, day as arguments
birthday = datetime(1994, 2, 15, 4, 25, 12)
birthday.year
birthday.month
birthday.weekday() #from 0 to 6 with 0 being monday

#creating a date using datime.now()
datetime.now() #current time

#parsing a date using strptime
#Takes a string types of date and convert it into python readable date
parse_date = datetime.strptime("Jan 15, 2018", "%b %d, %Y") #google python datetime and check details in the documentation
parse_date.month
parse_date.year

parse_date = datetime.strptime("Jul 04, 2011", "%b %d, %Y")
parse_date.month
parse_date.year

#rendering a date as a string using strftime
#Takes python dates and output a string of our choice
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
date_string
