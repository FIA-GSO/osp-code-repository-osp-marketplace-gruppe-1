import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

class EmailService:
    SENDER_EMAIL = "your_email@gmail.com"
    RECIEVER_EMAIL = "recipient_email@gmail.com"
    SUBJECT = "Updated Email Subject"

def sendUpdateNotifictionMail(userId, body_data):
    


# Create a MIMEMultipart object for the email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Update the email body
body = "This is the updated content of the email."
msg.attach(MIMEText(body, 'plain'))