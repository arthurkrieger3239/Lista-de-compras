from Telas import Util
from Controles.Controle_Inicio import acessar_usuario,Get_gastos,Get_proporcao_gasto_orcamento,Nova_compra,Historico
from Navegacao import navegacao
import Controles.Controle_Inicio as controle
import flet as ft

def criar_componenetes(função : str):

    logo  = ft.Image(
        src = "imagens/logo.png",
        width = 60,
        height = 60
        )

    if função == "topo":
        return logo
def criar_topo():

    logo = criar_componenetes("topo")
    texto = ft.Text("Compras",size = 21,color= "#FFFFFF",weight = ft.FontWeight.BOLD)
    botao_usuario = Util.criar_botão_icone(ft.Icons.PERSON,acessar_usuario)
    texto.expand = True
    topo_inicio = ft.Row(controls = [logo,texto],spacing = 0,expand=True)
    topo_fim = ft.Row(controls = [botao_usuario])

    topo = ft.Row(
        controls = [
            topo_inicio,
            topo_fim
        ],
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )

    return topo
def criar_campo_gastos():

    icone_carteira = ft.Container(
        height = 30,
        width = 30,
        bgcolor = "#0C3574",
        border_radius=15,
        content = ft.Icon(icon = ft.icons.Icons.WALLET_OUTLINED,size = 25,color = "#AEC1CC")
        )
    valor_gasto = Get_gastos()

    proporcao = Get_proporcao_gasto_orcamento()
    preenchido = round(max(0, min(1, proporcao)) * 10000)
    segmentos = []
    if preenchido > 0:
        segmentos.append(ft.Container(
            expand=preenchido,
            border_radius=15,
            gradient=ft.LinearGradient(colors=["#1677FF", "#12DFF3"]),
        ))
    if preenchido < 10000:
        segmentos.append(ft.Container(expand=10000 - preenchido))

    barra = ft.Container(
        height=12,
        border_radius=15,
        bgcolor="#1556B8",
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=ft.Row(
            controls=segmentos,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
    )

    coluna = ft.Column(
        controls=[
            ft.Text("Gastos deste Mês",color = "#FFFFFF",size = 15,weight=ft.FontWeight.W_500),
            ft.Text(f"R$ {valor_gasto}",size = 20,color= "#FFFFFF",weight = ft.FontWeight.BOLD)
        ],
        spacing= 0,
        expand=True,
    )
    linha = ft.Row(
        controls=[
            icone_carteira,
            coluna
    ])

    campo_gastos = ft.Container(
        padding = 10,
        border_radius = 15,
        bgcolor="#052B57",
        border = ft.Border.all(width=1,color = "#006DC0"),
        
        content = 
            ft.Column(
                spacing = 8,
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    linha,
                    ft.Text(f"{proporcao*100}% do orçamento",size=10,color="#3387CC"),
                    barra
                ]),
    
        
    )
    return campo_gastos
def criar_botoes():
    nova_compra = Util.criar_botao_coluna("Nova compra",Nova_compra,icone = ft.Icons.ADD_SHOPPING_CART,largura_container=None)
    historico = Util.criar_botao_coluna("Histórico",Historico,icone = ft.Icons.HISTORY,largura_container=None)
    nova_compra.expand = True
    historico.expand = True

    botoes = ft.Row(
        controls = [
            nova_compra,
            historico
        ],
        spacing = 15
    )

    return botoes
def lista_compras():
    icone = ft.Container(
        content = ft.Icon(ft.Icons.CHECKLIST_OUTLINED,size = 20,color = "#00CFFF" ),
        width=  40,
        height= 40,
        border_radius=15,
        bgcolor = "#073B80",
        border=ft.Border.all(width=1,color="#24618F")
        
        )
    itens_atuais,itens_totais = controle.Get_itens()
    coluna = ft.Column(
        controls=[
            ft.Text("Listas de compras",size = 15,color = "#FFFFFF",weight=ft.FontWeight.BOLD),
            ft.Text(f"{itens_atuais} de {itens_totais} itens",color = "#A8D4FF",size = 10)
        ],
        spacing = 0,
        expand=True,
    )
    linha = ft.Row(
        controls = [
            icone,
            coluna
        ],
        spacing = 20
    )
    proporcao = itens_atuais / itens_totais if itens_totais else 0
    preenchido = round(max(0, min(1, proporcao)) * 10000)
    segmentos = []
    if preenchido > 0:
        segmentos.append(ft.Container(
            expand=preenchido,
            border_radius=15,
            gradient=ft.LinearGradient(colors=["#1677FF", "#12DFF3"]),
        ))
    if preenchido < 10000:
        segmentos.append(ft.Container(expand=10000 - preenchido))

    barra = ft.Container(
        height=12,
        border_radius=15,
        bgcolor="#1556B8",
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=ft.Row(
            controls=segmentos,
            spacing=0,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
    )

    botao_principal = Util.criar_botao_Principal("Continar lista",controle.lista_compras,altura_borda=44,largura_borda=None,borda_raio = 15 )
    conteudo = ft.Column(
        controls = [
            linha,
            barra,
            botao_principal
        ],
        spacing = 15,
        tight=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
    lista = ft.Container(
        content = conteudo,
        bgcolor= "#0B315B",
        border_radius = 15,
        border = ft.Border.all(width = 1,color =  "#006DC0"),
        padding= 20
)
    return lista
def criar_compras_recentes():

    botao = Util.criar_botão_icone(ft.Icons.ARROW_FORWARD,controle.Ultimas_compras,altura_container=40,largura_cotainer=40)
    mercado1,mercado2,data1,data2,valor1,valor2 = controle.Get_Ultimas_compras()
    icone = ft.Icon(ft.Icons.SHOPPING_CART,color = "#00CFFF", size = 30)

    coluna_nome1 = ft.Column(
        controls=[
            ft.Text(f"{mercado1}",size=15,color="#FFFFFF"),
            ft.Text(f"{data1}",size = 10,color = "#FFFFFF")
        ],
        spacing=2,
        expand=True,
    )

    coluna_nome2 = ft.Column(
            controls=[
                ft.Text(f"{mercado2}",size=15,color="#FFFFFF"),
                ft.Text(f"{data2}",size = 10,color = "#FFFFFF")
            ],
            spacing=2,
            expand=True,
        )
    
    icone_nome1 = ft.Row(
        controls=[
            icone,
            coluna_nome1
        ],
        expand=3,
    )
    icone_nome2 = ft.Row(
            controls=[
                ft.Icon(ft.Icons.SHOPPING_CART,color = "#00CFFF", size = 30),
                coluna_nome2
            ],
            expand=3,
        )
    linha_nome1 = ft.Row(
        controls=[
            icone_nome1,
            ft.Text(f"{valor1}",size = 18,color="#FFFFFF",expand=2,text_align=ft.TextAlign.RIGHT)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    linha_nome2 = ft.Row(
        controls=[
            icone_nome2,
            ft.Text(f"{valor2}",size = 18,color="#FFFFFF",expand=2,text_align=ft.TextAlign.RIGHT)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        
    )

    linha_compra1 = ft.Container(
        content=linha_nome1,
        bgcolor="#0C3574",
        border_radius=15,
        border = ft.Border.all(width = 1,color =  "#006DC0"),
        padding=10,
    )
    linha_compra2 = ft.Container(
            content=linha_nome2,
            bgcolor="#0C3574",
            border_radius=15,
            border = ft.Border.all(width = 1,color =  "#006DC0"),
            padding=10,
        )
    linha = ft.Row(
        controls=[
            ft.Text("Compras recentes", size=20,color="#FFFFFF",weight = ft.FontWeight.W_600,expand=True) ,
            botao
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    coluna = ft.Column(
        controls = [
            linha,
            linha_compra1,
            linha_compra2
            
        ],
        tight=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
    conteudo = coluna
    compras = ft.Container(
        content = conteudo,
        bgcolor = "#0B315B",
        border_radius = 15,
        border = ft.Border.all(width = 1,color =  "#006DC0"),
        padding= 10
    )

    return compras
def criar_bottom():

    botao1 = Util.criar_botao_coluna("Início",Util.Inicio,ft.Icons.HOUSE,tem_container=False,tamanho_icone=28)
    botao2 = Util.criar_botao_coluna("Lista",Util.Inicio,ft.Icons.CHECKLIST_OUTLINED,tem_container=False,tamanho_icone=28)
    botao3 = Util.criar_botao_coluna("Compras",Util.Inicio,ft.Icons.SHOPPING_CART,tem_container=False,tamanho_icone=28)
    for botao in (botao1, botao2, botao3):
        botao.expand = True

    conteudo = ft.Row(
        controls=[
            botao1,
            botao2,
            botao3
        ],

        spacing=0,
    )

    bottom = ft.Container(
        content = conteudo,
        bgcolor = "#073B80",
        border_radius = 15,
        border=ft.Border.all(width=1,color="#24618F"),
       
    )

    return bottom
def criar_conteudo():

    page = ft.context.page
    nome = page.session.store.get("nome_usuario")
    topo = criar_topo()
    campo_gastos =  criar_campo_gastos()
    campo_botoes = criar_botoes()
    lista = lista_compras()
    compras = criar_compras_recentes()
    bottom = criar_bottom()
   


    # A coluna rolável ocupa o espaço restante; o menu fica sempre no rodapé.
    corpo = ft.Column(
        controls = [
            topo,
            ft.Text(f"Olá {nome.split()[0]}!",size = 25, color = "#FFFFFF", weight = ft.FontWeight.BOLD),
            campo_gastos,
            campo_botoes,
            lista,
            compras,
        ],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )
    conteudo = ft.Container(
        alignment=ft.Alignment.TOP_CENTER,
        content=ft.Container(
            # Largura máxima: as restrições do pai prevalecem em telas menores.
            width=640,
            padding=20,
            content=ft.Column(
                controls=[corpo, bottom],
                spacing=12,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
        ),
    )

    return conteudo

def tela_inicial():

    fundo = Util.criar_fundo()
    conteudo = criar_conteudo()

    tela_inicial = ft.Stack(
        controls = [
            fundo,
            ft.SafeArea(content=conteudo),
        ],
        expand = True,
        fit=ft.StackFit.EXPAND,
    )

    return tela_inicial


