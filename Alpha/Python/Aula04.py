# Sintaxe, Definição e Escopo
# Sintaxe e Definição: def

# def saudacao():
#     print('ola')

# saudacao()


# Parâmetros, Retorno e Argumentos

# def saudacao (nome):
#     print(f'ola ${nome}')

# saudacao('caue')

# sobrenome_nome = 'rezende'

# saudacao(sobrenome_nome)


# Retorno (return)

# def saudacao (nome):
#     return(f'ola ${nome}')

# sobrenome_nome = 'rezende'

# saudacao(sobrenome_nome)


# Rotinas e Unidades Lógicas

# Rotinas

# def saudacao ():
    # print('ola')

# saudacao()

# Unidades Lógicas

# def nome_completo(nome,sobrenome):
    # return f'{nome} {sobrenome}'

# idade = 21

# nome_idade = f'meu nome {nome_completo('caue', 'rezende')} e idade é {idade}'

# print(nome_idade)


# Boas Práticas

# Documentação

# def lista_numeros_pares(lista:list):

    # for numero in lista:
        # if numero %2==0:
            # print(numero)

# lista_qualquer = [1,2,3,4,5]

# lista_numeros_pares(lista_qualquer)


# Exercicio 01

# def saudacao_personalizada(nome):
#     print(nome)

# saudacao_personalizada('Caue')


# Exercicio 02

# def horario(lista: list):
#     for horas in lista:
#         if 0 <= horas < 12:
#             print('Bom dia!')
#         elif 12 <= horas < 18:
#             print('Boa tarde!')
#         elif 18 <= horas <= 06:
#             print('Boa noite!')
#         else:
#             print('Hora inválida')

# horario([13, 7, 21])


# Exercicio 03

# def somar(a,b):
#     return a + b


# # num1 = int(input("Digite o primeiro número: "))
# # num2 = int(input("Digite o segundo número: "))
# # resultado = somar(num1,num2)


# resultado = somar(10,3)
# print(resultado)


# Exercicio 04

# def subtracao(a,b):
#     return a - b

# # num1 = int(input("Digite o primeiro número: "))
# # num2 = int(input("Digite o segundo número: "))
# # resultado = subtracao(num1,num2)

# resultado = subtracao(10,3)
# print(resultado)


# Exercicio 05

# def mutliplicacao(a,b):
#     return a * b

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# resultado = subtracao(num1,num2)

# resultado = mutliplicacao(10,3)
# print(resultado)

# Desafio Pratico

def somar (a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por Zero!"
    
def menu():
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def eh_numero(valor):
    return valor.replace('.', '', 1).isdigit()

def obter_numeros():
    while True:
        a = input("Digite o primeiro número: ")
        b = input("Digite o segundo número: ")

        if eh_numero(a) and eh_numero(b):
            return float(a), float(b)
        else:
            print("Entrada inválida! Por favor, digite números válidos.")

def calculadora():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-5):")

        if escolha == "1":
            a, b = obter_numeros()
            print("Resultado da soma:", somar(a, b))
        elif escolha == "2":
            a, b = obter_numeros()
            print("Resultado da Subtração:", subtracao(a, b))
        elif escolha == "3":
            a, b = obter_numeros()
            print("Resultado da Multiplicação:", multiplicar(a, b))
        elif escolha == "4":
            a, b = obter_numeros(),
            resultado = dividir(a, b)
            print("Resultado da Divisão:", dividir(a, b))
        elif escolha == "5":
            print("Saindo da Calculadora. Ate logo!")
            break
        else:
            print("Opção Inválida. Tente Novamente")
calculadora()