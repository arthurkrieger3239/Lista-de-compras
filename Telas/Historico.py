
import  flet as ft
import Controles.Controle_historico as controle
from Telas.Util import criar_fundo
from Telas.Util import criar_botão_icone

compra = {
    "id_compra": 1,
    "mercado": "Gauchão",
    "data": "11/11/2026",
    "total": 182.40,
    "itens": []
}

def criar_topo():
    botao = criar_botão_icone(ft.Icons.ARROW_BACK,lambda e: controle.Voltar_inicio(e))
    texto = ft.Text("Historico de compras",size=20,color="#FFFFFF",weight=ft.FontWeight.W_600)

    linha = ft.Row(
        controls=[
            botao,
            texto
        ],
        spacing=30
    )

    return linha

def criar_caixa_compra(compra : dict):

    valor_total = compra["total"]
    quantidade_itens = len(compra["itens"])
    data = compra["data"]
    nome_mercado = compra["mercado"]

    texto_mercado = ft.Text(f"{nome_mercado}",size=16,weight=ft.FontWeight.W_700,color="#FFFFFF" )
    texto_quantidade_itens = ft.Text(f"{quantidade_itens} - itens",size=12,weight=ft.FontWeight.W_700,color="#585858")
    texto_valor_total = ft.Text(f"R$ {valor_total}",size=20,weight=ft.FontWeight.BOLD,color="#FFFFFF")
    texto_data =ft.Text(f"{data}", size= 20,color="#FFFFFF",weight=ft.FontWeight.BOLD)

    icone =  ft.Icon(ft.Icons.SHOPPING_BAG_OUTLINED,color="#FFFFFF",size=28)
    caixa_icone = ft.Container(
        content=icone,
        width=50,
        height=50,
        bgcolor="#1677FF",
        border_radius=12,
        alignment=ft.Alignment.CENTER,
    )

    coluna = ft.Column(
        controls=[
            texto_mercado,
            texto_quantidade_itens
        ],
        spacing=5
    )
    linha_inicial = ft.Row(
        controls=[
           caixa_icone,
            coluna
        ]
    )
    linha = ft.Row(
        controls=[
            linha_inicial,
            texto_valor_total
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    caixa = ft.Container(
        content=linha,
        width=float("inf"),
        height=80,
        bgcolor="#052B57",
        border=ft.Border.all(1, "#24618F"),
        padding=10,
        border_radius=15
        )

    return caixa,texto_data

def lista_ultimas_compras():

    caixa,texto_data = criar_caixa_compra(compra)
    return ft.Column(controls=[texto_data,caixa])

def criar_total_mes():

    valor_do_mes = str(0.01)
    numero_compras = 3

    texto = ft.Text("Compras em Novembro:",size=20,color="#FFFFFF",weight=ft.FontWeight.W_600)
    texto_valor = ft.Text(f"R$ {valor_do_mes.replace(".",",")}",size=30,color="#FFFFFF",weight=ft.FontWeight.BOLD)
    #texto_numero_compras = ft.Text(f"{numero_compras} - compras nesse mês")

    coluna = ft.Column(
        controls=
        [
            texto,
            texto_valor
        ],
        spacing=5
    )

    linha = ft.Row(
        controls=[
            coluna,
            #texto_numero_compras
        ]
    )

    conteudo = ft.Container(
        content=linha,
        width=float("inf"),
        height=100,
        bgcolor="#052B57",
        border=ft.Border.all(1, "#24618F"),
        padding=12,
        border_radius=15
    )

    return conteudo

def criar_conteudo():

    topo = criar_topo()
    valor_gasto_mes = criar_total_mes()
    lista = lista_ultimas_compras()


    corpo = ft.Column(
        controls=[
            topo,
            valor_gasto_mes,
            lista
        ]
    )

    conteudo = ft.Container(
        content=corpo,
        padding=20
    )
    return conteudo
def Tela_historico():

    fundo = criar_fundo()
    conteudo = criar_conteudo()

    historico = ft.Stack(
        controls=[
            fundo,
            conteudo
        ],
        expand=True
    )

    return historico