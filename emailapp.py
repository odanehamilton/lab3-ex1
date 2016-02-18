import smtplib

fromaddr = 'odane.hamilton@gmail.com'
fromname = 'Odane'
toname = 'George'
subject = 'Test email'
msg = 'This is the test message to be sent'
toaddr  = 'me@odanephamilton.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'odane.hamilton@gmail.com'
password = 'xcncejeiwtjbbqzg'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()