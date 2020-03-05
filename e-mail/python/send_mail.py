#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import smtplib
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
me = "XXXXXX@example.com"  # 送信元メールアドレス
you = "YYYYY@example.com"  # 送信先メールアドレス
 
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "タイトル"
msg['From'] = me
msg['To'] = you
 
# Create the body of the message (a plain-text and an HTML version).
text = "This is a test message.\nText and html.\nfor Text"
html = """\
<html>
  <head></head>
  <body>
    <p style='font-size:16.0pt;font-family:游ゴシック'>This is a test message.</p>
    <p>Text and HTML</p>
    <p>for HTML</p>
  </body>
</html>
"""
 
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
 
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
 
# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()