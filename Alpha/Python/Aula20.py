# ______________________________________________________ Modulo de Python ____________________________________________________________


# O que é lista?
#é uma variável que guarda mais de um valor ao mesmo tempo. Cada um desses valores, tem uma posição (índice, index), e sempre começa com 0


# lista = ["Nath",1,1.75,True,[]]
# print(lista[0])

#como adicionar algo no final da lista?
#append significa acrescentar e ele adiciona algo ao final da lista, mas apenas um por vez!
# lista.append("Jonathan")
# print(lista)

#função e método:

#Função: é um comando que faz alguma coisa, mas não depende do tipo da informação

#Método:  é um comando que faz alguma coisa mas DEPENDE do tipo da informação

# nome = 'nathalia'
# print(nome.upper())


#como adicionar algo em qualquer posição da lista?
# lista = ["Nath",1,1.75,True,[]]
# lista.insert(4,"Infinity School")
# print(lista)

#como remover algo de uma lista?
# lista = ["Nath",1,1.75,True,[]]

#pop() - o pop() sem valor nos parenteses, remove o ultimo elemento da lista.
# lista.pop()
# print(lista)

#pop(posição)
# lista.pop(3)
# print(lista)

# numeros = [1,2,3,4,5,5,5,6,7,8]
# numeros.remove(5)
# print(numeros)
#remove() - ele espera receber o valor do elemento que voce quer remover, mas tem a seguinte observação, ele so remove a primeira ocorrencia do elemento

# nomes = ["Jonathan","Lucrécio","Matheus","Alexsander","Nathalia","Paulo","Oswaldo"]
# for nome in nomes:
#     print(nome)

# nomes.extend(["Cristiane","Bárbara","Erick"]) - Adiciona mais de um elemento ao final da lista, mas esses elementos precisam estar dentro de outra lista
# print(nomes)

# nomes.sort() - organiza uma lista do menor para o maior ou em "ordem alfabética"
# print(nomes)


# numeros = [1,2,2,2,2,3,4,5,6,7,7,7,8]
# print(numeros.count(7)) - conta quantas vezes o elemento  dentro dos parenteses aparece na lista


# nomes.reverse() - Reverte a lista
# print(nomes)


# print(numeros.index(4))

# nomes.clear() - Limpa a lista
# print(nomes)


#como saber o tamanho da lista?
# print(len(numeros))



