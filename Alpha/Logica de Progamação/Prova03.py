numero_secreto = 5
tentavias_totais = 3
jogador_tentativas = 0

while jogador_tentativas < tentavias_totais:
    tentativas_restantes = tentavias_totais - jogador_tentativas
    palpite = int(input(f"Adivinhe o numero(Tentativas Total:{tentativas_restantes}):"))
    jogador_tentativas += 1
    if palpite == numero_secreto:
        print("Parabens Você acertou!")
        break
    else:
        print("Você errou. Tente novamente!")
else:
    print(f"Acabou suas tentativas. Mais sorte na Proxima! Numero Secreto era {numero_secreto}.")