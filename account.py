class Account:
        """
        A class representing an account for a person
        """
        
    def __init__(self, name: str) -> None:
        """
        Create the Account object with the given name and a balance of 0.
        :name: The account name.
        :balance: The accounts default balance
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposit the specified amount into the account.
        :amount: The amount to be deposited.
        :bool: True if the deposit transaction is successful, False otherwise.
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw the specified amount from the account.
        :amount: The amount to be withdrawn.
        :bool: True if the withdrawal transaction is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the current account balance.
        :balance: The current account balance.
        """
        return self.__balance

    def get_account_name(self) -> str:
        """
        Get the account name.
        :name: The account name.
        """
        return self.__account_name
