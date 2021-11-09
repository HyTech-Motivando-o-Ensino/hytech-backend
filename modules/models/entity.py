class Entity:
    def __init__(self, id, name, photo=None):
        self.__id = id
        self.__name = name
        self.__photo = None

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_photo(self):
        return self.__photo
    
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_photo(self, photo):
        self.__photo = photo
