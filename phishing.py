#!/usr/bin/env python3

from guerrillamail import GuerrillaMailSession
import smtplib
import sys
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders


session = GuerrillaMailSession()
#_from = session.get_session_state()['email_address'] #Get current email from seassion

try:
    _from = sys.argv[1]
    _to = sys.argv[2]
    _job_title = sys.argv[3]

except:
    print("Enter From and To and Job Title arguments")
    exit()

if not _from or not _to:
    print("From or To argument invalid.")
    print(_from)
    print(_to)
    exit()

_msg = ""
_msg += "Attention sir/madam.\nSince you are a " + _job_title + ", we got a great deal for you!\n"
what = ""


if _job_title == "doctor":
    what = "MRI Machine"
    _msg += "With just 99$ you can buy the latest " + what + "!\nEnter this link to learn more: example.com."
elif _job_title == "unemployed":
    what = "laptop"
    _msg += "With just 99$ you can buy the latest " + what + "!\nEnter this link to learn more: example.com."
    

msg = MIMEMultipart()
#msg['Subject'] = "Subject" 
#msg['From'] = _from
#msg['To'] = ', ' + _to

msg.attach(MIMEText(_msg))

part = MIMEBase('application', "octet-stream")
part.set_payload(open("attach_create.py", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="not_a_virtus.py"')

msg.attach(part)

#server = smtplib.SMTP("guerrillamail.com")
server = smtplib.SMTP("localhost")
server.sendmail(_from, _to, msg.as_string())
'''
for i in range(100):
    server.sendmail(_from, _to, msg.as_string())
    print("From = " + _from)
    print("To = " + _to)
    print("Email sent!")
'''
print("Email sent!")
server.quit()