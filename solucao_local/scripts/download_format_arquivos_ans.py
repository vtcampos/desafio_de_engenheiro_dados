#### SETUP
# Packages trablhar com linha de comando
import subprocess

# Packages para trabalhar com diretorios
import os
import glob

# Packages para manupular dados
import pandas as pd

# Packages webscrapping
import requests
from bs4 import BeautifulSoup
import lxml
import re


#### FUNCOES
# Funcao para rodar o comando wget desejado
def runcmd(cmd, verbose=False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

runcmd('echo "Hello, World!"', verbose=True)

#### BAIXA O ARQUIVO HTML DA PAGINA
# Url
url = 'https://dadosabertos.ans.gov.br/FTP/Base_de_dados/Microdados/dados_dbc/beneficiarios/operadoras/'

# Carrego o arquivo no BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
soup

# Pego todos os métodos 'a' do HTML poís é nesse método que encontram-se os nomes dos aquivos
files = soup.find_all('a')

# Escrevo os nomes dos arquivos em uma lista
files_list = []

for i in files:
    name = i.string
    # print(name.endswith('.dbc'))
    if name.endswith('.dbc'):
        files_list.append(name)
    pass


#### BAIXA OS ARQUIVOS .dbc

# Diretorio de destino
download_dir = 'C:\\Users\\Windows\\Documents\\BaseDosDados\\desafio_de_engenheiro_dados\\solucao_local\\data\\dbc'


# Adiciono os nomes dos arquivos a URL da página e baixo todos eles usando o WGET
for i in files_list:
    runcmd('wget --directory-prefix='+download_dir+' ' + url+'/'+str(i), verbose=True)


#### CONVERT OS ARQUIVOS .dbc em .csv USANDO R
script_path = 'C:\\Users\\Windows\\Documents\\BaseDosDados\\desafio_de_engenheiro_dados\\solucao_local\\scripts'
script = 'dbc2csv.r'
# Comando para executar o Script R que converte os dados .dbc em .csv
runcmd('Rscript '+script, verbose=True)




