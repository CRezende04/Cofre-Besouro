def verificar_par(num):
    if num %2 == 0:
        return f"O número {num} é par."
    else:
        return f"O número {num} é impar." 
    
biblioteca = [
    {"id":1,"titulo":"aneis","autor":"caue","copias":"3","disponivel":True}
]
    

def adicionar_biblioteca():
    tamanho_lista = len(biblioteca)
    novo_id = tamanho_lista + 1
    titulo = input("Titulo da Biblioteca: ")
    autor = input("Autor da Biblioteca: ")
    copias = int(input("Número de Cópias Disponíveis: "))
    disponivel = copias > 0
    
    nova_biblioteca = {
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "copias": copias,
        "disponivel": disponivel
    }
    biblioteca.append(nova_biblioteca)


def listar_livros(biblioteca):
    livros_disponiveis = [livro for livro in biblioteca if livro['disponivel']]

    if not livros_disponiveis:
        print("Nenhum livro disponível.")
        return

    livros_ordenados = sorted(livros_disponiveis, key=lambda livro: livro['titulo'].lower())

    for livro in livros_ordenados:
        print(f'''
Id: {livro['id']}, 
Título: {livro['titulo']}, 
Autor: {livro['autor']},  
Cópias: {livro['copias']}, 
Disponíveis: {livro['disponivel']}''')


def emprestimo_biblioteca():
    id = input("Digite o id do livro para empréstimo: ")
    
    if not id:
        print("ID inválido. O id não pode ser vazio.")
        return
    
    id = int(id)
    
    if id <= 0:
        print("ID inválido. O id deve ser um número positivo.")
        return

    for livro in biblioteca:
        if livro['id'] == id:
            # Converter 'copias' para int antes da comparação
            copias = int(livro['copias'])  # Convertendo 'copias' para int
            if copias > 0:
                livro['copias'] = str(copias - 1)  # Armazenando novamente como string
                if copias - 1 == 0:
                    livro['disponivel'] = False
                print(f"Você emprestou o livro '{livro['titulo']}'.")
                return
            else:
                print("Livro indisponível para empréstimo.")
                return
    print("Livro não encontrado.")

def devolver_biblioteca():
    id = input("Digite o id do livro para devolução: ")
    
    if not id:
        print("ID inválido. O id não pode ser vazio.")
        return
    
    id = int(id)
    
    if id <= 0:
        print("ID inválido. O id deve ser um número positivo.")
        return

    for livro in biblioteca:
        if livro['id'] == id:
            # Converter 'copias' para int antes de realizar a operação de devolução
            copias = int(livro['copias'])  # Convertendo 'copias' para int
            livro['copias'] = str(copias + 1)  # Armazenando novamente como string
            livro['disponivel'] = True
            print(f"Você devolveu o livro '{livro['titulo']}'.")
            return
    print("Livro não encontrado na biblioteca.")

def menu():
    print("\n=======MENU=======")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Emprestimo")
    print("4 - Devolução")
    print("5 - Sair")

def exibir_menu():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-6):")

        if escolha == "1":
           adicionar_biblioteca()
        elif escolha == "2":
            listar_livros(biblioteca)
        elif escolha == "3":
            emprestimo_biblioteca()
        elif escolha == "4":
            devolver_biblioteca()
        elif escolha == "5":
            break
        else:
            print("Opção Inválida. Tente Novamente")