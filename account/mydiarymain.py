import re


from diaries import Diaries
from entry import Entry



class DiaryMain:
    diaries = Diaries()

    def __init__(self, name):
        self.name = name
        self.username = 0


    def menu(self):
        try:
            self.output("========== Welcome to my diary ===========")
            self.output("")
            option = self.inputFunction("Enter 1 to continue: ")
            if option == "1":
                self.mainMenu()
            else:
                self.menu()
        except(KeyboardInterrupt, ValueError):
            self.output("wrong process")
            self.menu()

    def mainMenu(self):
        self.output("  olofofo you done land")
        self.output("""
        1. Register
        2. login
        3. Delete
        4.exit
        """)
        option = self.inputFunction("Enter Main Menu number: ")
        match option:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                self.delete()
            case "4":
                self.exit()
            case _:
                self.menu()

    def register(self):
        try:
            self.output("")
            self.username = self.inputFunction("Enter a username: ")
            self.nameValidation(self.username)
            password = self.inputFunction("Enter a password: ")
            self.passwordValidation(password)
            self.diaries.add_diary(self.username, password)
            self.output("username and password  created successfully")
            self.output("")
            self.mainMenu()
        except Exception as e:
            self.output(e)
            self.register()

    def login(self):
        try:
            name = self.inputFunction("Enter your username to login: ")
            password = self.inputFunction("Enter your password to login: ")
            self.diaries.find_by_username(name).unlock_diary(password)
            self.entryMenu()
        except Exception as e:
            self.output(e)
            self.mainMenu()

    def entryMenu(self):
        self.output("""\n
        Welcome finally amibo
        1. CreateEntry
        2. FindEntry
        3. UpdateEntry
        4.DeleteEntry
        5.Logout
        """)
        option = self.inputFunction("enter any of the MenuNumber: ")
        match option:
            case "1":
                self.createEntry()
            case "2":
                self.findEntry()
            case "3":
                self.updateEntry()
            case "4":
                self.deleteEntry()
            case "5":
                self.logout()
            case _:
                self.entryMenu()

    def createEntry(self):
        self.output("""\n
        1.Title and Body
        2.back to entry menu
        """)
        option = self.inputFunction("Enter any of the entry number: ")
        match option:
            case "1":
                self.titlesAndBody()
            case "2":
                self.entryMenu()
            case _:
                self.createEntry()

    def titlesAndBody(self):

        try:
            title = self.inputFunction("\n Enter title: ")
            self.titleValidation(title)
            body = self.inputFunction("\n Enter body: ")
            generate = self.diaries.find_by_username(self.username).entry_creation(title, body)
            Entry(int(generate), title, body)
            self.output("title and body successfully created")
            self.output("\n Title: " + title + "\n Body: " + body)
            self.output("your entry id is")
            self.output(int(generate))
            self.entryMenu()
        except Exception as e:
            self.output(e)
            self.titlesAndBody()

    def logout(self):
        self.output(""" \n are you sure you want to logout""")
        option = self.inputFunction("""
        1. yes
        2. no
        """)
        if option == "1":
            self.mainMenu()
        elif option == "2":
            self.entryMenu()
        else:
            self.logout()

    def findEntry(self):
        try:
            enterId = self.inputFunction("\nEnter id to find entry: ")
            info = self.diaries.find_by_username(self.username).can_find_entry(int(enterId)).get_entries()
            self.output("Entry found successfully")
            self.output(info)
            self.entryMenu()
        except Exception as e:
            self.output(e)
            self.findEntry()

    def updateEntry(self):
        try:
            enterId = self.inputFunction("Enter id to find: ")
            myEntry = self.diaries.find_by_username(self.username).can_find_entry(int(enterId)).get_entries()
            self.output("Entry found successfully")
            self.output(myEntry)
            title = self.inputFunction("Enter title to update: ")
            self.titleValidation(title)
            body = self.inputFunction("Enter body to update: ")
            self.diaries.find_by_username(self.username).update_entry(int(enterId), title, body)
            get = self.diaries.find_by_username(self.username).can_find_entry(int(enterId)).get_entries()
            self.output("Entry updated successfully")
            self.output(get)
            self.entryMenu()
        except Exception as e:
            self.output(e)
            self.updateEntry()

    def deleteEntry(self):
        try:
            deleteId = self.inputFunction("Enter id to delete: ")
            get = self.diaries.find_by_username(self.username).can_find_entry(int(deleteId)).get_entries()
            self.output(get + "\n" + "deletion in process")
            self.diaries.find_by_username(self.username).entry_deletion(deleteId)
            self.output("deleted successfully")
            self.entryMenu()
        except Exception as e:
            self.output(e)
            self.delete()

    def delete(self):
        self.output("""
        Are you sure you want to delete account
        1.yes
        2.no
        """)
        option = self.inputFunction("choose option: ")
        match option:
            case "1":
                self.delete1()
            case "2":
                self.mainMenu()
            case _:
                self.mainMenu()

    def delete1(self):
        try:
            name = self.inputFunction("input name to delete: ")
            password = self.inputFunction("enter your password: ")
            self.diaries.i_can_delete(name, password)
            self.output("diary account deleted successfully")
            self.mainMenu()
        except Exception as e:
            self.output(e)
            self.delete()

    def output(self, output):
        print(output)

    def inputFunction(self, enter):
        entry = input(enter)
        return entry

    def nameValidation(self, name):
        match = r'^[a-zA-Z]+$'
        if not re.search(match, name):
            self.output("name must contain only alphabet")
            self.register()

    def titleValidation(self,name):
        match = r'^[a-zA-Z" "]+$'
        if not re.search(match, name):
            self.output("name must contain only alphabet")
            self.updateEntry()

    def passwordValidation(self, name):
        match = r'^[a-zA-Z0-9]{8,12}$'
        if not re.search(match, name):
            self.output("password must contain must be between the range of 8 and 12")
            self.register()

    def exit(self):
        exit()

    def main(self):
        self.menu()


if __name__ == "__main__":
    diary = DiaryMain("my diary")
    diary.main()
