#lista nada mais é do que uma variável que consegue guardar mais de um valor ao mesmo tempo, esses valores são separados por virgula, e todos eles possuem uma posição atrelada, essa posição começa sempre do 0

# numeros = [1,2,3,4,5,6,7,8]
# print(numeros[4])


#métodos de lista:
#acrescentar algo na ultima posicao da lista: append()
# numeros.append(9)
# print(numeros)


#remove um elemento da lista passando o elemento: remove()
#obs: remove apenas a primeira ocorrencia do elemento
# numeros.remove(5)
# print(numeros)


#remove pela ultima posição:pop()
# numeros.pop()
# print(numeros)
#numeros.pop(posição) - espera receber a posição do elemento que deve ser removido.
# numeros.pop(4)
# print(numeros)


#método para organizar uma lista:
# nomes = ["Luana","Lucas","Caue","Alex","João"]
# nomes.sort()
# print(nomes)

#METODO PARA REVERTER:
# nomes.reverse()
# print(nomes)


#metodo onde consigo inserir um elemento em qualquer posição:
# nomes.insert(1,"Nath")
# print(nomes)


#como transformar duas listas em apenas uma?

# numeros = [1,2,3,4]
# nums2 = [5,6,7,8,9]
# numeros.extend(nums2)
# print(numeros)


#achar a posição de um elemento na lista.

# lista = [1,2,3,4,5,6,7,8]
# posicao = lista.index(5)
# print(posicao)



#como saber o tamanho da lista:
# print(len(lista))

# tupla = (1,2,3,4,5)
# num1,num2,num3,num4,num5 = tupla
# print(num4)

# conjunto = set()
# dicionario = dict()
# lista = list()
# tupla = tuple()
# conj = {"Nathalia","Alex","João"}
# # # print(conj)
# # conj.discard("infinity")

# # if "nathalia" not in conj:
# #     print("O nome está dentro do conjunto")


# dados = {
#     "nome":"nath",
#     "idade":23,
#     "cidade":"Salvador"
# }


#como adiconar algo em um dicionário?
# dados['profissao'] = ["Desenvolvedora","Professora","SDR"]
# print(dados["profissao"][1])

#para atualizar uma informação em um dicionario
# dados["idade"] = 24
# print(dados)

#para apagar uma informação de um dicionario:

# del dados["idade"]
# print(dados)


# 2. Acessando elementos
# Pergunta:
# Dada a lista animais = ["gato", "afhalksfhacachorro", "coelho", "tigre"], imprima apenas o terceiro elemento da lista.


# animais = ["gato", "afhalksfhacachorro", "coelho", "tigre"]
# print(animais[2])


# ✏️ 3. Alterando valores
# Pergunta:
# Dada a lista cores = ["vermelho", "verde", "azul"], troque o valor "verde" por "amarelo" e imprima a lista.


# cores = ["vermelho", "verde", "azul"]
# cores[1] = "amarelo"
# cores.remove("verde")
# cores.insert(1,"amarelo")
# print(cores)


# ➕ 4. Adicionando elementos
# Pergunta:
# Crie uma lista vazia chamada frutas. Depois, adicione os seguintes itens: "maçã", "banana" e "uva", um por um, e imprima a lista final.


# frutas = []
# frutas.insert("maçã", "banana" e "uva")
# print(frutas)


# ➖ 5. Removendo elementos
# Pergunta:
# Dada a lista itens = ["chave", "carteira", "celular", "moeda"], remova o item "celular" e imprima a nova lista.


# itens = ["chave", "carteira", "celular", "moeda"]
# itens.remove("celular")
# print(itens)


# Exercicio 01

# lista = [1,2,3,4,5]
# nem_lista= list(filter(lambda x: x%2==0, lista))
# print(nem_lista)


# Exercicio 02


# produtos = [
#     {"nome":"pizza","preco":90, "qtd_estoque":5}
# ]
# def adicionar_produto():
#     nome_produto = input("Digite o nome do produto: ")
#     preco_produto = float(input("Digite o preco do produto: "))
#     qtd_produto = int(input("Digite a quantidade em estoque do produto: "))
#     novo_produto = {"nome":nome_produto,"preco":preco_produto,"qtd_estoque":qtd_produto}
#     produtos.append(novo_produto)
#     print(produtos)

# def remover_produto():
#     for i in range(len(produtos)):
#         print(f'{i} - {produtos[i]["nome"]}')
#     escolha_usuario = int(input("DIGITE O NUMERO DO PRODUTO QUE DESEJA REMOVER: ")) 
#     produtos.pop(escolha_usuario)
#     print(produtos)


# def atualizar_produto():
#     for i in range(len(produtos)):
#         print(f'{i} - {produtos[i]["nome"]}')
#     escolha_usuario = int(input("DIGITE O NUMERO DO PRODUTO QUE DESEJA atualizar: "))
#     nome_nvproduto = input("Digite o novo nome do produto: ")
#     preco_nvproduto = float(input("Digite o novo preço do produto: "))
#     qtd_estoque = int(input("digite a nova quantidade em estoque desse produto: "))
#     produto_atualizado = {"nome":nome_nvproduto,"preco":preco_nvproduto,"qtd_estoque":qtd_estoque}
#     produtos[escolha_usuario] = produto_atualizado
#     print(produtos)
# atualizar_produto()


# Exercicio 03

# cores = {"azul", "verde", "rosa", "preto", "branco", "roxo", "amarelo", "cinza", "vermelho", "lilás"}

# def quatro_letras(conjunto):
#     resultado = set()
#     for cor in cores:
#         if len(cor) > 4:
#             resultado.add(cor)
#     return resultado
        

# resultado = quatro_letras(cores)
# print(resultado)


# Exercicio 04

