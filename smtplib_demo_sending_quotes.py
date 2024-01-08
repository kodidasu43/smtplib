#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "test1360degrees@gmail.com"
MY_PASSWORD = "XXXXXXXXXXXXX"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



# Sending Email with Python
# import smtplib

# my_email = "test1360degrees@gmail.com"
# password = "XXXXXXXXXXXXX"

# with smtplib.SMTP("smtp.gmail.com") as connection:
    # connection.starttls()
    # connection.login(user=my_email, password=password)
    # connection.sendmail(
        # from_addr=my_email,
        # to_addrs="ivyniah3107@gmail.com",
        # msg="Subject:Hello\n\nThis is the body of my email."
    # )


# Working with date and time in Python
# import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)