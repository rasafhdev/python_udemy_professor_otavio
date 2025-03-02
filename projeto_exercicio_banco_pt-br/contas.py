from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Conta(ABC):
    agencia: int
    conta: int
    saldo_conta: float

    @abstractmethod
    def sacar(self, valor_saque: float) -> float: ...

    def depositar(self, valor_deposito: float) -> float:
        self.saldo_conta += valor_deposito
        return self.saldo_conta
    
    def detalhes(self, msg: str = '' ) -> None:
        print(f'Seu saldo é: {self.saldo_conta:.2f} {msg}')
        print('-'*10)


@dataclass
class ContaPoupanca(Conta):
    def sacar(self, valor_saque: float):
        saldo_pos_saque = self.saldo_conta - valor_saque
        
        if saldo_pos_saque >= 0:
            self.saldo_conta -= valor_saque
            self.detalhes(f'(Valor sacado: {valor_saque})')
            return self.saldo_conta
        
        self.detalhes ('Falha, saldo insuficiente!')


if __name__ == '__main__':
    conta_poupanca = ContaPoupanca(111, 222, 200)
    print(conta_poupanca) # __repr__ automático


    conta_poupanca.detalhes()
    conta_poupanca.depositar(50)
    conta_poupanca.sacar(20)

@dataclass
class ContaCorrente(Conta):
    agencia: int
    conta: int
    saldo_conta: float =0
    limite: float=0

    def sacar(self, valor_saque: float):
        saldo_pos_saque = self.saldo_conta - valor_saque
        limite_maximo = -self.limite

        if saldo_pos_saque >= limite_maximo:
            self.saldo_conta -= valor_saque
            self.detalhes(f'Saque: {valor_saque}')
            return self.saldo_conta
        
        self.detalhes(f'Falha, saldo insuficiente ou limite da conta atingido: {valor_saque}')

if __name__ == '__main__':
    conta_poupanca = ContaPoupanca(111, 222, 200)

    conta_poupanca.detalhes()
    conta_poupanca.depositar(50)
    conta_poupanca.sacar(20)

    print("\nCriando Conta Corrente...")
    conta_corrente = ContaCorrente(111, 333, 500, 100)
    conta_corrente.sacar(550)  # Teste com limite
    conta_corrente.sacar(100)  # Deve falhar        
