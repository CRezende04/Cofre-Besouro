contato = {}

nome = input("Digite o nome do contato: ")
telefone = int(input("Digite o número de telefone: "))
email = input("Digite o endereço de email: ")

contato['nome'] = nome
contato['telefone'] = telefone
contato['email'] = email

print("\nInformações do contato:")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")