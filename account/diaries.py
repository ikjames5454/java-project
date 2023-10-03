from diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries_of_diary = []


    def add_diary(self,username,password):
        diary_adding = Diary(username, password)
        self.__diaries_of_diary.append(diary_adding)

    def find_by_username(self, username):
        for diary in self.__diaries_of_diary:
            if diary.get_diary_username() == username:
                return diary
        raise AttributeError("wrong username")

    def i_can_delete(self, username, password):
        diary = self.find_by_username(username)
        if diary.get_diary_password() == password:
            self.__diaries_of_diary.remove(diary)
        else:
            raise AttributeError("wrong pin")
        # if self.find_by_username(username) is not None:
        #     self.__diaries_of_diary.remove(self.find_by_username(username))
