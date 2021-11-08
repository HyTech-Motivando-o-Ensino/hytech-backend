from entity import Entity
from status_enum import Status

class Message:
    def __init__(self, contents, from_, to, status, timestamp):
        self.__contents = contents
        self.__from = from_
        self.__to = to
        self.__status = status
        self.__timestamp = timestamp

    def get_contents(self):
        return self.__contents

    def get_from(self):
        return self.__from
    
    def get_to(self):
        return self.__to
    
    def get_status(self):
        return self.__status
    
    def get_timestamp(self):
        return self.__timestamp
    
    def set_contents(self, contents):
        self.__contents = contents

    def set_contents(self, to_entity):
        self.__to = to_entity

    def set_from(self, from_entity):
        self.__from = from_entity

    def set_status(self, status):
        if status == 0:
            self.__status = Status.SENDING
        elif status == 1:
            self.__status = Status.SENT
        elif status == 2:
            self.__status = Status.ERROR

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp