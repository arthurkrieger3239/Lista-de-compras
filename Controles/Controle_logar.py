from Navegacao.navegacao import trocar_tela
from datetime import datetime, timedelta, timezone
from flet.security import encrypt, decrypt
from cryptography.fernet import InvalidToken
import os
import flet as ft
import Telas
import Banco
import secrets
import seguranca


CHAVE_TOKEN_LOCAL = "projeto_william.auth_token"
CHAVE_CRIPTOGRAFIA = "PROJETO_WILLIAM_SECRET_KEY"

async def logar(e,email:ft.TextField ,senha: ft.TextField,lembrar):
    email.error = None
    senha.error =  None
    erro = False

    if not Banco.email_ja_cadastrado(email.value):
        email.error = "Email não cadastrado"
        erro = True
    else:

        if not Banco.senha_certa(email.value,senha.value):
            senha.error = "Senha Inválida"
            erro = True

    if erro:
        email.update()
        senha.update()
        return
    if lembrar.value:
        await manter_logado(e,email.value)

    trocar_tela(e,Telas.Inicio.tela_inicial)

def nao_cadastrado(e):
    trocar_tela(e,Telas.Cadastro.tela_criar_cadastro)

async def manter_logado(e, email):
    usuario_id = Banco.buscar_id_usuario(email)

    if usuario_id is None:
        return False

    chave = os.getenv(CHAVE_CRIPTOGRAFIA)

    if chave is None:
        raise RuntimeError(
            "A chave de criptografia não foi configurada"
        )

    token = secrets.token_urlsafe(32)
    token_hash = seguranca.transformar_token_em_hash(token)

    expira_em = (
        datetime.now(timezone.utc) + timedelta(days=90)
    ).isoformat()

    Banco.salvar_sessao(
        usuario_id,
        token_hash,
        expira_em
    )

    token_criptografado = encrypt(token, chave)

    page = e.control.page

    await page.shared_preferences.set(
        CHAVE_TOKEN_LOCAL,
        token_criptografado
    )

    return True

async def verificar_login_salvo(page):
    token_criptografado = await page.shared_preferences.get(
        CHAVE_TOKEN_LOCAL
    )

    if not token_criptografado:
        return None

    chave = os.getenv(CHAVE_CRIPTOGRAFIA)

    if chave is None:
        raise RuntimeError(
            "A chave de criptografia não foi configurada"
        )

    try:
        token = decrypt(token_criptografado, chave)

    except (InvalidToken, ValueError, TypeError):
        await page.shared_preferences.remove(
            CHAVE_TOKEN_LOCAL
        )
        return None

    if not token:
        await page.shared_preferences.remove(
            CHAVE_TOKEN_LOCAL
        )
        return None

    token_hash = seguranca.transformar_token_em_hash(token)

    usuario_id = Banco.buscar_usuario_sessao_valida(
        token_hash
    )

    if usuario_id is None:
        await page.shared_preferences.remove(
            CHAVE_TOKEN_LOCAL
        )
        return None

    page.session.store.set(
        "usuario_id",
        usuario_id
    )

    return usuario_id