import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

class EmailService:
    # login information of a microsoft hotmail account you want to send the service emails from
    TRY_TO_SEND_EMAIL = False
    SENDER_EMAIL = "%%% ACCOUNT EMAIL ADDRESS %%%"
    SENDER_PASSWORD = "%%% ACCOUNT PASSWORD %%%"

    def sendUpdateNotifictionMail(self, toEmailAddress, eventRegistrationData):
        msg = MIMEMultipart()
        msg['From'] = self.SENDER_EMAIL
        msg['To'] = toEmailAddress
        msg['Subject'] = "Der Status ihrer event anmeldung wurde aktualisiert"

        body = "ihre neuen daten: \n"

        for key, value in eventRegistrationData[0].items():
            body += str(key) + ": " + str(value) + "\n"

        body += "\n"
        body += "Mit freundlichen Grüßen"
        body += "\n"
        body += "ihr GSO Team"

        msg.attach(MIMEText(body, 'plain'))
        if self.TRY_TO_SEND_EMAIL:
            self.sendEmail(msg)

    def sendRegistrationNoticeMail(self, toEmailAddress:str, companyName:str):
        msg = MIMEMultipart()
        msg['From'] = self.SENDER_EMAIL
        msg['To'] = toEmailAddress
        msg['Subject'] = "Ihre Registrierung war erfolgreich."

        body = "Hallo " + companyName + ", \n"
        body += "\n"

        body += "hiermit bestätigen wir Ihnen Ihre Registrierung. Sie können sich jetzt mit Ihrem Konto anmelden."

        body += "\n"
        body += "Mit freundlichen Grüßen"
        body += "\n"
        body += "ihr GSO Team"

        msg.attach(MIMEText(body, 'plain'))
        if self.TRY_TO_SEND_EMAIL:
            self.sendEmail(msg)



    def _sendEmail(self, email:MIMEText):
        smtp_server = "imap-mail.outlook.com"
        port = 465
        SSL_context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=SSL_context) as server:  # Using localhost (no actual server)
                server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
