

# cria um decorator, e que empurra as informações para a classe.
# é como se este código estivesse na clase.
# isto faz com que não repitamos código

def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome


flamengo = Time('Flamengo')
pais = Pais('Brasil')

print(pais)
print(flamengo)
