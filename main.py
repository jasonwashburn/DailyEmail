
# TODO 3. Email Dad joke and quote to myself daily
# TODO 4. HTML formatting?
# TODO 5. Configure to use github actions/secrets

import datetime as dt
import smtplib
import random
import config  # store our login info separate from code to keep it out of git
import requests
import json

DAD_JOKE_URL = 'https://icanhazdadjoke.com/'
QUOTES_URL = 'https://zenquotes.io/api/today'

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


def get_dad_joke():
    headers = {
        "Accept": "application/json",
        "user-agent": "WBurn - Daily Email GitHub repo https://github.com/jasonwashburn/DailyEmail"
    }
    try:
        request = requests.get(DAD_JOKE_URL, headers=headers)
        response = json.loads(request.text)
        return response
    except Exception as ex:
        raise Exception(f"Unable to retrieve dad joke from {DAD_JOKE_URL}: {ex}")


def get_quote():
    try:
        request = requests.get(QUOTES_URL)
        response = json.loads(request.text)
        return response
    except Exception as ex:
        raise Exception(f"Unable to retrieve dad joke from {QUOTES_URL}: {ex}")



print(get_dad_joke()['joke'])
print(get_quote())
email_message = f"{get_dad_joke()['joke']}\n\n{get_quote()[0]['q']} - {get_quote()[0]['a']}"
send_email(to_address=config.target_email, subject="Daily Dad Joke and Quote", message=email_message)