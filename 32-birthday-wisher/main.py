##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import random
from email.message import EmailMessage

from pandas import *
import smtplib

def send_email(wishes, receiver_email):
    my_email = "p.palat@samsung.com"
    password = "Trouble01!"
    msg = EmailMessage()
    msg['Subject'] = "Happy Birthday!"
    msg['From'] = my_email
    msg['To'] = receiver_email
    msg.set_content(wishes)
    with  smtplib.SMTP("smtp.w1.samsung.net", 25) as connection:
        connection.login(user=my_email, password=password)
        connection.send_message(msg)

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
today_tuple=(today_month,today_day)

birthdays = read_csv('birthdays.csv')

#born_today = birthdays[(birthdays['month'] == today_month) & (birthdays['day'] == today_day)]
birthday_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in birthdays.iterrows()}
if today_tuple in birthday_dict:
    born_today = birthday_dict[today_tuple]
    num=random.randint(1,3)
    with (open(f"letter_templates/letter_{num}.txt","r")) as file:
        wish_letter = file.read()

    wish_letter = wish_letter.replace('[NAME]',born_today['name'])
    email = born_today['email']
    send_email(wish_letter, email)











