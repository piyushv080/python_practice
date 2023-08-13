#send email to me
from http import server
import smtplib

server = smtplib.SMTP('smtp.google.com','587')
# EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
# EMAIL_PASSWORD = os.environ.get('PASSWORD')


# #using with statement
# with smtplib.SMTP('smtp.google.com',587) as smtp:
#     #encrpyting 
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login("user_email_id","password")
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
server.starttls()

server.login('email','pass')

server.sendmail('email1','email2','Mail using py')
print('piyush Mail sent')
