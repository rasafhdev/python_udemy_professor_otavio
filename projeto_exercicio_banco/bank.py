import accounts
import people

class Bank:
    def __init__(
        self,
        agencys: list[int] | None =  None,
        customers: list[people.People] | None = None,
        accounts: list[accounts.Account] | None =  None,
    ):
        self.agencys = agencys or []
        self.customers = customers or []
        self.accounts = accounts or []
    
    # Checkers
    def _check_agency(self, account):
        if account.agency in self.agencys:
            return True
        return False

    def _check_customer(self, customer):
        if customer in self.customers:
            return True
        return False


    def _check_account(self, account):
        if account in self.accounts:
            return True
        return False
    
    def _check_account_isof_customer(self, cosutomer, account):
        if account in cosutomer.account:
            return True
        return False

    def auth(self, customer: people.Customer, account: accounts.Account):
        return self._check_account(account) and \
        self._check_customer(customer) and \
        self._check_agency(account)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.accounts!r}, {self.agencys}, {self.customers})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    c1 = people.Customer('Rodrigo', 29)
    cc1 = accounts.CheckingAccount(111, 222, 0, 100)
    c1.conta = cc1


    c2 = people.Customer('Asafh', 29)
    cp2 = accounts.SavingsAccount(333, 444, 0,)
    c2.conta = cp2


    bank = Bank()
    bank.customers.extend([c1, c2])
    bank.accounts.extend([cc1, cp2])
    bank.agencys.extend([111, 222, 333])

    if bank.auth(c1, cc1):
        cc1.make_a_deposit(100)
        print(c1.conta)

    