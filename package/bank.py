#Noah Colaco
#December 1, 2020

#import currency file which contains the currency enums
from package import currency

class AceBank:
    accounts = {} #'accounts' is a dictionary to store all the accounts of a particular customer
    
    '''
    Function Name: create_account
    Purpose: to create an account for a customer
    Parameters: account_number(str), balance(float)
    Return: None
    '''
    def create_account(self,account_number, balance):
        if balance >= 0:
            self.accounts[account_number] = float(balance) #Adds the account to the 'accounts' dictionary and cast the balance as a float
        else:
            print("Error, Balance must be $0 or more")

    '''
    Function Name: get_balance
    Purpose: to see the balance of the account
    Parameters: account_number(str)
    Return: balance(float)
    '''
    def get_balance(self, account_number):
        if account_number in self.accounts:
            return round(self.accounts.get(account_number),2) #Rounds the balance of the account to 2 decimal places then returns it
    
    '''
    Function Name: deposit_funds
    Purpose: to deposit money into an account
    Parameters: account_number(str), amount(float), currency(Currencies)
    Return: None
    '''
    def deposit_funds(self, account_number, amount, currency):
        if account_number in self.accounts:
            self.accounts[account_number] = self.accounts.get(account_number) + (amount*currency.value) #Updates the value in the dictionary where account_number is the key
    
    '''
    Function Name: withdraw_funds
    Purpose: to withdraw money from an account
    Parameters: account_number(str), amount(float), currency(Currencies)
    Return: None
    '''
    def withdraw_funds(self, account_number, amount, currency):
        if account_number in self.accounts and self.accounts.get(account_number) - (amount*(currency.value)) >= 0:
            self.accounts[account_number] = self.accounts.get(account_number) - (amount*currency.value) #Updates the value in the dictionary where account_number is the key
        else:
            print("Error, Amount to withdraw is too large")

    '''
    Function Name: transfer_funds
    Purpose: to transfer funds between accounts
    Parameters: incoming_account_number(str), outgoing_account_number(str), amount(float)
    Return: None
    '''
    def transfer_funds(self, incoming_account_number, outgoing_account_number, amount):
        if incoming_account_number in self.accounts and outgoing_account_number in self.accounts:
            if (self.accounts.get(outgoing_account_number) - amount) >= 0:
                self.accounts[outgoing_account_number] = self.accounts.get(outgoing_account_number) - amount #Updates the value in the dictionary where account_number is the key
                self.accounts[incoming_account_number] = self.accounts.get(incoming_account_number) + amount #Updates the value in the dictionary where account_number is the key
            else:
                print("Error, Transfer cannot be complete")