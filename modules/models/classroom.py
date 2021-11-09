class Classroom:
    def __init__(self, id, classroom_id, subject_id):
        self.__id = id
        self.__classroom_id = classroom_id
        self.__subject_id = subject_id

    def get_id(self):
        return self.__id

    def get_classroom_id(self):
        return self.__classroom_id

    def get_subject_id(self):
        return self.__subject_id

    def set_id(self, id):
        self.__id = id

    def set_classroom_id(self, classroom_id):
        self.__classroom_id = classroom_id

    def set_subject_id(self, subject_id):
        self.__subject_id = subject_id