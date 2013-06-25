import smtplib

class Sms(object):
    username = ""
    password = ""
    phone = ""
    domain = ""

    def __init__(self, username, password, phone, domain):
        """
        Initializes the Sms object. Phone should be a string.
        """
        self.username = username
        self.password = password
        self.phone = phone
        self.domain = domain

    def get_email(self):
        return self.phone + "@" + self.domain

    def send(self, msg):  
        # The actual mail send  
        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.starttls()  
        server.login(self.username, self.password)  
        server.sendmail(self.username, self.get_email(), msg)  
        server.quit()