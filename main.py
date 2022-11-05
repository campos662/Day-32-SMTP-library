import smtplib
import datetime as dt
import random

def sender(mail_q):
    my_email = "carlos@gmail.com"
    password = "Añadir_Password"

    connection = smtplib.SMTP("smtp.gmail.com")
    port = 587

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="carlos@yahoo.com", msg=f"Subject: Today's thought\n\n{mail_q}")
    connection.close()

def quote_selector():
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
    return random.choice(quotes)


now = dt.datetime.now()
day_of_the_week = now.weekday()

mail_quote = ""

if day_of_the_week == 4:
    mail_quote = quote_selector()
    sender(mail_quote)
    print(mail_quote)








