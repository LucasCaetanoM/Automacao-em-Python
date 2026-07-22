import pyautogui 
import time  

#pyautogui.click(100, 200) -> clica no sistemahttp
#pyautogui.write('usuario') -> digita o usuario
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey('ctrl', 'v') -> aperta uma combinação de teclas
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#passo a passo do programa

#passo 1 - entrar no sistema
#abrir o navegadorhttp chromeps:
pyautogui.hotkey('command', 'space')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')

#fazer uma pausa pro navegador carregar
time.sleep(1)
#passo 2 - fazer login
pyautogui.click(x=580, y=401)
pyautogui.write('ozizalmt453@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('enter')

#pausa pro sistema carregar
time.sleep(3)

#passo 3 - abrir a base de dados (importar o arquivo)
import pandas

tabela = pandas.read_csv("/Users/ozizal/Projetos/Python/Automação em Python/Automação em Python/produtos.csv")

for linha in tabela.index:
#passo 4 - cadastrar um produto
#codigo
    pyautogui.click(x=542, y=293)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preço
    preço = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preço)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")  

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
#voltar para o início da tela
    pyautogui.scroll(5000)
#passo 5 - repetir o processos