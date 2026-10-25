import flet as ft
import Telas
from flet.controls.alignment import Alignment


def criar_campo(texto,icon,password = False):

        campo = ft.TextField(
        
            border_radius = 14,
            label_style = ft.TextStyle(color = "#999B9C"),
            label = texto,
            color = "#E0E5EB",
            border_color="#0A1C2E",
            border_width=2,
            filled = True,
            fill_color="#112240",
            password = password,
            can_reveal_password = password, 
            prefix_icon = ft.Icon(
                icon,
                color = "#999B9C"
                ),
        )               
        return campo
def criar_fundo():

    fundo_gradiente = ft.Container(
        gradient=ft.LinearGradient(
            begin=Alignment(0, -1),
            end=Alignment(0, 1),
            colors=["#020C1A", "#0C3574", "#020A18"]
        ),
        expand=True
    )

    return fundo_gradiente

def criar_botao_Principal(
    texto ,
    funcao ,
    cor_container = ["#1677FF", "#12DFF3"],
    largura_borda=300,
    altura_borda=56,
    cor="#FFFFFF",
    tamanho_letra=18,
    icone_texto = "",
    borda_raio = None
):

    if borda_raio is None:
         borda_raio = altura_borda/2

    escrita = ft.Text(texto,color=cor,size=tamanho_letra,weight=ft.FontWeight.BOLD)

    if icone_texto != "":
        icone = ft.Icon(icone_texto, color = "#FFFFFF", size = 26)
        controle = [escrita,icone]

    else:
        controle =[escrita]
    
    conteudo = ft.Row(
         controls = controle,
         alignment = ft.MainAxisAlignment.CENTER
    )
         

    botao = ft.Container(
        width=largura_borda,
        height=altura_borda,
        border_radius=borda_raio,

        gradient=ft.LinearGradient(
            begin=Alignment(0, -1),
            colors=cor_container,
            end=Alignment(0, 1)
        ),

        content = conteudo,

        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=1,
            color="#4012DFF3"
        ),

        on_click=funcao,
        ink=True
    )

    return botao
def criar_botao_Texto(texto,funcao,cor_letra = "#FFFFFF",tamanho_letra = 14,negrito = False):
     escrita = ft.Text(
          value = texto,
          color = cor_letra,
          size = tamanho_letra,
          weight = (
            ft.FontWeight.BOLD
            if negrito
            else ft.FontWeight.NORMAL
          )
     )
     botao = ft.TextButton(
        content = escrita,
        on_click = funcao,
     )

     return botao
def criar_botão_icone(icone,funcao,cor_icone = "#FFFFFF",tamanho_icone = 26,altura_container = 50,largura_cotainer = 50,cor_container = "#0C3574"):

     icone_visual = ft.Icon(icone,color = cor_icone,size = tamanho_icone)

     botao = ft.Container(
          content = icone_visual,
          height = altura_container,
          width = largura_cotainer,
          bgcolor = cor_container,
          border_radius = altura_container/2,
          border = ft.Border.all(width = 2, color = "#7DD3FC"),
          on_click = funcao,
          ink = True,
          ink_color="#407DD3FC"

     )
     return botao
def criar_botao_coluna(texto,funcao,icone = "",tamanho_icone = 32,cor_icone ="#00CFFF" ,tamanho_texto = 13
                       ,cor_texto = "#FFFFFF",tem_container = True,largura_container = 160,altura_container = 90,cor_container = "#0B315B"):

    icon = ft.Icon(
         icon = icone,
         size = tamanho_icone,
         color = cor_icone
    )
    text =ft.Text(texto,size = tamanho_texto,color = cor_texto,weight=ft.FontWeight.W_600,text_align=ft.TextAlign.CENTER)
    
    coluna = ft.Column(
         controls = [
              icon,
              text
         ],
         horizontal_alignment = ft.CrossAxisAlignment.CENTER,
         alignment = ft.MainAxisAlignment.CENTER,
         tight = True,
         spacing = 4,
         
         
    )
    if tem_container:
        botao = ft.Container(
            content = coluna,
            width = largura_container,
            height = altura_container,
            border_radius = 15,
            bgcolor =  cor_container,
            on_click = funcao,
            ink = True,
            ink_color="#407DD3FC",
            padding = 10,
            alignment = ft.Alignment.CENTER,
            border = ft.Border.all(width=1, color= "#006DC0")
        )
    else:
         botao = ft.Container(
            content=coluna,
            on_click = funcao,
            ink = True,
            ink_color="#407DD3FC",
            padding = 10,
            alignment = ft.Alignment.CENTER,
         ) 

    return botao

def Inicio(e):

    page = e.control.page

    page.clean()
    page.add(Telas.Inicio.tela_inicial())
    
