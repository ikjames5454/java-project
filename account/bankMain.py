from bank import Bank
from account import Account


class BankMain:

    def __init__(self, name):
        self.name = name
        self.bank = Bank("UBA")
        self.userName = None
        self.myPassword = None

    def menu(self):
        try:
            self.output("   Welcome to verySpecial bank   ")
            inputName = self.inputFunction("\n" + "Enter one to continue: ")
            if inputName == "1":
                self.mainMenu()
            else:
                self.menu()
        except(KeyboardInterrupt, ValueError):
            self.output("wrong action")
            self.menu()

    def mainMenu(self):
        self.output(""" 
        1-> CreateUser
        2-> Login
        3-> exit
        """)
        option = self.inputFunction("choose any of the option: ")
        match option:
            case "1":
                self.createUser()
            case "2":
                self.login()
            case "3":
                self.exit()
            case _:
                self.mainMenu()

    def exit(self):
        self.output("""
           are you sure you want to exit: 
           1.yes
           2.no
           """)
        option = self.inputFunction("choose any of the option: ")
        match option:
            case "1":
                exit()
            case "2":
                self.mainMenu()
            case _:
                self.exit()

    def createUser(self):
        name = self.inputFunction("Enter a username: ")
        self.userName = name
        password = self.inputFunction("Enter a password: ")
        self.myPassword = password
        if len(password) >= 8:
            self.output("password and username created successfully")
            self.mainMenu()
            self.userName = name
            self.myPassword = password

        else:
            self.output("password mus be equal or greater than 8")
            self.createUser()

    def login(self):
        name = self.inputFunction("Enter your username: ")
        if name != self.userName:
            self.output("wrong username")
            self.login()
        else:
            self.login2()

    def login2(self):
        password = self.inputFunction("Enter your password: ")
        if password != self.myPassword:
            self.output("wrong password")
            self.login()
        else:
            self.bankMenu()

    def bankMenu(self):
        self.output("""Welcome extinguish customer
                1->Register
                2->FindAccount
                3->CheckBalance
                4->CanTransfer
                5->Deposit
                6->withdraw
                7->logout
                """)
        option = self.inputFunction("choose any of the option")
        match option:
            case "1":
                self.register()
            case "2":
                self.findAccount()
            case "3":
                self.checkBalance()
            case "4":
                self.canTransfer()
            case "5":
                self.deposit()
            case "6":
                self.withdraw()
            case "7":
                self.logout()
            case _:
                self.bankMenu()

    def register(self):
        try:
            firstName = self.inputFunction("enter your name to register: ")
            secondName = self.inputFunction("enter your second name: ")
            pin = self.inputFunction("enter a pin to register: ")
            fullname = firstName + " " + secondName
            register = self.bank.can_register(firstName,secondName,pin)
            Account(register,fullname,pin)
            self.output("account created successfully ")
            self.output("your account number is: " + str(register))
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.register()



    def findAccount(self):
        try:
            account = self.inputFunction("enter account number to find account: ")
            display = self.bank.can_find_out(account).I_can_get_account()
            self.output("account found successfully")
            self.output(display)
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.findAccount()

    def checkBalance(self):
        try:
            account = self.inputFunction("enter account number to check balance: ")
            pin = self.inputFunction("enter account pin to check balance: ")
            display = self.bank.check_balance(account,pin)
            self.output("your balance is: " + str(display))
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.checkBalance()


    def canTransfer(self):
        try:
            accountSender = self.inputFunction("enter the account of sender: ")
            amount = self.inputFunction("enter the amount to send: ")
            accountReceiver = self.inputFunction("enter the account of the receiver: ")
            pin = self.inputFunction("enter sender,s pin: ")
            self.bank.can_make_transfer(int(amount),accountSender,accountReceiver,pin)
            self.output(amount + " transferred successfully")
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.canTransfer()


    def deposit(self):
        try:
            account = self.inputFunction("enter your accountNumber to deposit: ")
            amount = self.inputFunction("enter amount you want to deposit: ")
            self.bank.i_can_deposit(int(amount),account)
            self.output(amount + " deposited successfully")
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.deposit()


    def withdraw(self):
        try:
            account = self.inputFunction("enter your accountNumber to withdraw: ")
            pin = self.inputFunction("enter your pin to withdraw: ")
            amount = self.inputFunction("enter the amount you want to withdraw: ")
            self.bank.can_withdraw(int(amount),account,pin)
            self.output(amount + " withdrew successfully")
            self.bankMenu()
        except Exception as e:
            self.output(e)
            self.deposit()


    def logout(self):
        self.output("""
          are you sure you want to logout
            1->yes
            2->no
            """)
        option = self.inputFunction("enter any of the option number")
        match option:
            case "1":
                self.mainMenu()
            case "2":
                self.bankMenu()
            case _:
                self.logout()

    @staticmethod
    def output(output):
        print(output)

    @staticmethod
    def inputFunction(enter):
        entry = input(enter)
        return entry

    def main(self):
        self.menu()


if __name__ == "__main__":
    bank = BankMain("My bank")
    bank.main()
