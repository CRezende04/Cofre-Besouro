numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

soma_pares = 0
par = False

for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        soma_pares += i
        par = True
else:
    if not par:
        print("Não há números pares.")

print(f"A soma dos números pares é: {soma_pares}")