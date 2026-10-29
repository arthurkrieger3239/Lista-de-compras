import flet as ft
import Telas.Inicio
import Controles.Controle_acessar_usuario
from Telas.Util import criar_botão_icone
def criar_botao(texto,icone,cor_letra,funcao):

    estrutura_inicio = ft.Row(
            controls=[
                ft.Icon(icon=icone,size=25,color=cor_letra),
                ft.Text(texto,color=cor_letra)
            ]
        )
    if funcao != Controles.Controle_acessar_usuario.sair_conta:

        estrutura = ft.Row(
            controls=[
                estrutura_inicio,
                ft.Icon(ft.Icons.CHEVRON_RIGHT,size=25,color=cor_letra)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    else:
        estrutura=estrutura_inicio

    botao = ft.Container(
        content= estrutura,
        ink=True,
        ink_color="#407DD3FC",
        on_click=funcao
    )

    return botao

def Tela_acessar_usuario():
    page = ft.context.page
    largura_tela = page.width* 0.70

    

    tela_fundo = ft.Container(
        expand=True,
        left=0,
        right=0,
        top=0,
        bottom=0,
        bgcolor=ft.Colors.with_opacity(0.55,ft.Colors.BLACK),
    )

    fechar = ft.Row(
        controls=[
            ft.Text("Minha conta",size=20,color = "#FFFFFF",weight=ft.FontWeight.W_600),
            criar_botão_icone(ft.Icons.CLOSE,lambda e: Controles.Controle_acessar_usuario.fechar_aba(e, Menu, tela_fundo))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    espaco = ft.Container(
        height=1,
        width=largura_tela,
        bgcolor="#24618F"
    )
    
    conteudo = ft.Column(
        controls=[
            fechar,
            espaco,
            criar_botao("Meus dados",ft.Icons.PERSON,"#FFFFFF",Controles.Controle_acessar_usuario.ver_dados),
            criar_botao("Sair da conta",ft.Icons.LOGOUT,"#FF5252",Controles.Controle_acessar_usuario.sair_conta)
        ],
        spacing=20
    )

    Menu = ft.Container(
        content=conteudo,
        width= largura_tela,
        bgcolor= "#001F3F",
        top=0,
        right=0,
        bottom=0,
        border_radius=15,
        border=ft.Border.all(width=1,color="#24618F"),
        padding=20
    )
    
    acesar_usuario = ft.Stack(
        controls=[
            Telas.Inicio.tela_inicial(),
            tela_fundo,
            Menu
        ],
        expand=True
    )

    return acesar_usuario