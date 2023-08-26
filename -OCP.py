class Notifier:
    def __init__(self, user, message):
        self.user = user
        self.message = message
    
    def Notify (self):
        raise NotImplementedError
    
class EmailNotifier(Notifier):
    def Notify(self):
        print(f"Sending email to {self.user.email}")

class SMSNotifier(Notifier):
    def Notify(self):
        print(f"Sending SMS to {self.user.sms}")