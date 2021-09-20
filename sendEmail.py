# Write a Python function to send a basic email notification
# INPUT: Receiver email address,subject line,message body

import smtplib

SENDER_EMAIL = ''
SENDER_PASSWORD = ''


def send_mail(receiver_email, subject, body):
    message = 'Subject : {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)


send_mail('manquiz92@gmail.com', 'HI', 'UMEPATA?')






