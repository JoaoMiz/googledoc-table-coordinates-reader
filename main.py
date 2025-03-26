from bs4 import BeautifulSoup
import requests
def Decodar(url):
    dados_tabela = []
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    tabela = soup.find('table')
    max_x = 0
    max_y = 0
    todos_x = []
    todos_y = []
    matriz = []

    #adicionar dado na tabela
    for tr in tabela.find_all('tr')[1:]:
        colunas = tr.find_all('td')
        pos_x = colunas[0].find('span').text
        pos_y = colunas[2].find('span').text
        #checa se o caractere ta vazio, se estiver coloca espaço em branco
        if colunas[1] != "":
            caractere = colunas[1].find('span').text
        else:
            caractere = " "
        dados_tabela.append([pos_x, pos_y, caractere])

    #pegar o tamanho da tabela
    for i in range(0, len(dados_tabela)):
        todos_x.append(int(dados_tabela[i][0]))
        todos_y.append(int(dados_tabela[i][1]))
    #usa +1 por causa que o x e y começam em 0
    max_x = max(todos_x)+1
    max_y = max(todos_y)+1
    #criar a matriz
    for i in range(max_y):
        linha = [' ' for _ in range(max_x)]
        matriz.append(linha)
    #encher a matriz com base nas posições
    for pos_x,pos_y,caractere in dados_tabela:
        matriz[int(pos_y)][int(pos_x)] = caractere
    #a matriz ta de cabeça pra baixo por que o y dita a altura/linha
    for y in range(max_y-1,-1,-1):
        for x in range(max_x):
            print(matriz[y][x],end='')
        print()



Decodar("https://docs.google.com/document/d/e"
        "/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53e"
        "rafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub")