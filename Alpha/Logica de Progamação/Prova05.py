numerodealunos = int(input("Digite o numero de Alunos:"))
for i in range(numerodealunos):
    nome = input("Digite o nome do Aluno:")
    soma = 0
    for i in range(1,4):
        nota = float(input(f"Digite a nota {i}:"))
        soma += nota
    media = soma/3
    print(f"Media: {media:.2f}")
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
