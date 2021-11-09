
class Class:
    def __init__(self, id, course_id, period, zoom_id):
        self.__id = id
        self.__course_id = course_id
        self.__period = period
        self.__zoom_id = zoom_id

    def get_id(self):
        return self.__id

    def get_course_id(self):
        return self.__course_id

    def get_period(self):
        return self.__period

    def get_zoom_id(self):
        return self.__zoom_id

    def set_id(self, id):
        self.__id = id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_period(self, period):
        self.__period = period

    def set_zoom_id(self, zoom_id):
        self.__zoom_id = zoom_id