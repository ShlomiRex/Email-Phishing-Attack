Shlomi 318643640



https://www.guerrillamail.com/

Linux

TODO: INSERT IN THIS LINE THE LOCAL IP

## Requirements

Python3, Python libraries(below), Services (below)

## Running environment

Linux Ubuntu 18.04

## Services

postfix, bind9

## Python Libraries

scapy, smtplib, guerrillamail, email, getpass, os, requests, sys, email

## How to run

1.  First send a phishing email by typing:

```
sudo python3 phishing.py <from> <to> <job title>
```

2.  I am using guerrillamail. Go to the website and get email address. 
3.  Example phishing attack:

```
sudo python3 phishing.py totaly_not_scammer@gmail.com i72dmh+f0fu6yw7b4mmg@sharklasers.com doctor
```

You should see the email sent to your mailbox.

## Hard coded values

1.  Localhost - for local SMTP server.
2.  8.8.8.8 - used for dns server (the attacker's IP address. Need to change that to real IP address.)
3.  [Public IP API website](https://api.ipify.org)