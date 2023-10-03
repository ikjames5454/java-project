from _datetime import datetime

class Entry:
    def __init__(self, ids, title, body):
        self.__ids = ids
        self.__title = title
        self.__body = body
        self.__date_created = datetime

    def set_id(self, ids):
        self.__ids = ids

    def get_id(self):
        return self.__ids

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_body(self,body):
        self.__body = body

    def get_body(self):
        return self.__body

    def get_entry(self):
        return self.__title + self.__body

    def get_entries(self):
        return "Title: " + self.__title + "\n" + "Body: " + self.__body
