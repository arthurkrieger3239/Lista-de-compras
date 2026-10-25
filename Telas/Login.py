import flet as ft
from flet.controls.alignment import Alignment
import Telas.Util as Util
from Controles import Controle_cadastro,Controle_logar


def carregar_componentes():

    logo = ft.Image(
        src = "imagens/logo.png",
        height = 120,
        width = 120
    )

    email = Util.criar_campo("Insira o seu email", ft.Icons.EMAIL_OUTLINED)
    senha = Util.criar_campo("Insira a sua senha", ft.Icons.KEY_OFF_OUTLINED,password=True)

    return logo, email,senha  

def criar_conteudo():
    logo,email,senha = carregar_componentes()

    async def clicar_logar(e):
        await Controle_logar.logar(e,email,senha,lembrar)

    carregar_logo = ft.Column(
        controls =[
            logo
        ],
        spacing = 12,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        
    )

    botao_esqueci_senha = Util.criar_botao_Texto("Esqueci minha senha",Controle_cadastro.trocar_senha,cor_letra = "#12A8FF",tamanho_letra = 14)
    botao_logar = Util.criar_botao_Principal("Logar",clicar_logar,icone_texto = ft.Icons.ARROW_FORWARD)
    botao_cadastrar = Util.criar_botao_Texto("Cadastrar-se",Controle_logar.nao_cadastrado,cor_letra = "#12A8FF")
    lembrar = ft.Checkbox(label = "Lembrar de mim", value = False,active_color="#12A8FF",label_style= ft.TextStyle(color = "#FFFFFF", size = 12))
    opcoes_login = ft.Row(
        controls = [
            lembrar,
            botao_esqueci_senha
        ]
    )

    formulario = ft.Column(
        controls =[
        email,
        senha,
        opcoes_login,
        botao_logar,
        
        ],
        spacing = 12,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    )
    retangulo_fundo = ft.Container(
            content = formulario,
            width = 330,
            height = 265,
            padding = 20,
            border_radius = 25,
            bgcolor="#082548",
            border=ft.Border.all(1, "#1C4D7A")
        )

    conteudo= ft.Column(
        controls = [
            ft.Container(height = 30),
            carregar_logo,
            ft.Text("Bem vindo de volta!",color = "#FFFFFF",size = 32, weight = ft.FontWeight.BOLD),
            ft.Text("Entre para continuar",size = 21, color = "#999999"),

            ft.Container(height = 12),
            retangulo_fundo,
            ft.Text(value = "Ainda não possui uma conta?",size = 15,color = "#999999"),
            botao_cadastrar

        ],
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        expand = True,
        width = float("inf"),
    )
    
    return conteudo

def tela_login():

    fundo = Util.criar_fundo()
    conteudo = criar_conteudo()

    tela_Login = ft.Stack(
        controls = [
            fundo,
            conteudo
        ],
        expand = True
    )

    return tela_Login
