from Navegacao .navegacao import trocar_tela
from Telas.Acessar_usuario import Tela_acessar_usuario
from Telas.Lista_compras import Tela_lista_compras
from Telas.Historico import Tela_historico

def acessar_usuario(e):
    trocar_tela(e,Tela_acessar_usuario)
def Nova_compra(e):
    raise NotImplementedError("A função ainda nao foi implementada") 
def lista_compras(e):
    trocar_tela(e,lambda: Tela_lista_compras(e))
def Historico(e):
   trocar_tela(e,Tela_historico)
def Ultimas_compras():
    raise NotImplementedError("A função ainda nao foi implementada")
def Get_Ultimas_compras():

    return "nome1","nome2","data1","data2","valor1","valor2"
def Get_gastos():
    return 0.00

def Get_proporcao_gasto_orcamento():
    return 0.5

def Get_itens():
    return 3,10
