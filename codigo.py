# Passo 1: Entrar no sistema da empresa - https://hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=450, y=400)
pyautogui.write("treinamentopython@mail.com")
# passar para o proximo campo
pyautogui.press("tab")
pyautogui.write("minha senha aqui")
# apertar no botão de login
pyautogui.click(x=667, y=567)

time.sleep(2)

# Passo 3: Importar a base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4: Cadastrar um produto

# para cada linha da tabela

for linha in tabela.index:
    # selecionar o 1º campo
    pyautogui.click(x=383, y=287)   
    # texto = string = str()

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    # nan = Not a Number = vazio
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar no botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar os produtos