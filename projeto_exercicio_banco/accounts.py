import abc


class Account(abc.ABC):
    """
    teste
    """
    def __init__(self, agency: int, account: int, balance: float=0) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def cash_out(self, value: float) -> float: ...
    """
    Classe abstrata
    """
    
    def make_a_deposit(self, amout: float) -> float:
        self.balance += amout
        self.details(f'(Deposit {amout})')
        return self.balance

    def details(self, msg: str ='' ) -> None:
        print(f'Your balace is: {self.balance:.2f} {msg}')
        print('-'*10)
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        atts = f'({self.agency!r}, {self.account!r}, {self.balance!r})'
        return f'{class_name}{atts}'

class SavingsAccount(Account):
    """
    Teste
    """
    def cash_out(self, value):
        balance_after_cash_out = self.balance - value

        if balance_after_cash_out >= 0:
            self.balance -= value
            self.details(f'(Cash Out: {value})')
            return self.balance
        print('Sorry!')
        self.details(f'\n(Transaction declined USD:{value})')


class CheckingAccount(Account):
    """
    teste
    """
    def __init__(self,
                 agency: int,
                 account: int,
                 balance: float=0,
                 limit: int=0):
        super().__init__(agency, account, balance)
        self.limit = limit

    def cash_out(self, value: float=0):
        balance_after_cash_out = self.balance - value
        max_limit = -self.limit

        if balance_after_cash_out >= max_limit:
            self.balance -= value
            self.details(f'(Cash Out: {value})')
            return self.balance
        
        print('Sorry!')
        self.details(f'\n(Transaction declined USD:{value})')
        return self.balance

    def __repr__(self) -> str:
        class_name = type(self).__name__
        atts = f'({self.agency!r}, {self.account!r}, {self.balance!r}, '\
            f'{self.limit!r})'
        return f'{class_name}{atts}'    

if __name__ == '__main__':
    # saving_accout = SavingsAccount(111, 222, 200)
    # saving_accout.cash_out(1)
    # saving_accout.make_a_deposit(10)
    # saving_accout.cash_out(4)
    # print('##')

    checking_account = CheckingAccount(agency=111,
                                       account=222,
                                       balance=0,
                                       limit=100)
    checking_account.cash_out(1)
    checking_account.make_a_deposit(1)
    checking_account.cash_out(1)
    checking_account.cash_out(1)
    checking_account.cash_out(1)
    checking_account.cash_out(98)
    print('##')
