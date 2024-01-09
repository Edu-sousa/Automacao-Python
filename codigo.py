
# pip install nomeBiblioteca / para instalar qualquer biblioteca
import pyautogui
import pandas

#criação variavel tabela
tabela = pandas.read_csv("produtos.csv")
#print(tabela)

# pause do tempo escolhido a cada ação que for feita
pyautogui.PAUSE = 0.5

#aperta a tecla windows
pyautogui.press("win")

#digita o nome do programa
pyautogui.write("chrome")
#aperta enter
pyautogui.press("enter")

#digita o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

pyautogui.click(x=721, y=409) # ou pyautogui.press("tab")

#digita o login
pyautogui.write("emailqualquer@email.com")

pyautogui.press("tab")

#digita a senha
pyautogui.write("senha")

pyautogui.press("tab")

pyautogui.press("enter")

#laço de repetição para cada linha /tabela.index para linhas ou tabela.columns para colunas
for linha in tabela.index:

    pyautogui.click(x=685, y=294)

    #cadastrar produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #convertendo o valor para string com str
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #convertendo o valor para string com str
    #preço unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #convertendo o valor para string com str
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha, "obs"]
    #verifica se a linha obs não esta vazia 
    if not pandas.isna(obs):
        pyautogui.write(obs)

    #enviar o produto    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)




