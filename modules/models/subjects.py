

class Subjects:
    def __init__(self, id, name, period):
        self.__id = id
        self.__name = name
        self.__period = period

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_period(self):
        return self.__period

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_period(self, period):
        self.__period = period