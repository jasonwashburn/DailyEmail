# TODO 4. HTML formatting?
# TODO 5. Configure to use github actions/secrets
import html
import smtplib
import requests
import json
import os

DAD_JOKE_URL = 'https://icanhazdadjoke.com/'
QUOTES_URL = 'https://zenquotes.io/api/today'
MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')
TARGET_EMAIL = os.getenv('TARGET_EMAIL')


def send_email(to_address, subject, message):
    # Sends an email message using the email server info provided in config.py
    #
    # args:
    #   to_address: email address of the recipient
    #   subject: subject of email
    #   message: message to send
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_address,
            msg=f"Subject: {subject}\n\n{message}".encode('utf-8')
        )


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
        formatted_quote = f"{response[0]['q']} - {response[0]['a']}"
        return formatted_quote
    except Exception as ex:
        raise Exception(f"Unable to retrieve dad joke from {QUOTES_URL}: {ex}")


quote = get_quote()
dad_joke = get_dad_joke()['joke']
print(dad_joke)
print(quote)
email_message = f"{dad_joke}\n\n{quote}"
send_email(to_address=TARGET_EMAIL, subject="Daily Dad Joke and Quote", message=email_message)
