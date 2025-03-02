import accounts

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @age.setter
    def age(self, age: int):
        self._age = age


    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'



class Customer(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: accounts.Account | None = None

if __name__ == '__main__':

    c1 = Customer(name='Rodrigo', age=29)
    c1.conta = accounts.CheckingAccount(account = 111,
                                      agency  = 222,
                                      balance = 0,
                                      limit   = 100)
    
    print(c1)
    print(c1.conta)

    c2 = Customer(name='Asafh', age=29)
    c2.conta = accounts.SavingsAccount(account = 333,
                                      agency  = 444,
                                      balance = 0,)
    
    print(c2)
    print(c2.conta)