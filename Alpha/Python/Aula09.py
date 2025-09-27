import flet as ft

# def main(page: ft.page):
#     ola = ft.Text(value="Olá Mundo!", size = 30)
#     page.controls.append(ola)
#     page.update()

# ft.app(target = main)


# def main(page: ft.Page):
#     page.title = "Minha Aplicação"
#     page.add(
#         ft.Text("Bem vindo ao Flet!"),
#         ft.ElevatedButton(
#             "Clique Aqui", on_click=lambda _: page.add(ft.Text("Botão Clicado!")))
#     )

# ft.app(target=main)


# def main(page: ft.Page):
#     page.title = "Minha Aplicação Flet"
    
#     layout = ft.Column(
#     controls=[
#         ft.Text("Janela Principal", size=20, weight=ft.FontWeight.BOLD),
#         ft.ElevatedButton("Botão 1"),
#         ft.ElevatedButton("Botão 2"),
#         ft.ElevatedButton("Botão 3"),
#     ]
#     )

#     page.add(layout)

# ft.app(target=main)


# def main(page: ft.Page):
#     page.title = "Meu Login"
#     layout = ft.Column(
#         controls=[
#             ft.TextField(label="Nome"),
#             ft.TextField(label="Sobrenome"),
#             ft.TextField(label="Email")
#         ]
#     )
#     page.add(layout)
    
# ft.app(target=main)


# def main(page: ft.Page):  # Função principal da aplicação
#     page.title = "Lista de Tarefas"  # Define o título da página

#     tarefas = []  # Lista que vai guardar os elementos visuais (as tarefas)

#     # Função para adicionar uma nova tarefa
#     def adicionar_tarefa(e):
#         if campo_tarefa.value:  # Só adiciona se o campo não estiver vazio
#             nova_tarefa = ft.Checkbox(label=campo_tarefa.value)  # Cria um checkbox com o texto da tarefa
#             tarefas.append(nova_tarefa)  # Adiciona à lista de tarefas
#             atualizar_lista()  # Atualiza a interface
#             campo_tarefa.value = ""  # Limpa o campo de texto
#             page.update()

#     # Função para remover tarefas concluídas
#     def remover_concluidas(e):
#         # Remove da lista todas que estiverem marcadas (checked)
#         tarefas[:] = [t for t in tarefas if not t.value]
#         atualizar_lista() 

#     # Atualiza a exibição da lista na interface
#     def atualizar_lista():
#         lista_tarefas.controls = tarefas  # Atualiza os controles visuais
#         page.update()

#     # Campo de texto para digitar a nova tarefa
#     campo_tarefa = ft.TextField(label="Nova Tarefa", width=300)

#     # Botão para adicionar a tarefa
#     botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar_tarefa)

#     # Botão para remover as tarefas concluídas
#     botao_remover = ft.ElevatedButton("Remover Concluídas", on_click=remover_concluidas)

#     # Coluna onde as tarefas vão aparecer
#     lista_tarefas = ft.Column()

#     # Adiciona tudo à página
#     page.add(
#         ft.Row([campo_tarefa, botao_adicionar, botao_remover]),  # Primeira linha com o input e botões
#         lista_tarefas  # Coluna com a lista de tarefas
#     )

# # Inicializa o app
# ft.app(target=main)
    
    
# def main(page: ft.Page):
#     page.title = "Calculadora"
#     lista_tarefas = ft.Column()
#     numeros = []
    
#     def somar(e):
#         if campo_numero.value:
#             numero = ft.Checkbox(label=campo_numero.value)
#             numeros.append(numero)
#             atualizar_lista()
#             campo_numero.value = ""
#             page.update()
#     campo_numero = ft.TextField(label="")
#     botao_somar = ft.ElevatedButton("Adicionar", on_click=somar)
    
    
#     def subtracao(e):
#         atualizar_lista() 
        


#     def limpar():
#         lista_numeros.controls = numeros
#         page.update()

#     campo_tarefa = ft.TextField(label="Nova Tarefa", width=300)

#     botao_somar = ft.ElevatedButton("+", on_click=somar)

#     botao_remover = ft.ElevatedButton("-", on_click=subtracao)

#     botao_dividir = ft.ElevatedButton("-", on_click=dividir)

#     botao_limpar = ft.ElevatedButton("CE", on_click=limpar)

#     lista_numeros = ft.Column()

#     page.add(
#         ft.Row([campo_tarefa, botao_somar, botao_remover, botao_dividir, botao_limpar]),
#         lista_numeros
#     )

# ft.app(target=main)

