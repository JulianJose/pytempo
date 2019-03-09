#!/home/julian/anaconda3/bin/python

import requests, sys, bs4
import re

def baixa_site(estado = "pr", cidade = "ponta-grossa"):
    ''' Baixa o site que fornece as informações de clima.
    Retora uma string com o site em html.
    Usa como parâmetro o estado e a cidade. Os nomes devem
    estar em letras minúsculas e separados por "-" caso se-
    jam compostos. '''

    print("Baixando informações de: \n{}".format("http://tempo.cptec.inpe.br/{0}/{1}".format(estado, cidade)))

    site = requests.get("http://tempo.cptec.inpe.br/{0}/{1}".format(estado, cidade))
    site.raise_for_status()

    return site.text

def extrai_dados(texto):
    temperatura = re.findall("\d\d. \d\d. ", texto)
    datas = re.findall("\d\d/\d\d/\d{4}", texto)
    chuva = re.findall("\d\d%", texto)

    return datas, temperatura, chuva


# Cria um objeto BeautifulSoup e o inicia com o texto html baixado.
if len(sys.argv) == 3:
    soup = bs4.BeautifulSoup(baixa_site(sys.argv[1], sys.argv[2]), "html.parser")
else:
    soup = bs4.BeautifulSoup(baixa_site(), "html.parser")

# Seleciona as informações.
info = soup.select("#previsaoTempo")

# Trata o texto
texto = info[0].getText()
texto = texto.replace("\n", " ")

data, temperatura, chuva = extrai_dados(texto)

for i in range(len(data)):
    print("Data: {0} Temparatura (Máx Min): {1} Probabilidade de chuva: {2}".format(data[i], temperatura[i], chuva[i]))
