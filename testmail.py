# Test 
import smtplib, ssl

port = 587  # For starttls
smtp_server = "serv15.avernis.de"

sender_email = "pagingcalls@hampager.de"
receiver_email = "receiver@mail.com"
username = "pagingcalls@hampager.de"
password = "CHANGEME"
message = """\
From: DAPNET Paging Calls <pagingcalls@hampager.de>
To: DL1ABC <receiver@mail.com>
Subject: DAPNET paging call for you

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, message)
