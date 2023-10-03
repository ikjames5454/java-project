import unittest
from bank import Bank
from account import Account


class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("UBA")


    def test_i_can_register(self):
        self.bank.can_register("ikenna","james","1234")
        self.assertEqual(Account("1","ikenna james","1234").I_can_get_account(),self.bank.can_find_out("1").I_can_get_account())
        self.bank.can_register("harry", "nwaogwugwu", "5454")
        self.assertEqual(Account("2", "harry nwaogwugwu", "5454").I_can_get_account(),self.bank.can_find_out("2").I_can_get_account())

    def test_i_can_deposit(self):
        self.bank.can_register("ikenna", "james", "1234")
        self.assertEqual(Account("1", "ikenna james", "1234").I_can_get_account(),self.bank.can_find_out("1").I_can_get_account())
        self.bank.i_can_deposit(5000,"1")
        self.assertEqual(5000,self.bank.check_balance("1","1234"))
        self.bank.i_can_deposit(-5000, "1")
        self.assertEqual(5000, self.bank.check_balance("1", "1234"))


    def  test_i_can_withdraw(self):
        self.bank.can_register("ikenna", "james", "1234")
        self.assertEqual(Account("1", "ikenna james", "1234").I_can_get_account(),self.bank.can_find_out("1").I_can_get_account())
        self.bank.i_can_deposit(100000, "1")
        self.assertEqual(100000, self.bank.check_balance("1", "1234"))
        self.bank.can_withdraw( 50000,"1", "1234")
        self.assertEqual(50000, self.bank.check_balance("1", "1234"))


    def test_i_can_transfer_from_account_to_transfer(self):
        self.bank.can_register("ikenna", "james", "1234")
        self.bank.can_register("harry", "nwaogwugwu", "5454")
        self.assertEqual(Account("1", "ikenna james", "1234").I_can_get_account(),self.bank.can_find_out("1").I_can_get_account())
        self.assertEqual(Account("2", "harry nwaogwugwu", "5454").I_can_get_account(),self.bank.can_find_out("2").I_can_get_account())
        self.bank.i_can_deposit(10000, "1")
        self.assertEqual(10000, self.bank.check_balance("1", "1234"))
        self.bank.can_make_transfer(6000,"1","2","1234")
        self.assertEqual(4000,self.bank.check_balance("1","1234"))
        self.assertEqual(6000,self.bank.check_balance("2","5454"))






