import unittest
from account import *


class AccountTests(unittest.TestCase):
    def test_init(self):
        account = Account("John")
        self.assertEqual(account.get_name(), "John")
        self.assertEqual(account.get_balance(), 0)

    def test_deposit(self):
        account = Account("John")
        self.assertTrue(account.deposit(100))  
        self.assertEqual(account.get_balance(), 100)  
        self.assertFalse(account.deposit(-50))  
        self.assertEqual(account.get_balance(), 100)  

    def test_withdraw(self):
        account = Account("John")
        account.deposit(100) 
        self.assertTrue(account.withdraw(50))  
        self.assertEqual(account.get_balance(), 50) 
        self.assertFalse(account.withdraw(-30))  
        self.assertEqual(account.get_balance(), 50)  
        self.assertFalse(account.withdraw(100)) 
        self.assertEqual(account.get_balance(), 50) 

if __name__ == '__main__':
    unittest.main()
