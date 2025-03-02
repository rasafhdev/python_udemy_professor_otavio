import accounts
from bank import Bank
import people


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