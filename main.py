import flet as ft
import Telas
from Banco import criar_tabela,Buscar_usuario_ativo
from Navegacao.navegacao import definir_page
from Controles.Controle_logar import verificar_login_salvo
from dotenv import load_dotenv
from Modelos.usuario import Usuario_ativo 

load_dotenv()


async def main(page: ft.Page):

    criar_tabela()
    definir_page(page)

    usuario_id = await verificar_login_salvo(page)

    if usuario_id is not None:
        dados = Buscar_usuario_ativo(usuario_id)
        page.session.store.set("nome_usuario", dados[1])
        page.session.store.set("cpf_usuario", dados[2])
        page.session.store.set("email_usuario", dados[3])
        page.add(Telas.Inicio.tela_inicial())
    else:
        page.add(Telas.Login.tela_login())
        
if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="Assets"
    )