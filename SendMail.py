from Package import *
from Speak import *

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mahendragandham730@gmail.com', '12345678')
    server.sendmail('mahendragandham730@gmail.com', to, content)
    server.close()
