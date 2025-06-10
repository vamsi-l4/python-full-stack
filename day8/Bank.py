from abc import ABC,abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass
    @abstractmethod
    def set_balance(self):
        pass
class SavingAccount(Account):
    __balance=0

    def get_balance(self):
        return self.__balance
    def withdraw_balance(self,amount):
        if self.__balance < amount:
             print("not enough money")
        self.__balance-=amount
        print("the balance is",amount)
    def deposit_balance
class currentAccount(Account):
    __balance=0
    limit__balance=limit      
    def limit_blance(self,limit):
        return self.limit
    def deposit_balance(self)        