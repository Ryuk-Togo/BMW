 #!python

'''to save all attached image files in a mailbox'''


import email
import os
from email import policy
from email.parser import BytesParser
import csv
from datetime import datetime

class MailLoad(object):
    
    email_msg = None
    subject = None
    receive_date = None
    to_address = None
    cc_address = None
    from_address = None
    body = None
    attach_file_list = []

    def __init__(self, mail_file_path):
        self.perse_eml(mail_file_path)
        self.get_email_data(self.email_msg)
        None

    def perse_eml(self,file_path):
        try:
            with open(file_path, 'rb') as f:
                self.email_msg = BytesParser(policy=policy.default).parse(f)
        except(e):
            print(e)
    
    def get_email_data(self,email_msg):
        self.from_address = email_msg.get('From', '')
        self.to_address = email_msg.get('To', '')
        self.cc_address = email_msg.get('Cc', '')
        # to_addresses = '/'.join([addr.strip() for addr in to_addresses.split(',')])  # 複数の宛先を '/' 区切りにします
        self.subject = email_msg.get('Subject', '')
        self.body = self.get_email_text(email_msg)
        self.receive_date = email_msg.get('Date', '')


    def get_email_text(self,email_msg):
        text = ""
        if email_msg.is_multipart():
            for part in email_msg.walk():
                if part.get_content_type() == 'text/plain':
                    charset = part.get_content_charset() or 'utf-8'
                    text = part.get_payload(decode=True).decode(charset, errors='replace')
                    break
                if part.get_content_type() == 'text/html':
                    charset = part.get_content_charset() or 'utf-8'
                    text = part.get_payload(decode=True).decode(charset, errors='replace')

        else:
            if email_msg.get_content_type() == 'text/plain':
                charset = email_msg.get_content_charset() or 'utf-8'
                text = email_msg.get_payload(decode=True).decode(charset, errors='replace')
            elif email_msg.get_content_type() == 'text/html':
                charset = email_msg.get_content_charset() or 'utf-8'
                text = email_msg.get_payload(decode=True).decode(charset, errors='replace')
        return text