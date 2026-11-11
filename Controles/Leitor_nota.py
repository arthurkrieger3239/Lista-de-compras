import requests
from bs4 import BeautifulSoup

def Ler_nota(url):

    itens = []

    resposta = requests.get(url,timeout=20)
    pagina = BeautifulSoup(resposta.text, "html.parser")

    mercado = pagina.find("div", id="u20").get_text(strip=True)
    valor_total = pagina.find("div", id="totalNota")
    valor_total = valor_total.find("span", class_="totalNumb txtMax").get_text(strip=True)
    data = pagina.find("div",id = "infos").find("strong", string = " Emissão: ")
    data = data.next_sibling.split(" - Via Consumidor")[0].strip()

    tabela_itens = pagina.find("table", id="tabResult")
    linhas_itens = tabela_itens.find_all("tr")  

    for linha in linhas_itens:
        nome = linha.find("span", class_="txtTit").get_text(strip=True)
        quantidade =linha.find("span", class_="Rqtd").get_text(strip=True).removeprefix("Qtde.:").strip()
        unidade = linha.find("span", class_="RUN").get_text(strip=True).removeprefix("UN:").strip()
        valor_unitario = linha.find("span", class_="RvlUnit").get_text(strip=True).removeprefix("Vl. Unit.:").strip()
        valor_item =linha.find("span", class_="valor").get_text(strip=True)

        itens.append({"nome":nome,"quantidade":quantidade,"unidade":unidade,"valor_unitario":valor_unitario,"valor_item":valor_item})
    
    nota = {
    "id_compra": 1,
    "mercado": mercado,
    "data": data,
    "total": valor_total,
    "itens": itens
}

    return nota

    


