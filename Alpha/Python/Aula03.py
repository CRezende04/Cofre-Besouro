# Exercicio 01

# idade = int(input("Digite a idade:"))
# if idade >= 0 and idade < 12:
#     print("Criança")
# elif idade >= 12 and idade < 17:
#     print("Adolescente")
# elif idade >= 18 and idade < 59:
#     print("Adulto")
# elif idade >= 60 or idade > 60:
#     print("Idoso")
# else:
#     print("Não Nasceu")


# maior = 0
# menor = 0

# for i in range(5):
#     numero = int(input(f"Digite um numero: "))
#     if numero > 10:
#         maior += 1
#     elif numero < 10:
#         menor += 1
# print(f"Temos {maior} numeros maiores que 10 e temos {menor} numeros menores que 10")     


# Exercicio ChatGPT

# Exercicio 01 

# lista_notas = []
# media = 0

# while True:
#     nota = int(input("Digite suas notas [Digite -1 para Encerrar]: "))
#     if nota == -1:
#         print("Encerrado")
#         break
#     lista_notas.append(nota)
    
# if lista_notas:
#     soma = 0
#     for nota in lista_notas:
#         soma += nota  # ou: soma = soma + nota

#     media = soma / len(lista_notas)
#     print(f"Média: {media:.2f}")
# else:
#     print("Nenhuma nota válida foi inserida.")


# Exercicio 02

dados_aluno = {}
notas = ()
nome_aluno = input("Digite seu Nome:")
idade = int(input("Digite a sua idade:"))
for i in range(2):
    nota_mat = float(input("Digite a nota de Matematica"))
    nota_cien = float(input("Digite a nota de Ciencia"))
    nota_his = float(input("Digite a nota de Historia "))
    notas = notas + (nota_mat , nota_cien, nota_his)

print (dados_aluno , notas)









# for i in range(0,10):
#     print(i)

#while True:


#lista é uma variável que guarda mais de um valor ao mesmo tempo

dados = [1.5,7,"nome",True, []]

#posição de elementos começa em 0
# print(dados[-6])

#como adicionar algo em uma lista:
#append() - acrescenta no final da lista
# lista = [1,2,3,4,5]
# lista.append("Nath")
# print(lista)

#insert() - acrescenta em qualquer posição da lista

# lista = [1,2,3,4,5]
# lista.insert(2,"Nath")
# print(lista)

#metodo é uma função que faz alguma coisa mas depende do tipo da informação

#função faz alguma coisa, mas não depende do tipo da informação


#como remover algo de uma lista?
#remove()
#pop() ou pop(posição)

lista = [1,2,3,4,5,6,7,7,8,9,10]
# lista.pop()
# print(lista)
# lista.pop(5)
# print(lista)
# lista.remove(7)
# print(lista)




# 1. Média de notas com listas e laços:
# Escreva um programa que receba uma lista de notas de um aluno e calcule sua média. Use um laço de repetição para PERCORRER sobre a lista de notas e uma variável para acumular a soma das notas. Depois, calcule a média e imprima o resultado.
# notas = []

# for i in range(4):
#     nota = float(input("Digite a sua notinha: "))
#     notas.append(nota)
# soma = sum(notas)
# media = soma/len(notas)
# print(media)
# lista = [1,2,3,4,5]

# minha_tupla = (1,2,3,4,5,6)

# frutas = {"maçã","banana","laranja"}
# print(frutas)
# frutas = set()
# lista = list()
# dicti = dict()
# tupla = tuple()


# lista = [1,2,3]
# set_ = {4,5,6}

# set1 = set(lista)
# lista_nova = list(set_)
# nova_tupla = tuple(lista)



dados = {"Nathalia",23,"Salvador","São Paulo"}
#diferença entre remove e discard

#remove() - sinaliza um erro caso tente tirar algo que não está no conjunto
# dados.remove("Belo Horizonte")
#discard() - se tentar remover algo que nao esta na lista com o discard, não da erro
# dados.discard("Belo Horizonte")
# print(dados)



dados ={"nome":"Nathalia",
"idade":23,
"nascida_em":"Salvador",
"mora_em":"SP",
"habilidades": ["Python","css"],
"notas": {

}}






# DESAFIO PRÁTICO
# Sistema de Cadastro de Alunos – passo 1
# Cadastro de Alunos: O programa deve permitir ao usuário cadastrar alunos. Cada aluno terá as seguintes informações: nome, idade e notas em três disciplinas: Matemática, Ciências e História. Os dados de cada aluno devem ser armazenados em um dicionário com as seguintes chaves: 'nome', 'idade', 'notas'. As notas devem ser armazenadas em uma tupla.

notas_matematica = []
notas_ciencias = []
notas_historia = []
dados_aluno = {}
nome_aluno = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
for i in range(3):
    nota_mat = float(input("Digite a nota de Matematica: "))
    nota_cien = float(input("Digite a nota de Ciencias: "))
    nota_his = float(input("Digite a nota de Historia: "))
    notas_matematica.append(nota_mat)
    notas_ciencias.append(nota_cien)
    notas_historia.append(nota_his)
tupla_mat = tuple(notas_matematica)
tupla_his = tuple(notas_historia)
tupla_cien = tuple(notas_ciencias)

notas = {"Matematica":tupla_mat,"historia":tupla_his,"ciencias":tupla_cien}

dados_aluno = {"nome":nome_aluno,"idade":idade,"notas":notas}
print(dados_aluno)