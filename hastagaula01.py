# para instalar: pip install pyautogui
import pyautogui
from time import sleep
pyautogui.PAUSE = 0.5

#---------------------------------------

# abrir navegador (Chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(2)

# entrar non site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# aqui pode ser que ele demore alguns segundos para carregar o site apenas para esse bloco
sleep(2)

pyautogui.click(x=766, y=461)
pyautogui.write('pythonautogui@gmail.com')
pyautogui.press('tab')     # pulara para a proxima aba
pyautogui.write('senha123')
pyautogui.press('tab')     # botao de login
pyautogui.press('enter')

sleep(2)

# abrir/importar base de dados de produtos para cadastrar
import pandas # as pd é abreviar

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])

    pyautogui.click(x=642, y=327)
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.scroll(5000)
