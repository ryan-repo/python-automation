import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user="ryandnot@gmail.com"
email_pasword="Tanzil@7890"
subject="subscription activated"

with open('emails.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        text="hello "+line[1]+" you won "+ line[2]+" Lottery price"
        #print(text)

        email_send=line[0]
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))
        text=msg.as_string()

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_user, email_pasword)
        server.sendmail(email_user, email_send, text)

        server.quit()
