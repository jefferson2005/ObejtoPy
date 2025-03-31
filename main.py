from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e meu email é: {self.email}")

gui = Cliente(nome = 'Guilherme', email = 'gui@gmail.com', idade = '30')

gui.exibir()