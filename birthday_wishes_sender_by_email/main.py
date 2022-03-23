from pandas import *
import datetime as dt
import random
import smtplib

letters_templates = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]


def create_email_text(person_name):
    global letters_templates
    with open(random.choice(letters_templates)) as letter_template:
        content = letter_template.read()
        result = content.replace('[NAME]', person_name)
        return result


def send_email(text_for_email, recipient):
    my_email = "denpankratix@gmail.com"
    password = "_1998Denis_"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient,
                            msg=f"Subject: Happy Birthday!\n\n{text_for_email}")


date = dt.datetime.now()
today_month = date.month
today_day = date.day
data = read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

for item in data_dict:
    email = item['email']
    name = item['name']
    birthday_month = item['month']
    birthday_day = item['day']
    if birthday_month == today_month and birthday_day == today_day:
        email_text = create_email_text(name)
        send_email(email_text, email)
        print(f"Email for {name} to {email} already send, because this person have birthday today.")
    else:
        print(f"Email for {name} to {email} not send, because birthday will be at {birthday_month}, {birthday_day}")





