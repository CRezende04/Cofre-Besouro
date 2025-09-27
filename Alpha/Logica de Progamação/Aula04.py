# INTRODUÇÃO AO FOR

# for variavel in sequencia:


# FUNCIONAMENTO DO FOR

# for i in range(5):
#     print(i)

# Execute o código acima para iterar sobre os números de 0 a 4 e imprimir cada número.


# VANTAGENS DO USO DO LOOP FOR

# palavra = "Python"
# for letran in palavra:
#     print(letra)

# Execute o código acima para iterar sobre cada letra da palavra "Infinity" e imprimir cada letra.


# FUNÇÃO RANGE()

# Existem tres formas principais de usar a função range():

# range(stop)
# range(start,stop)
# range(start,stop,step)

# for i in range(5):
#     print(i)

# for i in range(2,7):
#     print(i)

# for i in range(1,10,2):
#     print(i)


# # Exercicio 01

# numero = int(input("Insira um numero:"))
# for i in range(1, 11):
#     print(f"{numero} X {i} = {numero * i}")


# soma = 0
# for i in range(1,101):
#     soma += i
#     print(soma)


# Exercicio 03

# palavra = input("Insira uma Palavra:")

# for letra in palavra:
#     print(letra)


# Exercicio 04

# for i in range(10,0,-1):
#     print(i)

# print("Feliz Ano Novo!")


# Exercicio 05

# positivos = 0
# negativos = 0

# for i in range():
#     numero = float(input(f"Digite o {i+1}º número: "))
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
# print(f"Números Positivos: {positivos}")
# print(f"Números negativos: {negativos}")


# Exercicio 06

# soma = 0
# for i in range(1,51):
#     if i %2 == 0:
#         soma += i
# print(soma)


# Exercicio 07

# palavra = input("Digite uma palavra:")
# vogais = "aeiouAEIOU"
# qtd_vogais = 0
# for letra in palavra:
#     if letra in vogais:
#         qtd_vogais += 1
# print(f"Contém {qtd_vogais} vogais.")


# Exercicio 08

soma = 0
for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}:"))
    soma += nota
media = soma/5
print(f"Media: {media:.2f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")


# Exercicio 09

# for i in range(1, 21):
#     if i == 15:
#         break
#     if i % 2 == 0:
#         print(f"{i} é par")
#     else:
#         print(f"{i} é ímpar")


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


# Escreva um programa em Python que pede ao usuário para digitar um número inteiro. O programa deve verificar se o número é negativo ou maior que 100. Se for, exiba a mensagem "Fora do intervalo"; caso contrário, exiba "Dentro do intervalo"


# numero = int(input(' Digite uma numero: '))
# if numero<0 or numero>100:
#     print("Fora do intervalo")
# else:
#     print("Dentro do intervalo")



# # Escreva um programa em Python que pede ao usuário para digitar uma letra. O programa deve verificar se a letra é "a" ou "e" (minúsculas).
# # Se for, exiba: "Você digitou uma vogal comum"
# # Caso contrário, exiba: "Outra letra"

# idade1=input("digite idade 1:")
# idade2=input("digite idade 2:")
# if idade1>idade2:
#     print("maior")
# elif idade1<idade2:
#     print("menor")
# else:
#     print("igual")


# # Peça ao usuário duas idades e use operadores de comparação para
# # verificar se a primeira idade é maior, menor ou igual à segunda.


# idade = int(input("Digite a sua idade: "))
# idade2 = int(input("Digite outra idade: "))

# if idade>idade2:
#     print("A primeira idade é maior que a segunda!")
# elif idade<idade2:
#     print("A primeira idade é menor que a segunda!")
# else:
#     print("As duas idades são iguais!")

# # Peça ao usuário duas palavras e use operadores
# # de comparação para verificar se elas são iguais.

# palavra = input(" Digite a primeira palavra: ")
# palavra2 = input("Digite a segunda palavra: ")

# if palavra==palavra2:
#     print('As palavras são iguais!')
# else:
#     print("As palavras são diferentes")




# #operadores de comparação:
# #toda vez que utilizamos um operador de comparação, estamos fazendo uma pergunta para a máquina, e ela nos responde, com sim ou não
# # print(5==6)
# # print(12>8)
# # print(5>=5)
# # print(5!=5)

# #operadores de atribuição:
# # numero = 5
# # soma = 0
# # soma+=numero
# # print(soma)

# #peça uma idade ao usuario, e mostre:
# #maior de idade, se ele tiver 18 ou mais 
# #menor de idade, se ele tiver menos

# # idade = int(input("Digite a sua idade: "))
# # if idade>=18:
# #     print('Maior de idade!')
# # else:
# #     print("Menor de idade")

# # Crie um programa que peça ao usuário um número e use a
# # estrutura condicional if para verificar se ele é par ou ímpar.

# # numero = int(input(' Digite um número: '))
# # if numero%2==0:
# #     print("Par")
# # else:
# #     print("Ímpar")



# # Crie um programa que peça a nota de um aluno e
# # use if e else para verificar se ele foi aprovado (nota >= 6).

# # nota = float(input("Digite a nota do aluno: "))
# # if nota>=6:
# #     print('Aprovado!')
# # else:
# #     print("Reprovado!")


# #peça a idade do usuário e mostre:
# # se tiver de 0 a 12 anos, criança
# #senão, se tiver de 13 a 17 anos, adolescente
# #senão, mostre adulto!

# # idade = int(input(' Digite uma idade: '))
# # if idade>=0 and idade<=12:
# #     print("Criança")
# # elif idade>=13 and idade<=17:
# #     print("Aborrescente!")
# # else:
# #     print("Adulto")


# # Escreva um programa em Python que pede ao usuário para digitar um número inteiro. O programa deve verificar se o número é negativo ou maior que 100. Se for, exiba a mensagem "Fora do intervalo"; caso contrário, exiba "Dentro do intervalo"


# # numero = int(input(' Digite uma numero: '))
# # if numero<0 or numero>100:
# #     print("Fora do intervalo")
# # else:
# #     print("Dentro do intervalo")




# # Escreva um programa em Python que pede ao usuário para digitar uma letra. O programa deve verificar se a letra é "a" ou "e" (minúsculas).
# # Se for, exiba: "Você digitou uma vogal comum"
# # Caso contrário, exiba: "Outra letra"

# # letra = input(' Digite uma letra: ')
# # if letra=='a' or letra=='e':
# #     print("Você digitou uma vogal comum")
# # else:
# #     print('Outra letra!')
    

# # eh_habilitada = False
# # if not eh_habilitada:
# #     print("Voce não tem habilitação. ")
# # else:
# #     print(" Voce tem habilitação")

# # # Peça ao usuário duas idades e use operadores de comparação para
# # # verificar se a primeira idade é maior, menor ou igual à segunda.


# # idade = int(input("Digite a sua idade: "))
# # idade2 = int(input("Digite outra idade: "))

# # if idade>idade2:
# #     print("A primeira idade é maior que a segunda!")
# # elif idade<idade2:
# #     print("A primeira idade é menor que a segunda!")
# # else:
# #     print("As duas idades são iguais!")

# # # Peça ao usuário duas palavras e use operadores
# # # de comparação para verificar se elas são iguais.

# # palavra = input(" Digite a primeira palavra: ")
# # palavra2 = input("Digite a segunda palavra: ")

# # if palavra==palavra2:
# #     print('As palavras são iguais!')
# # else:
# #     print("As palavras são diferentes")

# # Verificação de Maioridade e Habilitação:
# # Crie um programa que peça a idade do usuário e se ele possui habilitação
# # (sim ou não). Use operadores lógicos para verificar se ele é maior de idade
# # (>= 18) e possui habilitação.

# idade = int(input("Digite a sua idade: "))
# tem_habilitacao = int(input(" 1. Sim, 2.Não"))
# if idade>=18 and tem_habilitacao==1:
#     print("Você é de maior e tem habilitação, pode dirigir")
# else:
#     print("Você não pode dirigir!")



# # Desconto em Preço:
# # Peça ao usuário para inserir o preço de um produto e, em seguida,
# # use o operador de atribuição -= para aplicar um desconto de 5%.

# preco = float(input("Digite o preço do produto: "))
# desconto_5 = (5/preco)*100
# preco-=desconto_5
# print(f'O valor do produto com o desconto é de {preco}')



# # Atividade 06:
# # Dobro do Valor:
# # Solicite ao usuário um número e use o operador de
# # atribuição *= para dobrar o valor e exibir o resultado.

# numero = int(input(' Digite um número: '))
# numero_antigo = numero
# numero*=2
# print(f" O dobro do número {numero_antigo} é {numero} ")



# # Verificação de Caracteres em uma String:
# # Crie um programa que peça ao usuário uma frase e um caractere.
# # Use o operador de associação in para verificar se o caractere está
# # presente na frase.

# frase = input('Digite uma frase: ')
# letra = input("Digite uma letra: ")
# if letra in frase:
#     print('A letra esta na frase!')
# else:
#     print(" A letra não está na frase")

# ___________________________________________AULA 03 ____________________________________________


# # base = float(input('Insira a base: '))
# # altura = float(input('Insira a altura: '))
# # area=base*altura
# # print(area)

# #utilizamos o while quando não sabemos a quantidade de vezes que algo deve ser repetido

# #for é utilizado quando voces sabem a quantidade de vezes que algo precisa ser repetido


# #toda vez que fizer um while com condição, precisa de uma linha de código para que essa condição, em algum momento, se torne falsa.

# # contador = 1
# # while contador<=5:
# #     print(contador)
# #     contador+=1

# #mostre uma contagem de 10 a zero, e no final, mostre Feliz Ano novo!
# # contador =10
# # while contador>=0:
# #     print(contador)
# #     contador-=1
# # print("Feliz ANo novo")

# #a contagem começa com 10
# # termina em zero
# #preciso ir de 1 em 1
# #o print("Feliz ANo novo") vai ficar fora do while

# # senha = ""
# # while senha!="1234":
# #     senha = input("Digite a sua senha: ")
# # print("Senha correta")


# # Contagem de 1 a 10:
# # Crie um programa que use um laço while
# # para contar de 1 a 10 e exibir cada número.

# # contador=1
# # while contador<=10:
# #     print(contador)
# #     contador+=2

# # Soma de Números de 1 a 100:
# # Escreva um programa que use um laço while para
# # somar os números de 1 a 100 e exiba o resultado.

# # contador = 1
# # soma = 0
# # while contador<=100:
# #     soma+=contador
# #     contador+=1
# # print(soma)

# # Tabuada de um Número:
# # Faça um programa que solicite um número ao usuário e use
# # um laço while para exibir a tabuada desse número (de 1 a 10).

# # numero =int(input('digite seu numero'))
# # tabuada = 1
# # while tabuada<=10:
# #     resultado = numero*tabuada
# #     print(f'{numero}x{tabuada}={resultado}')
# #     tabuada+=1






# nome = input("digite um nome: ")
# print(nome.capitalize())

# .lower() - deixa tudo minúsculo
# .upper() - deixa tudo maiusculo
# .capitalize() - deixa a primeira letra maiuscula
#.title() - deixa todas as primeiras letras maiusculas



#quando utilizar for e While:

#utilizamos o while quando NÃO SABEMOS a quantidade de vezes que algo deve ser repetido

#utilizamos o for quando SABEMOS a quantidade de vezes que algo deve ser repetido

#inicio
#final - corta o ultimo
#passo
# for i in range(1,11,2):
#     print(i)

#final
# for x in range(10):
#     print(x)

#inicio
#final
# for i in range(1,11):
#     print(i)


#faça um laço for que vá de 10 a 0, indo de 1 em 1
# for i in range(10,-1,-1):
#     print(i)


#for que percorre listas (primeira aula de Python) e strings


# palavra = "Python"
# for letra in palavra:
#     print(letra)



#peça uma palavra ao usuario e conte a quantidade de vogais que tem nela.

#preciso pedir uma palavra ao usuario V
#tem um for em algum lugar V
#preciso saber identificar quais são as vogais V
#preciso de uma variavel pra guardar a quantidade de vogais
# palavra = input("Digite uma palavra qualquer: ")
# vogais = 0
# for letra in palavra:
#     if letra=="a" or letra=='e' or letra=='i' or letra=="o" or letra=="u":
#         vogais+=1
# print(f'tem {vogais} vogais na palavra {palavra}')



# palavra = input("Digite uma palavra qualquer: ").lower()
# vogais = 0
# for letra in palavra:
#    if letra in 'aeiou':
#         vogais+=1
# print(f'tem {vogais} vogais na palavra {palavra}')


#Função e método:
#função funciona independentemente do tipo da informação
#método é uma função que depende do tipo da informação


# nome = "nathalia"
# print(nome.upper())



# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

# numero = int(input("Digite um número: "))
# for i in range(1,11,1):
#     print(f'{numero} X {i} = {numero*i}')


# Crie um programa que use um laço for para somar
# todos os números de 1 a 100 e exiba o resultado.

# soma = 0
# for i in range(1,101,1):
#     soma+=i
# print(soma)

# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.

# palavra = input("Digite uma palavra qualquer: ")
# for letra in palavra:
#     print(letra)


# Desenvolva um programa que use um laço for para fazer uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# for i in range(10,0,-1):
#     print(i)
# print("Feliz Ano Novo!")