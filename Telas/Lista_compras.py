import flet as ft
import Controles.Controle_lista_compras as controle
from Telas.Util import criar_fundo,criar_botão_icone,criar_botao_Principal
from Navegacao.navegacao import trocar_tela

def criar_topo():

    botao = criar_botão_icone(ft.Icons.ARROW_BACK,lambda e: controle.Voltar_inicio(e))
    texto = ft.Text("Lista de compras",size=24,color="#FFFFFF",weight=ft.FontWeight.BOLD)

    topo = ft.Row(
        controls=[
            botao,
            texto
        ],
        spacing=30
    )

    return topo

def caixa_criar_lista(linha_botoes_listas, campo_adicionar_item, lista_compras,botao_concluir):
    icone = ft.Icons.ADD
    cor_container = ["#1677FF", "#12DFF3"]

    async def ao_criar_lista(e):
        await controle.Criar_nova_lista(e, nome_lista, linha_botoes_listas,criar_botao_lista, campo_adicionar_item, lista_compras,botao_concluir)


    nome_lista = ft.TextField(
            border_radius = 14,
            label_style = ft.TextStyle(color = "#999B9C"),
            label = "Criar nova lista de compras",
            color = "#E0E5EB",
            border_color="#0A1C2E",
            border_width=2,
            filled = True,
            fill_color="#112240",
            height=48,
        )
    botao = ft.Container(
        content = ft.Icon(icone),
        width=48,
        height=48,
        border_radius=12,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            colors=cor_container,
            end=ft.Alignment(0, 1)
        ),
        ink=True,
        on_click=ao_criar_lista,
        
    )

    nome_lista.expand = 5
    botao.expand = 1

    linha = ft.Row(controls=[nome_lista,botao])

    return linha

def criar_botao_lista(nome_lista,id_lista,linha,campo_adicionar_item,lista_compras,botao_concluir):
    cor_container = ["#363636", "#B6B6B6"] 

    botao = ft.Container(
        content=ft.Text(nome_lista,color="#FFFFFF",weight=ft.FontWeight.W_400),
        border_radius=100,
        #border=ft.Border.all(width=2,color="#12DFF3"),
        height= 35,
        expand=1,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            colors=cor_container,
            end=ft.Alignment(0, 1)
        ),
        alignment=ft.Alignment.CENTER,
        ink=True,
        on_click=lambda e: controle.Acessar_lista(e,id_lista,botao,criar_item,linha,campo_adicionar_item,lista_compras,botao_concluir)
    )

    return botao

def listas_salvas(e,campo_adicionar_item,lista_compras,botao_concluir):

    listas_salvas = controle.Get_listas_salvas(e)
    listas_carregadas = []
    linha = ft.Row()


    if not listas_salvas:
        return ft.Row(controls=[])
    else:
        for lista_atual in listas_salvas:
            id_lista,nome = lista_atual
            botao_lista = criar_botao_lista(nome,id_lista,linha,campo_adicionar_item,lista_compras,botao_concluir)

            listas_carregadas.append(botao_lista)

        linha.controls=listas_carregadas
        return linha       
        
def criar_adicionar_item(lista_compras):

    mensagem_erro = ft.Text("", color="#FF0000",size= 15,visible=False)

    campo_nome = ft.TextField(
        border_radius = 14,
        label_style = ft.TextStyle(color = "#999B9C"),
        label = "Produto",
        color = "#E0E5EB",
        border_color="#0A1C2E",
        border_width=2,
        filled = True,
        fill_color="#112240",
        height=48,
    )
    campo_quantidade = ft.TextField(
        border_radius = 14,
        label_style = ft.TextStyle(color = "#999B9C"),
        label = "Qtd",
        color = "#E0E5EB",
        border_color="#0A1C2E",
        border_width=2,
        filled = True,
        fill_color="#112240",
        height=48,
    )
    campo_quantidade.expand=1
    campo_nome.expand = 3
    icone = ft.Icons.ADD
    cor_container = ["#1677FF", "#12DFF3"]

    botao = ft.Container(
        content = ft.Icon(icone),
        width=48,
        height=48,
        border_radius=12,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            colors=cor_container,
            end=ft.Alignment(0, 1)
        ),

        ink=True,
        on_click=lambda e: controle.Adicionar_item(e,campo_quantidade,campo_nome,lista_compras,criar_item,mensagem_erro)
    )               

    conteudo = ft.Row(
        controls=[
            campo_quantidade,
            campo_nome,
            botao
        ]
    )
    return ft.Column(controls=[conteudo,mensagem_erro])

def criar_item(nome: str, quantidade: str):

    icone = ft.Icons.EDIT_OUTLINED

    botao = ft.Container(content=ft.Icon(icone,color="#FFFFFF"),on_click=controle.Editar_item,ink=True)

    coluna = ft.Column(
        controls=[
            ft.Text(nome.capitalize(),size=16,color="#FFFFFF",weight=ft.FontWeight.BOLD),
            ft.Text(f"{quantidade} - unidades", size=12, color="#FFFFFF"),
        ],
        spacing=2
    )

    linha = ft.Row(
        controls=[
            ft.Checkbox(value=False,width=60,height=60,active_color="#0AA5D4"),
            coluna
        ],
    )
    conteudo = ft.Row(
            controls=[
                linha,
                botao
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    
        )

    caixa = ft.Container(
        content=conteudo,
        width=float("inf"),
        height=75,
        bgcolor="#052B57",
        border_radius=12,
        border=ft.Border.all(width=1,color="#24618F"),
        padding=10
    )

    return caixa

def lista(e):

    page = e.control.page

    id_lista = page.session.store.get("id_lista_ativa")


    if id_lista is None:
        return ft.Column(controls=[])

    lista_compras = controle.Get_lista(id_lista)

    compras = []
   

    if not lista_compras:
        return ft.Column(controls=[])

    else:
        for item in lista_compras:
            if not item:
                continue
            if not lista_compras[item]:
                continue

            compras.append(criar_item(item,lista_compras[item]))

    lista = ft.Column(
        controls=compras,
        expand=True
    )

    return lista

def criar_conteudo(e):        

    
    page = e.control.page
    botao_concluir = criar_botao_Principal("Concluir lista",controle.Concluir_lista)
    topo = criar_topo()
    traco = ft.Divider(color="#24618F", thickness=1)
    lista_compras = lista(e)
    campo_adicionar_item = criar_adicionar_item(lista_compras)
    linha_botoes_listas = listas_salvas(e,campo_adicionar_item,lista_compras,botao_concluir)
    nova_lista = caixa_criar_lista(linha_botoes_listas, campo_adicionar_item, lista_compras,botao_concluir)
    id_lista_atual = page.session.store.get("id_lista_ativa") is None
    
    
    id_lista_atual = page.session.store.get("id_lista_ativa")
    campo_adicionar_item.visible = (bool(linha_botoes_listas.controls) and id_lista_atual is not None)
    botao_concluir.visible = (bool(linha_botoes_listas.controls) and id_lista_atual is not None)
    
    conteudo = ft.Column(
        controls = [
            topo,
            nova_lista,
            #traco,
            linha_botoes_listas,
            campo_adicionar_item,
            #traco,
            lista_compras,
            botao_concluir
        ],
        spacing = 20,
        scroll=ft.ScrollMode.AUTO,
    )

    return conteudo

def Tela_lista_compras(e):

    fundo = criar_fundo()
    conteudo = ft.Container(
        content=criar_conteudo(e),
        padding=20
        )

    lista_compras = ft.Stack(
        controls= [
            fundo,
            conteudo
            ],
            expand=True
    )

    return lista_compras