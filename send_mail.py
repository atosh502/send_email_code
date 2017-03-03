# import the smtplib module to send emails
import smtplib

your_email = input('Enter you email: ')
your_password = input('Enter your password: ')
destination_email = input('Enter destination email: ')
subject = input('Enter the subject of email: ')
message = input('Enter the message you want to send: ')

# connect to the gmail server with an SMTP object  
smtpObject = smtplib.SMTP('smtp.gmail.com', 587);
# The SMTP object created represents a connection to an SMTP mail server
# if the smtplib.SMTP() call is not successful, your SMTP server might not support TLS on port 587, 
# in such a case create an SMTP object using smtplib.SMTP_SSL() at port 465 instead

# the method ehlo() or "say hello" is the first step in SMTP and is important for establishing connection to the server
smtpObject = smtplib.ehlo()
# a return value of 250 means the greeting is  successful

# enables encryption for your connection
smtpObject.starttls()
# the 220 return value tells you that the server is ready

smtpObject.login(your_email, your_password)
# a return value of 235 means successful
# you might get an error if you have login through less secure apps turned off in your
# or an error due to gmail application-specific passwords

smtpObject.sendmail(destination_email, your_email, 'Subject: ' + subject + '\n' + message)
# function sendmail takes destination and sender email address; also it has a message that starts with 
# 'Subject: TEST\n.....' to indicate the subject of the email
# the return type of sendmail is a dictionary for recipient for whom email delivery failed
# an empty dictionary means all recipients were successfully sent the email

# finally disconnect from the SMTP server
smtpObject.quit()

