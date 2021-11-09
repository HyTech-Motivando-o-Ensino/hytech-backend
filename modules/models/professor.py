from entity import Entity

class Professor(Entity):
    
    def __init__(self, id, name, photo, contact, email, slack, whatsapp):
        super().__init__(id, name, photo)
        self.__email = email
        self.__slack = slack
        self.__whatsapp = whatsapp
        self.__contact = contact

    def get_email(self):
        return self.__email
    
    def get_slack(self):
        return self.__slack

    def get_whatsapp(self):
        return self.__whatsapp

    def get_contact(self):
        return self.__contact

    def set_email(self, email):
        self.__email = email

    def set_slack(self, slack):
        self.__slack = slack

    def set_whatsapp(self, whatsapp):
        self.__whatsapp = whatsapp

    def set_contact(self, contact):
        self.__contact = contact
