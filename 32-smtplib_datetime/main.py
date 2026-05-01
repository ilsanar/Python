import smtplib
import random
import datetime as dt

def send_email(quote):
    my_email = "p.palat@samsung.com"
    password = "Trouble01!"
    msg = f"Subject: Your motivation for today!\n\n{quote}"
    with  smtplib.SMTP("smtp.w1.samsung.net", 25) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs= my_email,
                            msg=msg)


#
# now = dt.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
#
# date_of_birth = dt.datetime(year=1985, month=5, day=21, hour=16)
# print(date_of_birth)

if dt.datetime.now().weekday() == 1:

    with open("quotes.txt","r") as file:
        quotes = file.read().splitlines()

    today_quote = random.choice(quotes)
    send_email(today_quote)

