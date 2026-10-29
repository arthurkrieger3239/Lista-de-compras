import os
import Banco
import seguranca
from flet.security import decrypt
from Modelos.usuario import Usuario_ativo
from Navegacao.navegacao import trocar_tela
from Telas.Login import tela_login

def ver_dados():
    raise ValueError("Função ainda nao implementada")

async def sair_conta(e):

    page = e.control.page

    token_criptografado = await page.shared_preferences.get("Lista_compras.auth_token")

    if token_criptografado is not None:

        chave = os.getenv("LISTA_COMPRAS_SECRET_KEY")

        if chave is None:
            raise RuntimeError("Chave de criptografia não configurada")

        token = decrypt(token_criptografado, chave)

        token_hash = seguranca.transformar_token_em_hash(token)

        Banco.excluir_sessao(token_hash)

        await page.shared_preferences.remove("Lista_compras.auth_token")

        page.session.store.remove("usuario_id")
        page.session.store.remove("nome_usuario")
        page.session.store.remove("cpf_usuario")
        page.session.store.remove("email_usuario")

        trocar_tela(e,tela_login)


def fechar_aba(e, menu, fundo):
    menu.visible = False
    fundo.visible = False
    e.page.update()