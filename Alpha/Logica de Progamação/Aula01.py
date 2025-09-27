#Primeira aula do módulo de lógica
#variável - uma caixinha para guardar uma informação
#o nome da variável é sempre aquilo que ela vai guardar
#o python  é case sensitive, isso significa que letras maiusculas são diferentes de letras minusculas
# nome =
# Nome = 
# nome_de_usuario =
# nomeDeUsuario = 
# nomedeusuario =

#tipos de informação que existem na programação:
#string (texto) - tudo aquilo que está entre aspas
# nome = "Nath"
# #numero inteiro (int) - números positivos ou negativos sem casas decimais, (sem virgula, sem 'numeros quebrados')
# idade = 23
# #float - números "quebrados, números com vírgula"
# altura = 1.76
# maior_de_idade = True # Boolean (bool)
# type(10)#int
# type("10")#str
# type(10.5)#float
# print(type(42)) # Saída: <class ‘int’>
# print(type(3.14))# Saída: <class ‘float’>
# print(type("texto"))# Saída: <class ‘str’>

# cidade = input("Digite o nome da cidade que voce mora:  ")
# print(cidade)

# idade = int(input("Digite a sua idade: "))
# print(idade)

# altura = float(input("Digite a sua altura: "))
# print(altura)

#peça ao usuário a comida favorita dele, e o local favorito, e mostre na tela o que ele digitou!

# comida_local = input("Digite o seu comida favorito: "),input("Digite seu local favorito: ")
# print(comida_local)

# comidaFVT = input("Digite a sua Comida favorita: ")
# localFVT = input("Digite a seu Local favorito: ")
# print("Comida Favorita é:",comidaFVT , "Seu Local Favorito é:",localFVT)


# #Anotações 3

# num1 = 62
# num2 = 11

# print(“Adição: ”, num1 + num2) #73
# print(“Subtração: ”, num1 - num2) #51
# print(“Multiplicação: ”, num1 * num2) #682
# print(“Divisão: ”, num1 / num2) #5.63636363...
# print(“Divisão Inteira: ”, num1 // num2) #5
# print(“Módulo: ”, num1 % num2) #7
# print(“Exponenciação: , num1 ** num2)#52036560683837093888

# #Strings

# nome = "Infinity School"
# saudacao = (f"Olá, eu sou {nome} e dou as boas vindas a todos vocês!")
# print(saudacao)

# produto = "maça"
# preço = 1.99
# print(f"O preço da {produto} é R${preço}")

# pi = 3.14159
# print(f"O valor de pi com duas casa decimais é {pi:.2f}")

# largura = 5
# altura = 10
# area = (f"A área do retângulo é {largura * altura}")
# print(area)


#Exercício 1 : Crie uma variavel chamada “saudacao”, em seguida coloque uma atribuição e dentro de dado armazenado escreva “Hello World”

# saudacao = input("Digite seu nome:")
# print("Hello Word!" ,saudacao)


# # #Exercício 2 : Crie um programa que peça ao usuário para digitar:
# 1.Seu nome;
# 2.Sua idade;
# 3.Sua altura;
# 4.Em seguida, imprima esses valores e seus respectivos tipos.

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))

# print(nome, type(nome))
# print(idade, type(idade))
# print(altura, type(altura))


# #Exercício 3 : Criar um Programa que Peça as 4 Notas Bimestrais e Mostre a Média
# 1 - Solicitar as Notas do Usuário:
# 2 - Calcular a Média das Notas:
# 3 - Mostrar a Média Calculada para o Usuário:

# nota1 = float(input("Digite suas nota do 1º bimestre: "))
# nota2 = float(input("Digite suas nota do 2º bimestre: "))
# nota3 = float(input("Digite suas nota do 3º bimestre: "))
# nota4 = float(input("Digite suas nota do 4º bimestre: "))
# media = ((nota1) + (nota2) + (nota3) + (nota4)) / 4
# print(f"A sua media é: {media:.2f}")


# #Exercício 4 : Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha 20 dias no mês).
# 1 - Solicitar o Salário Mensal:
# 2 - Solicitar o Número de Horas Trabalhadas na Semana:
# 3 - Calcular o Total de Horas Trabalhadas no Mês:
# 4 - Calcular o Salário por Hora:
# 5 - Mostrar o Salário por Hora Calculado para o Usuário:

# salario_mensal = float(input("Digite o seu Salário Mensal: "))
# horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
# total_horas = (horas_trabalhadas)*4
# salario_hora = (salario_mensal) / (total_horas)
# print(f"O seu Salário por Hora é: {salario_hora}")


# #Exercício 5 : Peça ao usuário para digitar seu nome, idade e cidade natal. Use uma f-string para formatar e exibir uma mensagem com essas informações.
# 1 - Solicitar o Nome do Usuário:
# 2 - Solicitar a Idade do Usuário:
# 3 - Solicitar a Cidade Natal do Usuário:
# 4 - Formatar e Exibir a Mensagem com f-string:

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# cidade_natal = input("Digite sua cidade natal: ")
# print(f"Olá, seu nome é {nome}, tem {idade} anos e é de {cidade_natal}.")


