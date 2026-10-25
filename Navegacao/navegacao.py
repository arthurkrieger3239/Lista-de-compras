import flet as ft
def definir_page(page):
    page.window.width = 390
    page.window.height = 844
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.padding = 0

    page.update()


def trocar_tela(e,nova_tela):
    
    page = e.control.page
    if page is None:
        raise RuntimeError("A página ainda não foi definida")

    page.clean()
    page.add(nova_tela())

def fechar_dialogo(e):
    page = e.control.page

    page.pop_dialog()
    page.update()

