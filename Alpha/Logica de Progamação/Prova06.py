usuario = "admin"
senha = "admin123"
tentativa = 3
while tentativa > 0: 
    login = input("Insira o usuario:")
    key = input("Insira a Senha:") 
    if login == usuario and key == senha:
        print("Seja Bem vindo Tricolor")
        break
    else:
        tentativa -= 1
        print("Usuario ou Senha incorreta")
if tentativa == 0:
    for i in range(3):
        print("Acesso Bloqueado")