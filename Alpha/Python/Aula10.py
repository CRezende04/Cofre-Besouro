import flet as ft


# def main(page: ft.Page):
#     page.title = "Estilização Básica"
#     page.add(
#         ft.Text("Texto vermelho", color="red", size=20),
#         ft.ElevatedButton("Botão com estilo", bgcolor="green", color="white")
#     )
# ft.app(target=main)    


# def main(page: ft.Page):
#     page.title = "Aplicando Cores e Fontes"

#     page.add(
#         ft.Text("Texto vermelho", color="red", size=20),
#         ft.Text("Texto Azul e negrito", color="blue", weight="bold", size=24),
#         ft.Text("Texto verde e itálico", color="green", italic=True, size=18)
#     )

# ft.app(target=main)    


# def main(page: ft.Page):
#     page.title = "Utilizando Temas"

#     theme = ft.Theme(
#         color_scheme=ft.ColorScheme(
#             primary=ft.Colors.BLUE,
#             secondary=ft.Colors.RED,
#             background=ft.Colors.BLACK,
#             surface=ft.Colors.GREY,
#             on_primary=ft.Colors.WHITE,
#             on_secondary=ft.Colors.WHITE,
#             on_background=ft.Colors.BLACK,
#             on_surface=ft.Colors.BLACK
#         )
#     )
#     page.theme = theme

#     page.add(
#         ft.Text("Texto com Tema Personalizado"),
#         ft.ElevatedButton("Botão com Tema")
#     )
# ft.app(target=main)


# def main(page: ft.Page):
#     btn = ft.Button(
#         text="Clique Aqui",
#         bgcolor=ft.Colors.BLUE,
#         color=ft.Colors.WHITE,
#         border_radius=8,
#     )
#     page.add(btn)
# ft.app(target=main)

# label = ft.Text(
#     value="Ola Mundo!",
#     color=ft.Colors.RED,
#     size=20,
#     padding=ft.EdgeInsets.all(10),
# )


# Exercicio 01


def main(page: ft.Page):
    page.title = "Textos"
    page.bgcolor = "#161263"
    page.padding = 20

    # Texto 1 - Grande, vermelho, negrito
    texto1 = ft.Text(
        "Texto 1",
        size=30,
        weight=ft.FontWeight.BOLD,
        color="red"
    )

    # Texto 2 - Médio, azul, itálico
    texto2 = ft.Text(
        "Texto 2",
        size=24,
        italic=True,
        color="blue"
    )

    # Texto 3 - Pequeno, verde, normal
    texto3 = ft.Text(
        "Texto 3",
        size=18,
        weight=ft.FontWeight.W_400,
        color="green"
    )

    page.add(
        texto1,
        texto2,
        texto3
    )

ft.app(main)


# # Exercicio 02


# def main(page: ft.Page):
#     page.title = "Botões"
#     page.bgcolor = "#ECEFF1"
#     page.padding = 30

#     # Botão 1 - Vermelho com texto branco e fonte grande
#     botao1 = ft.ElevatedButton(
#         text="Botão 1",
#         bgcolor="red",
#         color="white",
#         style=ft.ButtonStyle(
#             text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
#         )
#     )

#     # Botão 2 - Azul com texto amarelo e fonte média
#     botao2 = ft.ElevatedButton(
#         text="Botão 2",
#         bgcolor="blue",
#         color="yellow",
#         style=ft.ButtonStyle(
#             text_style=ft.TextStyle(size=18, italic=True)
#         )
#     )

#     # Botão 3 - Verde com texto preto e fonte pequena
#     botao3 = ft.ElevatedButton(
#         text="Botão 3",
#         bgcolor="green",
#         color="black",
#         style=ft.ButtonStyle(
#             text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_400)
#         )
#     )

#     page.add(
#         ft.Column(
#             controls=[botao1, botao2, botao3],
#             spacing=15,
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER
#         )
#     )

# ft.app(main)

# # Exercicio 03


# import flet as ft

# def main(page: ft.Page):
#     page.title = "Formulário Estilizado"
#     page.bgcolor = "#F9F9F9"
#     page.padding = 30

#     # Campo Nome
#     nome_input = ft.TextField(
#         label="Nome",
#         border_color="blue",
#         border_radius=10,
#         bgcolor="#E3F2FD",
#         text_style=ft.TextStyle(size=16),
#         width=300
#     )

#     # Campo E-mail
#     email_input = ft.TextField(
#         label="E-mail",
#         border_color="green",
#         border_radius=10,
#         bgcolor="#E8F5E9",
#         text_style=ft.TextStyle(size=16),
#         width=300
#     )

#     # Botão de Envio
#     enviar_btn = ft.ElevatedButton(
#         text="Enviar",
#         bgcolor="purple",
#         color="white",
#         style=ft.ButtonStyle(
#             shape=ft.RoundedRectangleBorder(radius=8),
#             text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)
#         )
#     )

#     page.add(
#         ft.Column(
#             controls=[
#                 ft.Text("Formulário de Contato", size=24, weight=ft.FontWeight.BOLD, color="black"),
#                 nome_input,
#                 email_input,
#                 enviar_btn
#             ],
#             spacing=20,
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER
#         )
#     )

# ft.app(main)


# # Exercicio 04


# def main(page: ft.Page):
#     page.title = "Tema Personalizado"
#     page.padding = 30

#     # Definindo o tema personalizado
#     page.theme = ft.Theme(
#         color_scheme=ft.ColorScheme(
#             primary=ft.colors.BLUE,
#             secondary=ft.colors.ORANGE,
#             background=ft.colors.GREY_100,
#             on_primary=ft.colors.WHITE,
#             on_secondary=ft.colors.BLACK,
#             on_background=ft.colors.BLACK,
#         )
#     )

#     # Aplicando cor de fundo do tema
#     page.bgcolor = page.theme.color_scheme.background

#     # Texto estilizado pelo tema
#     texto = ft.Text(
#         "Exemplo de Tema Personalizado",
#         size=24,
#         weight=ft.FontWeight.BOLD,
#         color=page.theme.color_scheme.on_background
#     )

#     # Botão estilizado pelo tema
#     botao = ft.ElevatedButton(
#         text="Clique Aqui",
#         bgcolor=page.theme.color_scheme.primary,
#         color=page.theme.color_scheme.on_primary,
#         style=ft.ButtonStyle(
#             text_style=ft.TextStyle(size=18, weight=ft.FontWeight.W_600),
#             shape=ft.RoundedRectangleBorder(radius=10)
#         )
#     )

#     page.add(
#         ft.Column(
#             controls=[texto, botao],
#             spacing=20,
#             alignment=ft.MainAxisAlignment.CENTER,
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER
#         )
#     )

# ft.app(main)