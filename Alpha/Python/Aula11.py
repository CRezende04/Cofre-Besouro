# my_name = 'Raama'.upper()
# print(type(my_name))

# my_numbers = [4,3,2,1]

# my_numbers.append(0)
# print(type(my_numbers))

# class Carro:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
#         self.velocidade = 0
        
        
# def acelerar(self, velocidade):
#     self.velocidade += velocidade
#     print(f'O carro está a {self.velocidade} km/h.')

    
# def frear(self, velocidade):
#     if self.velocidade >= velocidade:
#         self.velocidade -= velocidade
#         print(f'O carro está a {self.velocidade} km/h após frear.')
#     else:
#         print('O carro já está parado.')
        
        
# class Carro:
#     def __init__(self, marca, modelo, ano, possui_4_rodas):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.possui_4_rodas = possui_4_rodas

        
# class Carro:
#     def __init__(self, marca, modelo, ano, possui_4_rodas):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.possui_4_rodas = possui_4_rodas
        
#     def ligar(self):
#         return f"O {self.modelo} está ligando"
    
# orochinho = Carro("Renault", "Oroch", 2019, True)

# print(orochinho.modelo)
# print(orochinho.ligar())


# class Carro:
#     def __init__(self, marca, modulo):
#         self.marca = marca
#         self.modulo = modulo
#         self.velocidade = 0
        
#     def acelerar(self):
#         self.velocidade += 10
#         print(f"{self.marca} {self.modulo} acelerando. Velocidade atual: {self.velocidade} km/h")
        
#     def frear(self):
#         self.velocidade -= 5
#         print(f"{self.marca} {self.modelo} freando. Velocidade atual: {self.velocidade} km/h")
        
# meu_carro = Carro("Ford", "Mustang")

# meu_carro.acelerar()
# meu_carro.frear()

# Exercicio 01


# class Cachorro:
#     def __init__(self,nome,raca,idade):
#         self.nome = nome
#         self.modulo = raca
#         self.idade = 0

# Exercicio 02


# class Pessoa:
#     def __init__(self,nome,idade,peso,genero):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.genero = genero
        
# Exercicio 03


# class Funcionario:
#     def __init__(self, nome, cargo, salario):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario = salario

#     def __str__(self):
#         return f"{self.nome} - {self.cargo} - R${self.salario:.2f}"


# class Empresa:
#     def __init__(self, nome):
#         self.nome = nome



#     def adicionar_funcionario(self, nome, cargo, salario):
#         funcionario = Funcionario(nome, cargo, salario)
#         self.funcionarios.append(funcionario)
#         print(f"Funcionário {nome} adicionado com sucesso.")
        
        
#     def remover_funcionario(self, nome):
#         for funcionario in self.funcionarios:
#             if funcionario.nome == nome:
#                 self.funcionarios.remove(funcionario)
#                 print(f"Funcionário {nome} removido com sucesso.")
#                 return
#         print(f"Funcionário {nome} não encontrado.")


#     def listar_funcionarios(self):
#         if not self.funcionarios:
#             print("Não há funcionários cadastrados.")
#         else:
#             print(f"Funcionários da empresa {self.nome}:")
#             for funcionario in self.funcionarios:
#                 print(funcionario)


# empresa = Empresa("Tech Solutions")

# empresa.adicionar_funcionario("Ana Souza", "Desenvolvedora", 4500.00)

# empresa.adicionar_funcionario("Carlos Lima", "Gerente", 7500.00)

# empresa.listar_funcionarios()

# empresa.remover_funcionario("Ana Souza")

# empresa.listar_funcionarios()


# Exercicio 04

# class Calculadora:
#     def __init__(self):
#         pass
#     def soma(self,x,y):
#         return x+y
#     def subtracao(self,x,y):
#         return x-y
#     def multiplicacao(self,x,y):
#         return x*y
#     def divisao(self,x,y):
#         return x/y
    

# Exercicio 05

class Fatura:
    def __init__(self,nome_i: str,preco: float,qtd_item:int,):
        self.nome_i = nome_i
        self.preco = preco
        self.qtd_item = qtd_item
        self.total_ftr = 0

    def gerar_fatura(self):
        self.valor_total = self.qtd_item * self.preco
        return self.valor_total
    
fatura1 = Fatura("Caneta", 2.50, 10)
print("Valor da fatura:", fatura1.gerar_fatura())
        
        