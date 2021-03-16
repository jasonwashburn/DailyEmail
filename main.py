import datetime as dt
import smtplib
import random
import config  # store our login info separate from code to keep it out of git


def send_email(to_address, subject, message):
    # Sends an email message using the email server info provided in config.py
    #
    # args:
    #   to_address: email address of the recipient
    #   subject: subject of email
    #   message: message to send
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=config.my_email, password=config.password)
        connection.sendmail(
            from_addr=config.my_email,
            to_addrs=to_address,
            msg=f"Subject: {subject}\n\n{message}"
        )


# Load quote data from quotes.txt into list
with open("quotes.txt", "r") as quotes_file:
    quotes = [line for line in quotes_file]

now = dt.datetime.now()
if now.weekday() == 1:
    send_email(to_address="wburn.test@yahoo.com", subject="Inspirational Quote", message=random.choice(quotes))