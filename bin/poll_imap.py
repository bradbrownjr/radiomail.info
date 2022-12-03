#!/usr/bin/env python3

# Import required libraries
# Uses imap-tools from https://github.com/ikvk/imap_tools
import os
import config as cfg

try:
  import imap_tools
except ImportError:
  print ("Trying to Install required module: imap_tools\n")
  os.system('python3 -m pip install imap_tools')
from imap_tools import MailBox, AND, A

# Test App
def test():
    result = "Test message was received.\n" + msg.text
    return result

# Send reply
def respond(response):
    print(response)  # Validating receipt of response for testing
    return

# Poll messages
with MailBox(cfg.imap_servername).login(cfg.imap_username, cfg.imap_password) as mailbox:
    for msg in mailbox.fetch(): #.fetch(AND(seen=False)):
        print("Payload", msg.date, msg.subject, len(msg.text or msg.html))
        respond(eval(msg.subject+'()'))
