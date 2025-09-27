tarefas = [
    {"id":1,"nome":"limpar a casa","descricao":"Muito bagunçado",
    "prioridade":1,"categoria":1,"concluida":True}
]
    

def adicionar_tarefa():
    tamanho_lista = len(tarefas)
    novo_id = tamanho_lista + 1
    nome = input("Nome da Tarefa: ")
    descricao = input("Descrição da Tarefa: ")
    prioridade = int(input("Nivel da Prioridade de 1 a 3 (1-Pequena | 2-Media | 3-Grande): "))
    categoria = int(input("Nivel da Categoria de 1 a 4 (1-Pessoal | 2-Profissional | 3-Financeiro | 4-Lazer): "))
    concluida = False
    
    nova_tarefa = {
        "id": novo_id,
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": concluida
    }
    tarefas.append(nova_tarefa)


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma Tarefa")
        return
    
    for tarefa in tarefas:
        print(f'''
            Id: {tarefa['id']}, 
            Nome: {tarefa['nome']}, 
            Descrição: {tarefa['descricao']},  
            Prioridade: {tarefa['prioridade']}, 
            Categoria: {tarefa['categoria']}, 
            Concluida: {tarefa['concluida']}''')


def prioridade():
    tarefas_ordenadas = sorted(tarefas, key=lambda t: t['prioridade'], reverse=True)
    
    for t in tarefas_ordenadas:
        print(f'''ID: {t['id']}, 
              Nome: {t['nome']},  
              Descrição: {t['descricao']},  
              Prioridade: {t['prioridade']}, 
              Concluída: {'Sim' if t['concluida'] else 'Não'}''')


def concluidas(id_tarefa):
    for tarefa in tarefas:
        if tarefa["concluida"] == False: 
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                print(f"Tarefa {id_tarefa} marcada como concluída.")
                return
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
        else:
            print(f"Tarefa com ID {id_tarefa} ja esta finalizada.")


def menu():
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Prioridade")
    print("4 - Concluida")
    print("5 - Sair")


def exibir_menu():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-6):")

        if escolha == "1":
           adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            prioridade()
        elif escolha == "4":
            id_tarefa_concluida = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
            concluidas(id_tarefa_concluida)
        elif escolha == "5":
            break
        else:
            print("Opção Inválida. Tente Novamente")
exibir_menu()