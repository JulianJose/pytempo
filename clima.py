#!/home/julian/anaconda3/bin/python

import requests, sys, bs4
from tqdm import tqdm

def baixa_site(estado = "pr", cidade = "ponta-grossa"):
    ''' Baixa o site que fornece as informações de clima.
    Retora uma string com o site em html.
    Usa como parâmetro o estado e a cidade. Os nomes devem
    estar em letras minúsculas e separados por "-" caso se-
    jam compostos. '''

    print("Baixando informações de: \n{}".format("http://tempo.cptec.inpe.br/{0}\
    #/{1}".format(estado, cidade)))

    site = requests.get("http://tempo.cptec.inpe.br/{0}/{1}".format(estado, cidade))

    site.raise_for_status()

    return site.text

# Cria um objeto BeautifulSoup usando o texto html

soup = bs4.BeautifulSoup(baixa_site(), "html.parser")

# Seleciona as informações que temos interesse
info = soup.select("#previsaoTempo")


texto = info[0].getText()
texto = texto.replace("\n", " ")
print(texto)
