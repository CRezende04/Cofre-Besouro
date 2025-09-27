# Sets e suas características

# meu_set = {'Infinity', 'School'}
# print(type(meu_set))
# # <class 'set'>

# frutas = {"maçã", "banana", "cereja", "maçã"}
# print(frutas)
# # {'maçã', 'cereja', 'banana'}


# 1.Elementos separados por Vírgula dentro de um Conjunto:
# set1 = {'Infinity','School','202...'}

# 2. Usando Compreensão de Conjuntos:

# set1 = {letra for letra in 'infinity' if letra not in 'aeiou'}

# 3. Usando o método Construtor:

# set1 = set(['Infinity','School','202...'])
# print(set1)

# add()

# convidados = {'João', 'Maria', 'Eduarda'}

# convidados.add('Carlos')
# print(convidados)
# # {'Eduarda', 'Carlos', 'João', 'Maria'}

# update()

# ids = {10, 12, 13, 14}
# novos_ids = {11, 13, 15}

# ids.update(novos_ids)
# print(ids)
# # {10, 11, 12, 13, 14, 15}

# Errado
# set_1 = {1, 2, 3}
# print(set_1[0])


# convidados = {'João', 'Maria', 'Eduarda'}
# print('Maria' in convidados)

# convidados = {'João', 'Maria', 'Eduarda'}
# for x in convidados:
#     print(x)

# remove() | discard()

# convidados = {'João', 'Maria', 'Eduarda'}
# print(convidados.remove('Maria'))
# print(convidados.discard('Eduarda'))
# print(convidados)


# Operações Matemáticas com Sets

# Intersection()

# convidados = {'João', 'Maria', 'Eduarda'}
# convidados2 = {'Pedro', 'Raama', 'Maria'}

# print(convidados.intersection(convidados2))
# #{'Maria'}

# Intersection_update()

# convidados = {'João', 'Maria', 'Eduarda'}
# convidados2 = {'Pedro', 'Raama', 'Maria'}

# convidados.intersection_update(convidados2)
# print(convidados)
# {'Maria'}

# union()

# set1 = {1, 2, 3}
# set2 = {'z','x', 'a'}

# print(set1.union(set2))

# print(set1 | set2)


# Exercicio 01

# frutas = {}

# frutas.add('maçã','banana','uva','laranja')
# print(frutas)


# Exercicio 02

# frutas = ('maçã','banana','uva','laranja')

# fruta = "banana\n"

# if fruta in frutas:
#     print("A fruta está no conjunto.")
# else:
#     print("A fruta NÃO está no conjunto.")


# Exercicio 03

# frutas_vermelhas = set()
# frutas_vermelhas.add("morango")
# frutas_vermelhas.add("cereja")
# frutas_vermelhas.add("framboesa")

# print(frutas_vermelhas)


# Exercicio 04

# frutas_vermelhas = {"morango", "cereja", "framboesa"}
# frutas_vermelhas.discard("cereja")

# print(frutas_vermelhas)


# Exercicio 05

# conjunto_A = {1, 2, 3, 4, 5}
# conjunto_B = {6, 7, 8, 9, 10}

# uniao_AB = conjunto_A.union(conjunto_B)
# print(uniao_AB)


# Exercicio 06

# A = set()
# B = set()

# print("Digite 3 elementos para o Conjunto A:")

# a1 = input("Elemento 1 do Conjunto A: ")
# a2 = input("Elemento 2 do Conjunto A: ")
# a3 = input("Elemento 3 do Conjunto A: ")

# A.add(a1)
# A.add(a2)
# A.add(a3)

# print("\nDigite 3 elementos para o Conjunto B:")

# b1 = input("Elemento 1 do Conjunto B: ")
# b2 = input("Elemento 2 do Conjunto B: ")
# b3 = input("Elemento 3 do Conjunto B: ")

# B.add(b1)
# B.add(b2)
# B.add(b3)

# intersecao = A.intersection(B)

# print("\nInterseção dos Conjuntos A e B:", intersecao)


# Exercicio 07


# lista1 = []
# lista2 = []


# print("Digite 3 elementos para a primeira lista:")
# for i in range(3):
#     item = input(f"Elemento {i+1}: ")
#     lista1.append(item)


# print("\nDigite 3 elementos para a segunda lista:")
# for i in range(3):
#     item = input(f"Elemento {i+1}: ")
#     lista2.append(item)


# conjunto1 = set(lista1)
# conjunto2 = set(lista2)

# uniao = conjunto1.union(conjunto2)

# print("\nUnião dos elementos únicos das duas listas:")
# print(uniao)


# Dicionários e suas características

# dicionario = {
#     'Instituição': 'Infinity School',
#     'Curso': 'Dev Full Stack',
#     'Modulo' : 'Python'
# } 


# print(dicionario)
# print(type(dicionario))