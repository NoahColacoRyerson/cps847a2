
import unittest
from package import bank
from package import currency
C = currency.Currencies #Make C refer to the Currencies enumeration to make testing easier 

class TestBank(unittest.TestCase):
    def test_a(self):
        #Test the first initial given test case

        #Setup
        Customer234 = bank.AceBank()
        Customer234.create_account("0808",1000.00)

        #Actions
        Customer234.deposit_funds("0808",500.00, C.USD)
        Customer234.withdraw_funds("0808",100.00, C.CAD)

        #Check if expected balance is equal to actual balance
        self.assertEqual(Customer234.get_balance("0808"),1650.00)
    
    def test_b(self):
        #Test the second initial given test case

        #Setup
        Customer756 = bank.AceBank()
        Customer756.create_account("0903",100.00)
        Customer756.create_account("0875",6000.00)

        #Actions
        Customer756.withdraw_funds("0875",700.00, C.USD)
        Customer756.deposit_funds("0903",2500.00, C.EUR)
        Customer756.transfer_funds("0875","0903", 1100.00)        

        #Check if the expected balances are equal to the actual balances
        self.assertEqual((Customer756.get_balance("0875"),Customer756.get_balance("0903")),(6050.00,4000.00))
        
    def test_c(self):
        #Test the first case which I created

        #Setup
        Customer491 = bank.AceBank()
        Customer491.create_account("0381",800.31)
        Customer491.create_account("1832",200.12)

        #Actions
        Customer491.withdraw_funds("0381",500.16, C.CAD)
        Customer491.transfer_funds("1832","0381", 300.05)
        Customer491.deposit_funds("0381",500.50, C.EUR)

        #Check if the expected balances are equal to the actual balances
        self.assertEqual((Customer491.get_balance("0381"),Customer491.get_balance("1832")),(1001.10,500.17))

    def test_d(self):
        #Test the second case which I created

        #Setup
        Customer175 = bank.AceBank()
        Customer175.create_account("3472",200.02)

        #Actions
        Customer175.withdraw_funds("3472",100.01, C.EUR)

        #Check if the expected balances are equal to the actual balances
        self.assertEqual(Customer175.get_balance("3472"),0.00)
    

if __name__ == '__main__':
    unittest.main()
