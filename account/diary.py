from entry import Entry
import random


class Diary:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name
        self.__password = password
        self.isLock = False
        self.__diary_list_entry = []

    def lock_diary(self):
        self.isLock = True

    def unlock_diary(self, password):
        self.validate_password(password)
        self.isLock = False

    def isLock(self):
        return self.isLock

    def validate_password(self, password):
        if self.__password == password:
            return password
        else:
            raise AttributeError("wrong password")


    def diary_entry(self):
        return random.randint(0, 10000)

        # return len(self.__diary_list_entry) + 1

    def can_find_entry(self, ids):
        for entry in self.__diary_list_entry:
            if entry.get_id() == int(ids):
                return entry
        return None
        # raise AttributeError("wrong entry")

    def entry_creation(self, title, body):
        generate = self.diary_entry()
        create_entry = Entry(generate, title, body)
        self.__diary_list_entry.append(create_entry)
        return generate

    def entry_deletion(self, ids):
        delete = self.can_find_entry(ids)
        if delete is not None:
            self.__diary_list_entry.remove(delete)
        else:
            raise AttributeError("entry is empty")

    def update_entry(self, ids, title, body):
        entry = self.can_find_entry(ids)
        entry.set_id(ids)
        entry.set_title(title)
        entry.set_body(body)

    def get_diary_username(self):
        return self.__user_name

    def get_diary_password(self):
        return self.__password
