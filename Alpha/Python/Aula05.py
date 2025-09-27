# Resumo da aula passada

# def soma(a,b):
#     return a + b

# resultado = soma(5,3)
# print(resultado)


# def quadrado(numero):
#     resultado = numero ** 2
#     return resultado

# resultado = quadrado(5)
# print("O quadrado de 5 é", resultado)


# Exercicio 01

# def calcular_media(n1, n2, n3):
#     media = (n1 + n2 + n3) / 3
#     return media

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))

# media_final = calcular_media(nota1, nota2, nota3)
# print(f"A média das notas é: {media_final:.2f}")


# Exercicio 02

# def calcular_area_retangulo(largura,comprimento):
#     area_retangulo = largura * comprimento
#     return area_retangulo

# largura = float(input("Digite a largura do retangulo: "))
# comprimento = float(input("Digite a comprimento do retangulo: "))

# area = calcular_area_retangulo(largura,comprimento)
# print(area)


# Args (Argumentos Posicionais Arbitrários)

# def somar_numeros(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado

# print(somar_numeros(1,2,3))
# print(somar_numeros(10,20,30,40,50))


# def somar(*args):
#     resultado = 0
#     for num in args:
#         resultado += num
#     return resultado

# print(somar(1,2,3))


# Kwargs (Argumentos de Palavra Chave)

# def mostrar_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# mostrar_info(nome = "Caue", idade = 30, cidade = "São Paulo")


# def mostrar_infomacoes(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# mostrar_infomacoes(nome = "Caue", idade = 30, cidade = "Exemplo")
# mostrar_infomacoes(curso = "Python", nivel = "Iniciante", plataforma = "Online")


# Args e Kwargs

# def minha_funcao(*args,**kwargs):
#     for arg in args:
#         print(arg)
#     for chave,valor in kwargs.items():
#         print(chave, valor)

# minha_funcao("Curriculo", "Desenvolvedor", nome = "Caue", idade = 21)


# Funções Lambda

# variavel = lambda parâmetro : comando

# quadrado = lambda x : x ** 2
# print(quadrado(5))

# par = lambda x : x %2 == 0
# print(par(10))

# name_upperCase = lambda n : n.upper()
# print(name_upperCase("Caue"))


# Expressões condicionais Funções Lambda

# par_impar = lambda x : "par" if x %2 == 0 else "impar"

# print(par_impar(5))
# print(par_impar(-2))


# Expressões condicionais Funções Lambda

# valida_usuarios = lambda user: "Erro: Usuario Precisa ser definido" if user == "" else ("Usuario não pode ter menos de 4 digitos" if len(user) < 4 else "Usuario Definido com sucesso!")

# print(valida_usuarios(""))
# print(valida_usuarios("Caue"))
# print(valida_usuarios("Rezende"))


# Funções Lambda

# numeros = [1,2,3,4,5]
# quadrados = list(map(lambda x : x **2, numeros))
# print(quadrados)


# from functools import reduce

# numeros = [1,2,3,4,5]
# soma = reduce(lambda x, y: x + y, numeros)
# print(soma)


# Exercicios GPT

# Exercicio 01 GPT

# def soma_todos(*args):
#     return sum(args)

# print(soma_todos(5, 10))
# print(soma_todos(1, 2, 3, 4, 5))
# print(soma_todos())


# Exercicio 02 GPT

# def imprimir_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")

# imprimir_info(nome="Ana", idade=25, cidade="São Paulo")


# Exercicio 03 GPT

# def ordenar_dict(*args,**kwargs):
    

# Exercicio 03

# def concatenar_strings(*args):
#     resultado = ""
#     for string in args:
#         resultado += string
#     return resultado 

# Exercicio 04

# def lista(*args):

#     lista_nums = [1,2,3,4,5,6,7,8,9,10]
#     dobro = list(map(lambda x : x**2,lista_nums))
#     return dobro
# print(lista())

# Exercicio 05

# def lista(*args):

#     lista_nums = [1,2,3,4,5,6,7,8,9,10]
#     pares = list(filter(lambda x : x%2==0, lista_nums))
#     return pares
# print(lista())

# Exercicio 06

# from functools import reduce

# def maior_string(lista):
#     if not lista:
#         return None
    
#     return reduce(lambda a, b: a if len(a) >= len(b) else b, lista)

# strings = ["gato", "elefante", "cachorro", "ar"]
# maior = maior_string(strings)
# print(maior)


# Exercicio 07

# def criar_lista_de_compras(*args):
#     compras = 