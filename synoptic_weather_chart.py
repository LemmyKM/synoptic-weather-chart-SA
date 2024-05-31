import smtplib, ssl
import requests
import os
from email.message import EmailMessage

def send_email():
    message = EmailMessage()

    message["From"] = 'your email address'
    message["To"] =  'your email address'
    message["Subject"] = 'Synoptic Chart SA'

    message.set_content("Latest synoptic chart as attachment.")

    with open('synoptic_latest.gif', 'rb') as attachment:
        message.add_attachment(
            attachment.read(), maintype='image', subtype='gif')

    context = ssl.create_default_context() 
    with smtplib.SMTP('your SMTP server address', 'server port') as server:
        server.ehlo()
        server.starttls(context=context) 
        server.login('login address for your email account', 'password for your email account')
        server.send_message(message)


url = 'https://www.weathersa.co.za/images/data/specialised/ma_sy.gif'
response = requests.get(url, stream=True) 

with open('synoptic_latest.gif', mode='wb') as file:
    for chunk in response.iter_content(chunk_size=100 * 1024):
        file.write(chunk)

send_email()
os.remove('synoptic_latest.gif')