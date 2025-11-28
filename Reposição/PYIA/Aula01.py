# For

# for variavel in range(inicio, fim , passo):


# Range
# Ate onde ele deve percorrer!

# for i in range(5):
    # print(i)


# Break no For
# Apos validação onde ele deve finalizar caso a condição esteja correta.


# numero_procurado = 7
# for i in range(1,11):

    # if i == numero_procurado
        # print(f"Numéro {numero_procurado} encontrado!")
        # break
    # print(i)


# Continue no For
# Apos a validação esta correta o codigo deve continuar a ler a proximas linhas de codigo.

# for i in range(1,11):
    # if 1 % 2 != 0:
        # continue
    # print(i)


# Break e continue
# Se a validação estiver correta ela finaliza ali, caso contrario continuara lendo ate que a validação esteja correto e finalizar.

# for num in range(2,20):
    # for i in range(2, num):
        # if num % i == 0:
            # break
    # else:
        # print(f"{num} é um número primo!")


# Listas e suas características

# Definindo uma lista de Números
# lista_de_numeros = [1,2,3,4,5]

# Definindo uma lista de Letras
# lista_de_letras = ['a','e','i','o','u']

# Definindo uma lista de valores logicos
# lista_de_logicos = [True, False, False, True]

# Lista com Diferentes tipos de dados
# lista_mista = ['Gabriel', 12, True]


# Exercicio 01

# lista_numeros = [1,2,3,4,5]
# print(lista_numeros)


# Exercicio 02

# lista_vogais = ['a','e','i','o','u']
# print(lista_vogais)


# Definindo e exibindo valores de uma lista

# notas = [10.0,9.8,8.7]


# Exercicio 03

# lista_itens = ['RZ','a',5,3.5,True]
# print(lista_itens[2])


# Acessando valores de uma lista

# letras = ['a','b','c','d','e']

# print(letras[-1])
# print(letras[-2])
# print(letras[-3])
# print(letras[-4])
# print(letras[-5])


# Métodos para manipulação de listas

# Adição de itens ".append()"
# Adição de itens ".insert()"

# Remoção de itens ".remove()"
# Remoção de itens ".pop()"

# numeros = [1,2,3,4,5]

# numeros.append(6)
# print(numeros)

# numeros = [10,30,40,50]
# letras = ['a','e','o','u']
# pesos = [1.2,3.4,5.3,6.7]

# numeros.insert(1,20)
# letras.insert(2,'i')
# pesos.insert(2,4.0)

# print(numeros)
# print(letras)
# print(pesos)


# notas = [
#     9.0,
#     8,7,
#     9.9,
#     8.7,
#     7.9
# ]

# notas.pop(0)
# notas.pop(1)
# notas.pop(2)

# print(notas)


# Iterando listas em Python com FOR

# lista_compras = [
    # "2 pcts. de Arroz",
    # "6 pcts. de Feijão",
    # "2 pcts. de Farinha de Mandioca",
    # "4kg de Linguiça Calabresa",
    # "4kg de Charque",
    # "2kg de Bacon de Barriga",
    # "2kg de Pé e Orelha de Porco",
    # "1 pct de folha de louro",
    # "6 mói de couve"
    # "5kg de laranja"
# ]

# print("Lista de Compras", end='\n\n')

# for item in lista_compras:
    # print("[ ]", item)


# Definindo e exibindo valores de uma tupla:

# Lista Mútavel
# minha_lista = [1,2,3,4,5]
# minha_lista[0] = 10
# print(minha_lista)

# Tupla Imutável
# minha_tupla = (1,2,3,4,5)
# print(minha_tupla)

# Métodos para a Manipulação de Tuplas

# frutas = ('maçã','banana','laranja','abacaxi')

# indice_laranja = frutas.index('laranja')
# print("Indice da Laranja:", indice_laranja)

# quantidade_bananas = frutas.count('banana')
# print("Quantidade de bananas:", quantidade_bananas)

# maca, banana, laranja, abacaxi = frutas
# print("Fruta 1:",maca)
# print("Fruta 2:",banana)
# print("Fruta 3:",laranja)
# print("Fruta 4:",abacaxi)

# Exercicio 01 GPT


# numeros = [10, 20, 30, 40]
# soma = 0
# quantidade = 0

# for n in numeros:
#     soma += n
#     quantidade += 1   # conta os elementos manualmente

# media = soma / quantidade
# print(media)


# Exercicio 02 GPT


# lista = [1, 2, 2, 3, 4, 4, 5]
# nova_lista = []

# for item in lista:
#     existe = False
#     for x in nova_lista:     # verifica manualmente se já existe
#         if x == item:
#             existe = True
#             break
#     if not existe:
#         nova_lista.append(item)

# print(nova_lista)


# Exercicio 03 GPT


# lista = [1, 2, 3, 4, 5]
# invertida = []
# tamanho = 0


# for _ in lista:
#     tamanho += 1


# for i in range(tamanho-1, -1, -1):
#     invertida.append(lista[i])

# print(invertida)


# Exercicio 04 GPT


# lista = [5, 2, 8, 1, 4, 7]
# pares = []


# for n in lista:
#     if n % 2 == 0:
#         pares.append(n)


# qtd_pares = 0
# for _ in pares:
#     qtd_pares += 1


# for i in range(qtd_pares):
#     for j in range(i+1, qtd_pares):
#         if pares[i] > pares[j]:
#             pares[i], pares[j] = pares[j], pares[i]

# resultado = []
# indice = 0

# for n in lista:
#     if n % 2 == 0:
#         resultado.append(pares[indice])
#         indice += 1
#     else:
#         resultado.append(n)

# print(resultado)


# Exercicio 05 

# lista = [1, 2, 3, 4]
# somas = []
# tamanho = 0


# for _ in lista:
#     tamanho += 1

# for i in range(tamanho-1):
#     somas.append(lista[i] + lista[i+1])

# print(somas)

# Exercicio 06 GPT

# numeros = [0,1,2,3,4,5,6,7,8,9,10]
# resultado = []
# for i in range(0, len(numeros) -1,2):
#     soma = numeros[i] + numeros[i + 1]
#     resultado.append(soma)


# Exercicio 04

# palestrantes = (("Ana Silva", "Inteligência Artificial na Educação", "Universidade Federal de São Paulo"),
#     ("Bruno Costa", "Cibersegurança e Privacidade de Dados", "Instituto Tecnológico de Aeronáutica"),
#     ("Carla Mendes", "Sustentabilidade e Inovação", "Universidade de Campinas")
#     )
# print(palestrantes[2])


# Desafui Pratico


# resultados = [
#     ("Equipe A", [8, 9, 7]),
#     ("Equipe B", [6, 5, 7]),
#     ("Equipe C", [9, 8, 10]),
#     ("Equipe D", [5, 6, 6])
# ]

# classificacao = []
# for equipe, notas in resultados:
#     media = sum(notas) / len(notas)
#     classificacao.append((equipe, media))

# for i in range(len(classificacao)):
#     for j in range(len(classificacao)):
#         if classificacao[i][1] > classificacao[j][1]:
#             classificacao[i], classificacao[j] = classificacao[j], classificacao[i]


# print("Classificação Final:")
# for item in classificacao:
#     print(f"{item[0]} - média: {item[1]:.2f}")




