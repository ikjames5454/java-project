import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.accounts = Account("1234", "james", "1237")


    def test_i_can_deposit(self):
        self.accounts.i_can_deposit(5000)
        self.assertEqual(5000, self.accounts.check_balance("1237"))
        self.accounts.i_can_deposit(500)
        self.accounts.i_can_deposit(1000)
        self.assertEqual(6500, self.accounts.check_balance("1237"))


    def test_i_can_withdraw(self):
        self.accounts.i_can_deposit(5000)
        self.assertEqual(5000, self.accounts.check_balance("1237"))
        self.accounts.i_can_withdraw(3000, "1237")
        self.assertEqual(2000, self.accounts.check_balance("1237"))

    def test_that_pin_is_validated(self):
        self.accounts.i_can_deposit(6000)
        self.assertEqual(6000, self.accounts.check_balance("1237"))


    def test_that_i_can_change_pin(self):
        self.accounts.i_can_deposit(6000)
        self.assertEqual(6000, self.accounts.check_balance("1237"))
        self.accounts.i_can_withdraw(3000,"1237")
        self.accounts.i_can_change_pin("1237","3456")
        self.assertEqual(3000,self.accounts.check_balance("3456"))
        self.accounts.i_can_withdraw(2000, "3456")
        self.assertEqual(1000, self.accounts.check_balance("3456"))
        self.accounts.i_can_deposit(3000)
        self.assertEqual(4000, self.accounts.check_balance("3456"))


    def test_that_i_get_account_number(self):
        self.assertTrue("1234", self.accounts.I_can_get_account_number())


