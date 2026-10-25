import flet as ft
import Telas.Util as Util
from flet.controls.alignment import Alignment
from Controles.Controle_cadastro import cadastrar,ja_cadastrado



def criar_componentes():

    logo  = ft.Image(
        src = "imagens/logo.png",
        width = 120,
        height = 120
        )

    nome = Util.criar_campo("Nome",ft.Icons.PERSON_OUTLINED)
    cpf = Util.criar_campo("CPF",ft.Icons.BADGE_OUTLINED)
    email = Util.criar_campo("Email",ft.Icons.EMAIL_OUTLINED)
    senha = Util.criar_campo("Senha",ft.Icons.LOCK_OUTLINED,True)
    confirmar_senha = Util.criar_campo("Confirmar Senha",ft.Icons.LOCK_OUTLINED,True)
    
    return logo,nome,cpf,email,senha,confirmar_senha
def criar_conteudo():

    logo,nome,cpf,email,senha,confirmar_senha = criar_componentes()
    botao_cadastrar = Util.criar_botao_Principal(
        "Cadastar",
        lambda e: cadastrar(e,nome,cpf,email,senha,confirmar_senha),
    )
    
    
    formulario = ft.Column(
        controls = [
            nome,
            cpf,
            email,
            senha,
            confirmar_senha    
        ],
        spacing = 12
    )
    botao_ja_cadastrado = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls = [
            ft.Container(height=4),

            ft.Row(
                alignment = ft.MainAxisAlignment.CENTER,
                controls = [
                    ft.Container(height = 1,width = 80, bgcolor = "#999B9C"),
                    ft.Text("ou",color = "#999B9C"),
                    ft.Container(height = 1,width = 80, bgcolor = "#999B9C")
                ]
            ),

            ft.Container(
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=1,
                    controls=[
                        ft.Text("Já tenho uma conta", color="#1EDBFF"),
                        ft.Container(width=125, height=1, bgcolor="#1EDBFF")
                    ]
                ),
                on_click =lambda e: ja_cadastrado(e),
                ink=True
                )
        ]
    )
    conteudo = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls =  [
            logo,
            ft.Text(
                "Cadastro",
                color = "#FFFFFF",
                size = 34,
                weight = ft.FontWeight.BOLD,
                font_family = "Inter"
                ),
            ft.Text(
                "Crie sua conta para começar",
                color = "#B8C1D1",
                size = 16,
                font_family = "Inter"
            ),
            ft.Text(
                "Organize suas compras e ",
                color = "#A6AFBD",
                size = 12,
               font_family = "Inter"
                    
            ),
            ft.Text(
                "tenha seus recibos sempre por perto.",
                color = "#A6AFBD",
                size = 12
            ),

            ft.Container(height = 16),
            formulario,
            ft.Container(height = 16),
            botao_cadastrar,
            botao_ja_cadastrado
            
            ],
        spacing = 3)

    return conteudo 
def tela_criar_cadastro():

    conteudo = criar_conteudo()
    fundo = Util.criar_fundo()

    tela_cadastro = ft.Stack(
        controls=[
            fundo,
            conteudo
        ],
        expand=True
    )

    return tela_cadastro
