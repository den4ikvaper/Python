import smtplib
import datetime as dt
import random

with open("quotes.txt") as all_quotes:
    all_quotes = all_quotes.readlines()

now = dt.datetime.now()
day = now.weekday()
random_quote = random.choice(all_quotes)
email_text = f"Subject: Wednesday motivation quote!\n\n{random_quote}"

if day == 2:
    my_email = "ratixed@yahoo.com"
    password = "jfacehtxcgztrwuy"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="denpankratix@gmail.com",
                            msg=email_text)


