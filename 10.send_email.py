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
#     smtp.login("1716510074@kit.ac.in","pv@8174812109")
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
server.starttls()

server.login('1716510074@kit.ac.in','pv@1716510074')

server.sendmail('1716510074@kit.ac.in','piyushv080@gmail.com','Mail using py')
print('piyush Mail sent')