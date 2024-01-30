import yfinance
import pyautogui
import pyperclip
import matplotlib

#Coleta de parâmetros
ticker = input("Digite o código da ação: ")
periodo = input("Digite o período em meses que deseja obter o relatório(APENAS NÚMEROS): ",)
destinatario = input("Digite o email par o qual deseja enviar o relatório: ")
assunto = input("Digite o título do email: ")
dados = yfinance.Ticker(ticker)
dados.history()

tabela = dados.history(periodo)

# Fechamento diario
fechamento = tabela.Close

# Gerar um gráfico
fechamento.plot()

# Gerando estatisticas
maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

#Criando email,
mensagem = f""" 
Bom dia, 

Segue abaixo as análises da ação {ticker} dos ultimos {periodo} meses:

Cotação Máxima: R$ {"%.2f" %maxima}
Cotação Mínima: R$ {"%.2f" %minima}
Cotação Atual: R$ {"%.2f" %atual}

Atenciosamente,
Isllas Curty.
"""

# Automatizando o envio
pyautogui.PAUSE = 4

# Abrir nova aba navegador
pyautogui.hotkey("ctrl", "t")

# Copiar endereço de login do email
pyperclip.copy("www.gmail.com")


# Colar o endereço e iniciar navegação
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

# Iniciando envio de novo email
pyautogui.click(x=79, y=182)


# inserindo destinatário
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Inserindo assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# Inserindo mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

# Clicando no botão enviar
pyautogui.click(x=841, y=694)

# Fechar aba do email
pyautogui.hotkey("ctrl","f4")

# Retornar menssagem de sucesso
print("Email enviado com sucesso!")

