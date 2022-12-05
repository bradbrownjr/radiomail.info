#!/usr/bin/env python3

# Import required libraries
# Uses imap-tools from https://github.com/ikvk/imap_tools
import os
import config as cfg
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
  import imap_tools
except ImportError:
  print ("Trying to Install required module: imap_tools\n")
  os.system('python3 -m pip install imap_tools')
from imap_tools import MailBox, AND

# Import modules


# About
def about(request):
    result = """Get Radio Info
--------------
Retrieve information from the Internet
from locations off grid via radio-based
email, using Winlink, APRS, or packet
radio!

Commands are sent in the subject, and
the request in the body of a message.

Enter the following commands for help:
* Catalog - List of commands
* Help {command} - Get help on a
  specific command
"""
    return result
info = about

# Test App
def test(request):
    result = "Test message was received.\r\n\r\nYour request:\r\n" + request
    return result

# Send reply
def respond(result):
    reply = MIMEMultipart()
    reply['From'] = cfg.imap_username
    reply['To'] = msg.from_
    reply['Subject'] = 're: '+msg.subject
    reply.attach(MIMEText(result, 'plain'))
    server = smtplib.SMTP(cfg.imap_servername)
    server.login(cfg.imap_username, cfg.imap_password)
    server.sendmail(cfg.imap_username,msg.from_,reply.as_string())
    return

# Poll messages
def main():
    # Define global variables used in other functions
    global msg

    # Log into mailbox
    with MailBox(cfg.imap_servername).login(cfg.imap_username, cfg.imap_password) as mailbox:
    
        # Fetch mail
        for msg in mailbox.fetch(AND(seen=False)):
    
            # Log the inquiry (to screen atm)
            print(msg.date, msg.from_, msg.subject, len(msg.text or msg.html))
    
            # Run function based on subject name, and then reply
            # e.g.: respond(test(msg.text))
            try:
                respond(eval(msg.subject.lower()+'(msg.text)'))
            except:
                print("Not in scope: " + msg.subject.lower())
                respond("Request not in scope, sorry!")
            else:
                print("In scope: " + msg.subject.lower())
                respond(eval(msg.subject.lower()+'(msg.text)'))
    return

# Main
if __name__ == '__main__':
    main()
