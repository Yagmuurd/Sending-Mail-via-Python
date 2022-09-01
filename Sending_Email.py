#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:40:26 2022

@author: yagmur
"""

from email.message import EmailMessage #set the variables from, to, subject and body
import ssl #to secure the data in the mail
import smtplib #to send the mail

sender = 'senderaddress@gmail.com'
password = 'password'
reciever = 'recieveraddress@gmail.com'


subject = 'Subject of the Mail'
body = """

This message is send through using Python.

"""

em = EmailMessage()
em['From'] = sender
em['To'] = reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

#since the mail we send is a gmail account first part contains gmail server information
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, reciever, em.as_string())