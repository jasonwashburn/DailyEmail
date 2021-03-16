import smtplib
import config

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=config.my_email, password=config.password)
    connection.sendmail(
        from_addr=config.my_email,
        to_addrs="wburn.test@yahoo.com",
        msg="Subject: Hello\n\nThis is the body of my email."
    )
