import smtplib  #conn b/w system to email
from email.mime.multipart import MIMEMultipart #chose particular path(email)
from email.mime.text import MIMEText
import random

def send_otp(data):
    otp= random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587    #587 free port maintaned by gmail server

    username = "chandrikachavva5@gmail.com"
    password = "jdlg nmbg kbwp vrak"

    from_email = "chandrikachavva5@gmail.com"
    to_email = data
    subject = "OTP Validation"
    body = f"OTP for Validation is {otp} \n Thank You."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))   #body sent only in plain text

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()  #server starts
    server.login(username,password)
    server.send_message(msg)
    server.quit()

    return otp

