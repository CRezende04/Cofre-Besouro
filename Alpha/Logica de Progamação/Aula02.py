# OPERADORES DE COMPARAÇÃO

# x = 5
# y = 10
# print(x == y) #False
# print(x != y) #True
# print(x > y) #False
# print(x < y) #True
# print(x >= y) #False
# print(x <= y) #True


# OPERADORES LOGICOS

# a = True
# b = False

# resultado = (a and b) #False E
# resultado = (a or b) #True OU
# resultado = not a #False NÃO


# OPERADORES DE ATRIBUIÇÃO

# x = 10 #Atribui o valor do lado direito à variável do lado esquerdo
# x += 5 # x = x + 5 #Soma e atribui o resultado à variável
# x -= 3 # x = x - 3 #Subtrai e atribui o resultado à variável.
# x * 2 # x = x * 2 #Multiplica e atribui o resultado à variável.
# x /= 2 # x = x / 2 #Divide e atribui o resultado à variável.


# OPERADORES DE ASSOCIAÇÃO

# fruta1 = "maça"
# fruta2 = "banana"
# fruta3 = "cereja"
# resultado = "maça" in (fruta1, fruta2, fruta3)
# print(resultado) #True


# fruta1 = "maça"
# fruta2 = "banana"
# fruta3 = "cereja"
# resultado = "laranja" not in (fruta1, fruta2, fruta3)
# print(resultado) #True

#Exercicio 1

# idade1 = input("Insira a primeira idade:")
# idade2 = input("Insira a segunda idade:")

# print(idade1 >= idade2)


#Exercicio 2

# palavra1 = input("Insira a primeira palavra:")
# palavra2 = input("Insira a segunda palavra:")

# print(palavra1 == palavra2)


#Exercicio 3 

# idade = int(input("Insira sua idade:"))
# habilitacao = input("Possui Habilitação:")
# print(idade >= 18, habilitacao == "sim")

# if idade >= 18 :
#     print(idade >= 18, habilitacao == "sim")
# elif idade >= 18 and habilitacao == "não":
#     print(idade >= 18, habilitacao == "sim")
# else :
#     print(idade >= 18, habilitacao == "sim")
    
#Exercicio 4

# nota1 = float(input("Insira uma nota:"))
# nota2 = float(input("Insira outra nota:"))

# print(nota1 >= 6, nota2 >= 6 )


#Exercicio 5

# preco = float(input("Insira o preço de um produto:"))
# preco -= preco * 0.05 
# print(preco)


#Exercicio 6

# numero = float(input("Insira um numero:"))
# numero *= 2
# print(numero)


#Exercicio 7

# frase = input("Insira uma frase :")
# palavra = input("Insira um caractere:")
# resultado = caractere in frase

# print(resultado)

#Exercicio 8 

# frase = input("Insira uma frase :")
# palavra = input("Insira um palavra:")
# resultado = palavra in frase

# print(resultado)

#Exercicio 9

#numero = float(input("Insira um numero:"))

#if numero %2==0 :
#     print("Par")
#else :
#     print("Impar")


#Exercicio 10

# Crie um programa que peça a nota de um aluno e use if para verificar se ele foi aprovado (nota >= 6).

# nota = float(input("Insira sua Nota:"))
# if nota >= 6:
#     print("Aprovado")
# else :
#     print("Reprovado")


#Exercicio 11

# numero = float(input("Insira um numero:"))

# if numero %2==0 and numero >= 0 :
#     print("Par e Positivo")
# elif numero %2==0 and numero < 0:
#     print("Par e Negativo")
# elif numero %2==1 and numero >= 0:
#     print("Impar e Positivo")
# else :
#     print("Impar e Negativo") 

#Exercicio 12

# peso = float(input("Insira seu peso:"))
# altura = float(input("Insira sua altura:"))
# imc = peso / (altura ** 2)

# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc >= 18.5 and imc < 24.9:
#     print("Peso normal")
# elif imc <= 25 and imc < 29.9:
#     print("Sobrepeso")
# elif imc <= 30 and imc < 34.9:
#     print("Obesidade grau 1")
# elif imc <= 35 and imc < 39.9:
#     print("Obesidade grau 2")
# else:
#     print("Obesidade grau 3 ou mórbida")


#Exercicio 13

# nome = input("Insira seu nome:")
# senha = input("Insira sua senha:")
# if nome == "admin" and senha == "1234":
#     print("Usuario Conectado")
# elif nome == "admin" and senha != "1234":
#     print("Senha Incorreta")
# elif nome != "admin" and senha == "1234":
#     print("Nome de usuario incorreto")
# else:
#     print("Usuario e senha incorretos")


#Exercicio 14

# preco_original = float(input("Insira o preço original do produto:"))
# quantidade = float(input("Insira a quantidade comprada:"))

# if quantidade >= 10:
#     desconto = 0.1  # 10% de desconto
#     valor_final = preco_original * (1 - desconto)
#     print(f"Valor total: R${valor_final:.2f}")
# else:
#     print(f"Valor total: R${preco_original:.2f}")


#Extra 

# idade = int(input("Insira uma idade:"))
# if idade >= 0 and idade <= 12:
#     print("Criança")
# elif idade >= 13 and idade <= 17:
#     print("Adolescente")
# else :
#     print("Adulto")


# Extra 2

# numero = int(input("Digite um numero"))
# if numero <= 0 or numero > 100:
#     print("Fora do Intervalo")
# else:
#     print("Dentro do Intervalo")

# Extra 3

# letra = input("Digite uma letra:")
# if letra == "a" or letra == "e" :
#     print("Voçe digitou uma vogal comum")
# else :
#     print("Outra Letra")


#operadores de comparação:
#toda vez que utilizamos um operador de comparação, estamos fazendo uma pergunta para a máquina, e ela nos responde, com sim ou não
# print(5==6)
# print(12>8)
# print(5>=5)
# print(5!=5)

#operadores de atribuição:
# numero = 5
# soma = 0
# soma+=numero
# print(soma)

#peça uma idade ao usuario, e mostre:
#maior de idade, se ele tiver 18 ou mais 
#menor de idade, se ele tiver menos

# idade = int(input("Digite a sua idade: "))
# if idade>=18:
#     print('Maior de idade!')
# else:
#     print("Menor de idade")

# Crie um programa que peça ao usuário um número e use a
# estrutura condicional if para verificar se ele é par ou ímpar.

# numero = int(input(' Digite um número: '))
# if numero%2==0:
#     print("Par")
# else:
#     print("Ímpar")



# Crie um programa que peça a nota de um aluno e
# use if e else para verificar se ele foi aprovado (nota >= 6).

# nota = float(input("Digite a nota do aluno: "))
# if nota>=6:
#     print('Aprovado!')
# else:
#     print("Reprovado!")


#peça a idade do usuário e mostre:
# se tiver de 0 a 12 anos, criança
#senão, se tiver de 13 a 17 anos, adolescente
#senão, mostre adulto!

# idade = int(input(' Digite uma idade: '))
# if idade>=0 and idade<=12:
#     print("Criança")
# elif idade>=13 and idade<=17:
#     print("Aborrescente!")
# else:
#     print("Adulto")

