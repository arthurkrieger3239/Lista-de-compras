from  Banco import Acessar_todas_listas,Criar_lista,itens_da_lista,Salvar_item,Apagar_lista
from Navegacao.navegacao import trocar_tela
import asyncio
def Voltar_inicio(e):

    from Telas.Inicio import Tela_inicial
    page = e.control.page

    page.session.store.set("id_lista_ativa", None)
    trocar_tela(e,Tela_inicial)

def Get_lista(id_lista):

    return dict(itens_da_lista(id_lista))

def Adicionar_item(e, quantidade, nome, coluna_compras, criar_item, mensagem_erro):
    page = e.control.page

    mensagem_erro.visible = False
    mensagem_erro.value = ""
    nome.border_color = "#0A1C2E"
    quantidade.border_color = "#0A1C2E"

    if not quantidade.value or not quantidade.value.isdigit():
        quantidade.border_color = "#FF0000"
        mensagem_erro.value = "A quantidade deve ser um número"
        mensagem_erro.visible = True
        page.update()
        return

    if not nome.value or not nome.value.strip():
        nome.border_color = "#FF0000"
        mensagem_erro.value = "O campo produto não pode estar vazio"
        mensagem_erro.visible = True
        page.update()
        return

    produto = nome.value.strip().capitalize()

    id_lista = page.session.store.get("id_lista_ativa")

    if id_lista is None:
        return

    lista_compras = Get_lista(id_lista)

    if produto in lista_compras:
        nome.border_color = "#FF0000"
        mensagem_erro.value = "Esse produto já está na lista"
        mensagem_erro.visible = True
        page.update()
        return

    id_lista = page.session.store.get("id_lista_ativa")
    Salvar_item(id_lista,produto,quantidade.value)
    coluna_compras.controls.append(criar_item(produto, quantidade.value))

    nome.value = None
    quantidade.value = None
    page.update()

def Get_listas_salvas(e):
    page = e.control.page
    usuario_id = page.session.store.get("usuario_id")

    listas = Acessar_todas_listas(usuario_id)
    return listas

async def Criar_nova_lista(e, nome_lista, linha_botoes_listas, criar_botao_lista, campo_adicionar_item, lista_compras,botao_concluir):
    page = e.control.page
    usuario_id = page.session.store.get("usuario_id")
    nome_lista.error = None
    tamanho = len(Get_listas_salvas(e))
    listas = Get_listas_salvas(e)
    
    if nome_lista.value.strip() == "":
        nome_lista.error = "O nome da lista não pode estar vazia"
        page.update()
        await asyncio.sleep(5)
        nome_lista.error = None
        page.update()
        return
        
    if tamanho >= 3:
        nome_lista.error = "Máximo de 3 listas"
        page.update()
        await asyncio.sleep(5)
        nome_lista.error = None
        page.update()
        return

    for item in range(tamanho):
        id_lista,nome = listas[item]
        if nome_lista.value.strip().capitalize() == nome:
            nome_lista.error = "Essa lista ja existe"
            page.update()
            await asyncio.sleep(5)
            nome_lista.error = None
            page.update()
            return

    id_lista = Criar_lista(usuario_id, nome_lista.value.strip().capitalize())

    linha_botoes_listas.controls.append(
        criar_botao_lista(nome_lista.value.strip().capitalize(), id_lista, linha_botoes_listas, campo_adicionar_item, lista_compras,botao_concluir)
    )

    nome_lista.value = ""
    page.update()

def Acessar_lista(e,id_lista,botao,criar_item,linha,campo_adicionar_item,lista_compras,botao_concluir):

    page = e.control.page
    page.session.store.set("id_lista_ativa", None)
    itens = itens_da_lista(id_lista)

    for botao_atual in linha.controls:
        botao_atual.gradient.colors = ["#363636", "#B6B6B6"]

    page.session.store.set("id_lista_ativa", id_lista)
    campo_adicionar_item.visible = True
    botao_concluir.visible = True
    botao.gradient.colors = ["#1677FF", "#12DFF3"]

    lista_compras.controls.clear()

    for produto, quantidade in dict(itens).items():
        lista_compras.controls.append(criar_item(produto, quantidade))

    page.update()

def Editar_item(e):
    return

def Concluir_lista(e):

    from Telas.Lista_compras import Tela_lista_compras
    page = e.control.page
    id_lista = page.session.store.get("id_lista_ativa")
    if id_lista is None:
        return
    Apagar_lista(id_lista)
    page.session.store.set("id_lista_ativa",None)
    trocar_tela(e,lambda :Tela_lista_compras(e))
    page.update()
    return





