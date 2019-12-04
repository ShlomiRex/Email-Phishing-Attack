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
from bs4 import BeautifulSoup

session = GuerrillaMailSession()
# Gets temporarly email from guerrila mail
_from = session.get_session_state()['email_address'] #Get current email from seassion

argc = len(sys.argv)
print("Argument count: " + str(argc))
if argc <= 3:
    print("You must enter 3 or 4 arguments, you entered: " + str(argc))
    print("You must enter: Username, Mail Service Name, Job Title")
    exit()
elif argc >= 4:
    _username = sys.argv[1]
    _mail_service_name = sys.argv[2]
    _job_title = sys.argv[3]

    _to = _username + "@" + _mail_service_name

    if argc == 5:
        html_file_path = sys.argv[4]
        html_file = open(html_file_path, "r")

        source_code = html_file.read()
        soup = BeautifulSoup(source_code, 'html.parser')

        _title = soup.title.string
        _msg = soup.content.string
        _name = soup.find('name').string
        _to = soup.receiver.string
        _job_title = soup.receiver.string

        #print(_title, _content, _name, _receiver, _job)
    elif argc > 5:
        print("Argument count must be 3 or 4")
        exit()
try:
    # Check if defined
    _msg
except:
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
#msg['From'] = "a@gmail.com"
#msg['To'] = ', ' + "b@gmail.com"

msg.attach(MIMEText(_msg))

part = MIMEBase('application', "octet-stream")
part.set_payload(open("attach_create.py", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="not_a_virtus.py"')

msg.attach(part)

#server = smtplib.SMTP("guerrillamail.com")
server = smtplib.SMTP("localhost")
print("From = " + _from)
print("To = " + _to)
#print("Message = " + msg.as_string())
server.sendmail(_from, _to, msg.as_string())
print("Email sent!")
server.quit()