from account import Account

import random


class Bank:

    def __init__(self, bank: str):
        self.__bank = bank
        self.__lists_account = []

    def can_register(self, first_name, second_name, pin):
        fullname = first_name + " " + second_name
        generate = self.generate_account_number()
        new_account = Account(generate, fullname, pin)
        self.__lists_account.append(new_account)
        return generate


    def generate_account_number(self):
        return random.randint(6, 10000000000).__str__()
        # return str(len(self.__lists_account) + 1)

    def can_find_out(self, account_number):
        for account in self.__lists_account:
            if account.I_can_get_account_number() == account_number:
                return account
        else:
            raise ValueError("wrong account")

    def i_can_deposit(self, amount, account_number):
        if amount > 0:
            self.can_find_out(account_number).i_can_deposit(amount)

    def check_balance(self, account_number, pin):
        return self.can_find_out(account_number).check_balance(pin)

    def can_withdraw(self, amount, account_number, pin):

        self.can_find_out(account_number).i_can_withdraw(amount, pin)

    def can_make_transfer(self, amount: int, from_account: str, to_account: str, pin: str):
        account_sender = self.can_find_out(str(from_account))
        account_sender.i_can_withdraw(amount, pin)
        account_reciever = self.can_find_out(str(to_account))
        account_reciever.i_can_deposit(int(amount))
