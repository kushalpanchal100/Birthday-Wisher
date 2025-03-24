


import smtplib

my_email = "kush70578@gmail.com"
password = "zyjx yrpq oxjg wwot"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="Your Email Address", 
        msg="Subject:Hello\n\nThis is body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_weeks = now.weekday()
print(day_of_weeks)

date_of_birth = dt.datetime(year=2002, month=11, day=23)
print(date_of_birth)

connection.close()
