import smtplib

my_email = "appbreweryinfo@gmail.com"  # email account
password = "abcd1234()"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.close()

with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider
    connection.starttls()  # encrypted
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="appbrewerytesting@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email.")

# # # # #

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(day_of_week))

date_of_birth = dt.datetime(year=2004, month=6, day=21)
print(date_of_birth)
