# INTRODUÇÃO AO WHILE

# while <condição>:

# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1
# # Saida 1, 2, 3, 4, 5


# FUNCIONAMENTO DO WHILE

# soma = 0
# numero = 1
# while numero <= 10:
#     soma += numero
#     numero += 1
#     print("A soma dos numeros de 1 a 10 é:", soma)
# Saida A soma dos numeros de 1 a 10 é: 55


# APLICAÇÃO DO WHILE

# senha = ""
# while senha != "1234":
#     senha = input("Insira a senha:")
#     print("Senha correta!")


# Exercicio 1

# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1


# Exercicio 2

# contador = 1
# soma = 0
# while contador <= 100:
#     soma += contador
#     contador += 1
#     print("A soma dos numeros de 1 a 100 é:", soma)


# Exercicio 3

numero = int(input("Digite um numero para ver a tabuada:"))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} * {contador} = {resultado}")
    contador += 1


# Exercicio 4

# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1
# print("Feliz Ano Novo!")


# WHILE + CONDICIONAIS

# while condicao:
#     if condicao1:
#         # Bloco de codigo se condicao1 for verdadeira
#     elif condicao2:
#         # Bloco de codigo se condicao2 for verdadeira
#     else:
#         # Bloco de codigo se nenhuma das condicoes for verdadeira
#     # Outras ações ou atualizações de variesveis para evitar o loop infinito


# Repetição com Condições Dinâmicas

# contador = 0
# limite = 10
# while contador < limite:
#     print(contador)
#     contador += 1


# Interatividade e Verificação de Entrada

# senha = ""
# while senha != "12345":
#     senha = input("Digite a senha:")
#     if senha == "12345":
#         print("Acesso Concedido!")
#     else:
#         print("Senha Incorreta, tente novamente.")


# Implementação de Menus Interativos

# opcao = ""
# while opcao != "sair":
#     print("Menu:")
#     print("1. Opção 1")
#     print("2. Opção 2")
#     print("Digite 'sair' para encerrar")
#     opcao = input("Escolha uma opção: ")
#     if opcao == "1":
#         print("Você escolheu a Opção 1.")
#     elif opcao == "2":
#         print("Você escolheu a Opção 2.")
#     elif opcao == "sair":
#         print("Encerrando o programa")
#     else:
#         print("Opção inválida, tente novamente.")


# Exercicio 5

# numero = int(input("Digite um numero:"))
# contador = 1
# while contador <= numero:
#     contador += 1
#     if contador % 2 == 1:
#         print(f"{contador}")


# Exercicio 6

# numero = 0
# soma = 0

# while numero >= 0:
#     numero = int(input("Digite um numero positivo (ou negativo para sair):"))
#     if numero >= 0:
#         soma += numero
# print("A soma total dos numeros positivos é:", soma)


# Exercicio 7

# numero = int(input("Digite um numero positivo:"))
# contador = 1
# while contador <= 10:
#     resultado = numero * contador
#     if resultado %3==0:
#         print(resultado)
#     contador += 1


# Exercicio 8

# soma = 0
# quantidade = 0
# nota = float(input("Digite a nota do aluno (ou -1 para sair): "))

# while nota != -1:
#     soma += nota
#     quantidade += 1
#     nota = float(input("Digite a nota do aluno (ou -1 para sair): "))

# if quantidade > 0:
#     media = soma / quantidade
#     print(f"Media das notas é: {media:.2f}")
# else:
#     print("Insira uma nota.")


# WHILE + BREAK

# while condicao:
#     if condicao_para_interromper:
#         break
#     # mais codigo do bloco while



# numero = int(input("Digite um numero:"))
# contador = 1

# while contador <= numero:
#     print(contador)
#     contador += 1
#     if contador > numero:
#         break


# WHILE + ELSE

# while condicao:
#     # Bloco de codigo a ser repetido
#     if condicao_para_parar:
#         break
# else:
    # Bloco de codigo eexecutado se o laço não for interrompido por 'Break'



# numero_secreto = 7
# palpite = 0

# while palpite != numero_secreto:
#     palpite = int(input("Adivinhe o numero secreto (entre 1 e 10): "))
#     if palpite == numero_secreto:
#         print("Parabéns! Você acertou.")
#         break
#     else:
#         print("Errado.Tente novamente!")


# VANTAGENS DO USO DE BREAK EM WHILE

# senha_correta = "senha123"
# tentativa = ""

# while tentativa != senha_correta:
#     tentativa = input("Digite a senha: ")
#     if tentativa == senha_correta:
#         print("Senha correta! Acesso concedido.")
#         break
#     else:
#         print("Senha incorreta. Tente novamente.")


# Exercicio 9

# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1


# Exercicio 10

# numero = 1
# soma = 0

# while numero < 50 or numero > 50:
#     soma += numero
#     numero += 1
#     print(numero)


# Exercicio 11

# numero = int(input("Digite um numero de 1 a 10:"))
# while numero < 1 or numero > 110:
#     print("Numero invalido. Tente novamente.")
#     numero = int(input("Digite um numero de 1 a 10:"))


# Exercicio 12

# senha = input("Digite a senha: ")
# while senha != "1234":
#     print("Senha incorreta. Tente novamente.")
#     senha = input("Digite a senha:")



# ANINHAMENTO DE WHILE

# while condicao_externa:
    # Bloco de código do loop externo
    # while condicao_interna:
        # Bloco de código do loop interno
        # Pode haver uma logica para modificar a condicao interna e pode haver uma logica para modificar a condicao externa


# numero_secreto = 7
# tentavias_totais = 3
# jogador1_tentativas = 0
# jogador2_tentativas = 0

# while jogador1_tentativas < tentavias_totais and jogador2_tentativas < tentavias_totais:
#     palpite1 = int(input("Jogador 1, adivinhe o numero:")
#     jogador1_tentativas += 1
#     if palpite1 == numero_secreto:
#         print("Jogador 1 acertou!")
#         break
#     else:
#         print("Jogador 1 errou. Tente novamente.")
    
#     palpite2 = int(input("Jogador 2, adivinhe o numero:"))
#     jogador2_tentativas += 1
#     if palpite2 == numero_secreto:
#         print("Jogador 2 acertou!")
#         break
#     else:
#         print("Jogador 2 errou. Tente novamente.")
# else:
#     print("Nenhum jogador acertou o numero secreto.")


# LOOPS INFINITY

# contador = 0
# while contador < 5:
#     print("Este é um loop infinito!")
# A variável contador nunca é incrementada, então contador < 5 é sempre verdadeiro, resultando em um loop infinito.


# Estrutura ‘while True’

# while True:
#     print("\nMenu:")
#     print("1. Diga Olá")
#     print("2. Diga Adeus")
#     print("Digite 'sair' para terminar o programa")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         print("Olá!")
#     elif opcao == "2":
#         print("Adeus!")
#     elif opcao.lower() == "sair":
#         print("Encerrando o programa.")
#         break
#     else:
#         print("Opção inválida, tente novamente.")


# Desafios Praticos

# Desafio 1

# numero = 1
# soma = 0
# while numero <= 100:
#     if numero % 2 == 0:
#         soma += numero
#     numero += 1
# print("A soma dos numeros pares de 1 a 100 é:", soma)

# Desafio 2

# numero = 1
# while numero <= 50:
#     if numero % 2 == 1:
#         print(numero)
# numero += 1

# gustavo guanabara
# https://www.youtube.com/c/CursoemV%C3%ADdeo/playlists
# dio
# python tutor
