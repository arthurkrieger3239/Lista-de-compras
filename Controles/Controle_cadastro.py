
import Verificacoes.Valida_cadastro as v
from Navegacao.navegacao import trocar_tela,fechar_dialogo
import Telas
import Banco
import seguranca
import flet as ft


def cadastrar(e, nome, cpf, email, senha, confirmar_senha):

    page = e.control.page
    nome.error = None
    cpf.error = None
    email.error = None
    senha.error = None
    confirmar_senha.error = None
    page.update()
    erro = False

    if not v.Valida_nome(nome.value):
      nome.error = "Nome inválido"
      erro = True

    if not v.Valida_cpf(cpf.value):
      cpf.error = "cpf Inválido"
      erro = True

    if not v.Valida_email(email.value):
      email.error = "Email Inválido"
      erro = True
    
    if not v.Valida_senha(senha.value):
      senha.error = "Senha Inválida"
      erro = True       

    if not v.confirma_senha(senha.value,confirmar_senha.value):
      confirmar_senha.error = "As senhas devem ser iguais"
      erro = True

    if Banco.email_ja_cadastrado(email.value):
      email.error = "Email ja cadastrado"
      erro = True

    if Banco.cpf_ja_cadastrado(cpf.value):
      cpf.error = "Usuário já cadastrado"
      erro = True

    if erro:
      page.update()
      return

    if not erro :
      Banco.salvar_usuario(nome.value,cpf.value,email.value,seguranca.transformar_senha_em_hash(senha.value))
      mensagem = ft.AlertDialog(
      modal=True,
      icon=ft.Icon(
          ft.Icons.CHECK_CIRCLE,
          color="#0000FF",
          size=45
      ),
      title=ft.Text(
          "Cadastro concluído",
          text_align=ft.TextAlign.CENTER
      ),
      content=ft.Text(
          "Usuário cadastrado com sucesso!",
          color="#383842",
          text_align=ft.TextAlign.CENTER
      ),
      actions=[
      ft.TextButton(
          "Continuar",
          on_click=lambda e: ja_cadastrado(e)
      )],
      actions_alignment=ft.MainAxisAlignment.CENTER
  )
      page.show_dialog(mensagem)
      page.update()
              
def ja_cadastrado(e):
  fechar_dialogo(e)
  trocar_tela(e,Telas.Login.tela_login)

def trocar_senha():
  return
