from tkinter import *
from turtle import *
from random import *
import numpy as np


# Desenha as partes do layout
# Desenha a linha de cima
def linha_cima():
    # Variaveis que fazem os quadrados se moverem da esquerda para direita
    primeiroX = 0
    segundoX = 25

    # Lopp que move os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(primeiroX, 0, segundoX, 25, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(primeiroX, 0, segundoX, 25, fill='white', outline='white')

        # Move os quadrados 25 pixels
        primeiroX += 25
        segundoX += 25

# Desenha a linha da direita
def linha_direita():
    # Variaveis que movem os quadrados de cima para baixo
    primeiroY = 25
    segundoY = 50

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(775, primeiroY, 800, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(775, primeiroY, 800, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY += 25
        segundoY += 25

# Desenha a linha de baixo
def linha_baixo():
    # Variaveis que movem os quadrados da direita para esquerda
    primeiroX = 800
    segundoX = 775

    # Loop que movem os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(primeiroX, 575, segundoX, 600, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(primeiroX, 575, segundoX, 600, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroX -= 25
        segundoX -= 25

# Desenha a linha da esquerda
def linha_esquerda():
    # Variaveis que movem os quadrados de baixo pra cima
    primeiroY = 550
    segundoY = 575

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgTela.create_rectangle(0, primeiroY, 25, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgTela.create_rectangle(0, primeiroY, 25, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY -= 25
        segundoY -= 25

# Desenha o layout
def desenha_layout():
    linha_cima()
    linha_direita()
    linha_baixo()
    linha_esquerda()







def deleta_jogo():
    global labelLinha
    global caixaLinha
    global labelColuna
    global caixaColuna
    global botaoTentativa
    global botaoJogoVoltaMenuInicial
    global matrizJogo
    global tamanhoJogo
    global divisoria
    global matrizX
    global matrizMarquina
    global matrizTeste
    global matrizVerificacao

    labelLinha.destroy()
    caixaLinha.destroy()
    labelColuna.destroy()
    caixaColuna.destroy()
    botaoTentativa.destroy()
    botaoJogoVoltaMenuInicial.destroy()
    confgTela.delete(divisoria)

    for i in range(tamanhoJogo):
        for j in range(tamanhoJogo):
            confgTela.delete(matrizJogo[i][j])

    for i in range(len(matrizX)):
        for j in range(len(matrizX[i])):
            confgTela.delete(matrizX[i][j])

    for i in range(len(matrizMarquina)):
        confgTela.delete(matrizMarquina[i])

    matrizJogo = []
    matrizX = []
    matrizMarquina = []
    matrizTeste = []
    matrizVerificacao = []

    if labelAviso != None:
        labelAviso.destroy()
    if labelAlerta != None:
        labelAlerta.destroy()

def deletaMenuVenceu():
    global labelVenceu
    global botaoVenceuSair
    global botaoVenceuJogarNovamente

    labelVenceu.destroy()
    botaoVenceuSair.destroy()
    botaoVenceuJogarNovamente.destroy()

    desenha_menu_inicial()

def venceu():
    global labelVenceu
    global botaoVenceuSair
    global botaoVenceuJogarNovamente

    deleta_jogo()

    labelVenceu = Label(confgTela,text="Parabens você venceu!\nGostaria de continuar a jogar?")
    labelVenceu.config(width=42, height=3)
    labelVenceu.place(x=250,y=100)

    botaoVenceuSair = Button(confgTela,text="sair",command=sair)
    botaoVenceuSair.config(width=14,height=2)
    botaoVenceuSair.place(x=250,y=200)

    botaoVenceuJogarNovamente = Button(confgTela,text="Jogar Novamente",command=deletaMenuVenceu)
    botaoVenceuJogarNovamente.config(width=13,height=2)
    botaoVenceuJogarNovamente.place(x=450,y=200)

def deletaMenuPerdeu():
    global labelPerdeu
    global botaoPerdeuSair
    global botaoPerdeuJogarNovamente

    labelPerdeu.destroy()
    botaoPerdeuSair.destroy()
    botaoPerdeuJogarNovamente.destroy()

    desenha_menu_inicial()

def perdeu():
    global labelPerdeu
    global botaoPerdeuSair
    global botaoPerdeuJogarNovamente

    deleta_jogo()

    labelPerdeu = Label(confgTela,text="Você perdeu!\nGostaria de continuar a jogar?")
    labelPerdeu.config(width=42, height=3)
    labelPerdeu.place(x=250,y=100)

    botaoPerdeuSair = Button(confgTela,text="sair",command=sair)
    botaoPerdeuSair.config(width=14,height=2)
    botaoPerdeuSair.place(x=250,y=200)

    botaoPerdeuJogarNovamente = Button(confgTela,text="Jogar Novamente",command=deletaMenuPerdeu)
    botaoPerdeuJogarNovamente.config(width=13,height=2)
    botaoPerdeuJogarNovamente.place(x=450,y=200)

def deleta_menu_empate():
    global labelEmpate
    global botaoEmpateSair
    global botaoEmpateJogarNovamente

    labelEmpate.destroy()
    botaoEmpateSair.destroy()
    botaoEmpateJogarNovamente.destroy()

    desenha_menu_inicial()

def empate():
    global labelEmpate
    global botaoEmpateSair
    global botaoEmpateJogarNovamente

    deleta_jogo()

    labelEmpate = Label(confgTela,text="É um empate!\nGostaria de continuar a jogar?")
    labelEmpate.config(width=42, height=3)
    labelEmpate.place(x=250,y=100)

    botaoEmpateSair = Button(confgTela,text="sair",command=sair)
    botaoEmpateSair.config(width=14,height=2)
    botaoEmpateSair.place(x=250,y=200)

    botaoEmpateJogarNovamente = Button(confgTela,text="Jogar Novamente",command=deleta_menu_empate)
    botaoEmpateJogarNovamente.config(width=13,height=2)
    botaoEmpateJogarNovamente.place(x=450,y=200)


def verificacao():
    global matrizVerificacao

    matriz = np.array(matrizVerificacao)

    diagonal_principal = np.diagonal(matriz)

    diagonal_secundaria = np.diagonal(np.fliplr(matriz))

    # Coluna
    for coluna in range(len(matriz)):
        if np.all(matriz[:, coluna] == "maquina"):
            perdeu()
        elif  np.all(matriz[:, coluna] == "usuario"):
            venceu()
    # Linha
    for linha in range(len(matriz)):
        if np.all(matriz[linha, :] == "maquina"):
            perdeu()
        elif np.all(matriz[linha, :] == "usuario"):
            venceu()
    # Diagonal Principal
    if np.all(diagonal_principal == "maquina"):
        perdeu()
    elif np.all(diagonal_principal == "usuario"):
        venceu()
    # Diagonal Secundaria
    elif np.all(diagonal_secundaria == "maquina"):
        perdeu()
    elif np.all(diagonal_secundaria == "usuario"):
        venceu()
    
    # Verifica se ouve um impate
    if np.all(np.not_equal(matriz, None)):
        empate()

    matriz = []

def desenha_x(valorLinha,valorColuna,tamanhoQuadrado):
    global matrizX
    global matrizTeste
    global matrizVerificacao
    global labelAlerta

    linhaVerifica = valorLinha
    colunaVerifica = valorColuna

    valorVerificar = str(str(linhaVerifica) + ";" + str(colunaVerifica))

    if any(valorVerificar in linha for linha in matrizTeste):
        temporaria = []
        # Desenha o X do jogador
        temporaria.append(confgTela.create_line(75 + (tamanhoQuadrado * (valorColuna - 1)),125 + (tamanhoQuadrado * (valorLinha - 1)),(75 + ((tamanhoQuadrado) * valorColuna)),(125 + ((tamanhoQuadrado) * valorLinha)),fill="green",width=2))

        temporaria.append(confgTela.create_line((75 + ((tamanhoQuadrado) * valorColuna)),125 + (tamanhoQuadrado * (valorLinha - 1)),75 + (tamanhoQuadrado * (valorColuna - 1)),(125 + ((tamanhoQuadrado) * valorLinha)),fill="green",width=2))

        matrizX.append(temporaria)

        matrizVerificacao[linhaVerifica - 1][colunaVerifica - 1] = "usuario"

    else:
        labelAlerta = Label(confgTela,text="Você não fornexeu um valor dentro dos limites e perdeu sua jogada", wraplength=175)
        labelAlerta.config(width=28,height=4)
        labelAlerta.place(x=500,y=50)

    for i in range(len(matrizTeste) - 1, -1, -1):

        if valorVerificar in matrizTeste[i]:
            matrizTeste[i].remove(valorVerificar)

        if matrizTeste[i] == []:
            matrizTeste.remove(matrizTeste[i])

def tentativa_maquina(tamanhoQuadrado):
    global matrizMarquina
    global matrizTeste
    global matrizVerificacao

    listaSelecionada = choice(matrizTeste)
    valorEscolhido = choice(listaSelecionada)

    valorVerificar = valorEscolhido
    partes = valorVerificar.split(";")

    valorLinha = int(partes[0])
    valorColuna = int(partes[1])

    if any(valorVerificar in linha for linha in matrizTeste):
        # Desenha o circulo da maquina
        matrizMarquina.append(confgTela.create_oval(75 + (tamanhoQuadrado * (valorColuna - 1)),125 + (tamanhoQuadrado * (valorLinha - 1)),(75 + ((tamanhoQuadrado) * valorColuna)),(125 + ((tamanhoQuadrado) * valorLinha)),outline="red",width=2))
    
        matrizVerificacao[valorLinha - 1][valorColuna - 1] = "maquina"

    for i in range(len(matrizTeste) - 1, -1, -1):

        if valorVerificar in matrizTeste[i]:
            matrizTeste[i].remove(valorVerificar)

        if matrizTeste[i] == []:
            matrizTeste.remove(matrizTeste[i])
            
def tentativa():
    global caixaLinha
    global caixaColuna
    global tamanhoJogo
    global labelAviso
    global labelAlerta

    linha = caixaLinha.get()
    coluna = caixaColuna.get()

    if linha and coluna:
        if linha.isnumeric and coluna.isnumeric:

            if labelAviso != None:
                labelAviso.destroy()
            if labelAlerta != None:
                labelAlerta.destroy()

            valorLinha = int(linha)
            valorColuna = int(coluna)

            tamanhoQuadrado = 300/tamanhoJogo

            desenha_x(valorLinha,valorColuna,tamanhoQuadrado)

            caixaLinha.delete(0, END)
            caixaColuna.delete(0, END)

            verificacao()

            tentativa_maquina(tamanhoQuadrado)

            verificacao()

    else:
        labelAviso = Label(confgTela,text=" campos", wraplength=175)
        labelAviso.config(width=28,height=4)
        labelAviso.place(x=500,y=50)

def botao_jogo_volta_menu_inicial():
    global labelLinha
    global caixaLinha
    global labelColuna
    global caixaColuna
    global botaoTentativa
    global botaoJogoVoltaMenuInicial
    global matrizJogo
    global tamanhoJogo
    global divisoria
    global matrizX
    global matrizMarquina
    global matrizTeste
    global matrizVerificacao
    global labelAviso
    global labelAlerta

    labelLinha.destroy()
    caixaLinha.destroy()
    labelColuna.destroy()
    caixaColuna.destroy()
    botaoTentativa.destroy()
    botaoJogoVoltaMenuInicial.destroy()
    confgTela.delete(divisoria)

    if labelAviso != None:
        labelAviso.destroy()

    for i in range(tamanhoJogo):
        for j in range(tamanhoJogo):
            confgTela.delete(matrizJogo[i][j])

    for i in range(len(matrizX)):
        for j in range(len(matrizX[i])):
            confgTela.delete(matrizX[i][j])

    for i in range(len(matrizMarquina)):
        confgTela.delete(matrizMarquina[i])

    
    desenha_menu_inicial()
    matrizJogo = []
    matrizX = []
    matrizMarquina = []
    matrizTeste = []
    matrizVerificacao = []

    if labelAviso != None:
        labelAviso.destroy()
    if labelAlerta != None:
        labelAlerta.destroy()

def desenha_layout_jogo():
    global labelLinha
    global caixaLinha
    global labelColuna
    global caixaColuna
    global botaoTentativa
    global botaoJogoVoltaMenuInicial

    labelLinha = Label(confgTela,text="Linha")
    labelLinha.config(width=7,height=1)
    labelLinha.place(x=475,y=150)

    caixaLinha = Entry(confgTela)
    caixaLinha.config(width=20)
    caixaLinha.place(x=550,y=150)

    labelColuna = Label(confgTela,text="Coluna")
    labelColuna.config(width=7,height=1)
    labelColuna.place(x=475,y=200)

    caixaColuna = Entry(confgTela)
    caixaColuna.config(width=20)
    caixaColuna.place(x=550,y=200)

    botaoTentativa = Button(confgTela,text="Tentativa",command=tentativa)
    botaoTentativa.config(width=15,height=3)
    botaoTentativa.place(x=525,y=300)

    botaoJogoVoltaMenuInicial = Button(confgTela,text="Voltar",command=botao_jogo_volta_menu_inicial)
    botaoJogoVoltaMenuInicial.config(width=15,height=3)
    botaoJogoVoltaMenuInicial.place(x=525,y=400)

def deleta_layout_escolha_personalizada():
    global escolhaUsuario
    global botaoEscolheu

    escolhaUsuario.destroy()
    botaoEscolheu.destroy()

def gerar_matriz_personalizada():
    global escolhaUsuario
    global tamanhoJogo

    escolha = escolhaUsuario.get()


    if escolha.isnumeric:

        valor = int(escolha)
        if valor <= 15 and valor % 2 != 0:
            tamanhoJogo = valor

            desenha_matriz_jogo(valor)
            deleta_layout_escolha_personalizada()
            desenha_layout_jogo()
        else:
            escolhaUsuario.delete(0, END)
    else:
        escolhaUsuario.delete(0, END)

def desenha_menu_escolha_personalizado():
    global escolhaUsuario
    global botaoEscolheu

    escolhaUsuario = Entry(confgTela)
    escolhaUsuario.config(width=20)
    escolhaUsuario.place(x=525,y=200)

    botaoEscolheu = Button(confgTela,text="Gerar matriz", command=gerar_matriz_personalizada)
    botaoEscolheu.config(width=17,height=2)
    botaoEscolheu.place(x=525,y=275)

def deleta_botoes_menu_escoha():
    global botaoPrimeiraEscolha
    global botaoSegundaEscolha
    global botaoTerceiraEscolha
    global botaoQuartaEscolha
    global botaoQuintaEscolha
    global botaoVoltaMenuEscolha

    botaoPrimeiraEscolha.destroy()
    botaoSegundaEscolha.destroy()
    botaoTerceiraEscolha.destroy()
    botaoQuartaEscolha.destroy()
    botaoQuintaEscolha.destroy()
    botaoVoltaMenuEscolha.destroy()

def desenha_matriz_jogo(tamanhoJogo):
    global matrizJogo
    global lugarJogo
    global matrizTeste
    global matrizVerificacao

    confgTela.delete(lugarJogo)

    tamnhoDivisoes = 300/tamanhoJogo

    # Coordenadas inicias dos dois eixos x e y de cada um dos dois ponto do retangulo
    primeiroX = 75
    primeiroY = 125

    segundoX = 75+tamnhoDivisoes
    segundoY = 125+tamnhoDivisoes

    # Guarda o reset do X
    guardaPrimeiroX = primeiroX
    guardaSegundoX = segundoX
    
    # Desenha a matriz do jogo
    for i in range(tamanhoJogo):
        matrizTemporaria = []
        for j in range(tamanhoJogo):
            matrizTemporaria.append(confgTela.create_rectangle(primeiroX,primeiroY,segundoX,segundoY,fill="white"))

            primeiroX += tamnhoDivisoes
            segundoX += tamnhoDivisoes
        
        matrizJogo.append(matrizTemporaria)

        primeiroX = guardaPrimeiroX
        segundoX = guardaSegundoX

        primeiroY += tamnhoDivisoes
        segundoY += tamnhoDivisoes
    
    # Elabora a matriz que será usada para testar a tentativa do jogador e da maquina
    for i in range(tamanhoJogo):
        temporaria = []
        for j in range(tamanhoJogo):
            temporaria.append(str(i + 1) + ";" + str(j + 1))
        matrizTeste.append(temporaria)
    
    # Elabora a matriz que a maquina ira usar para escolher uma celula que ainda no foi escolhida por ela ou pelo jogador
    
    for i in range(tamanhoJogo):
        temporaria = []
        for j in range(tamanhoJogo):
            temporaria.append(None)
        matrizVerificacao.append(temporaria)

def jogo_tres():
    global tamanhoJogo

    tamanhoJogo = 3
    desenha_matriz_jogo(tamanhoJogo)
    deleta_botoes_menu_escoha()
    desenha_layout_jogo()

def jogo_cinco():
    global tamanhoJogo

    tamanhoJogo = 5
    desenha_matriz_jogo(tamanhoJogo)
    deleta_botoes_menu_escoha()
    desenha_layout_jogo()

def jogo_sete():
    global tamanhoJogo

    tamanhoJogo = 7
    desenha_matriz_jogo(tamanhoJogo)
    deleta_botoes_menu_escoha()
    desenha_layout_jogo()

def jogo_nove():
    global tamanhoJogo

    tamanhoJogo = 9
    desenha_matriz_jogo(tamanhoJogo)
    deleta_botoes_menu_escoha()
    desenha_layout_jogo()

def jogo_personalizado():
    deleta_botoes_menu_escoha()
    desenha_menu_escolha_personalizado()
            
# Deleta o menu escolha do jogo e desenha o menu inicial
def escolha_volta_menu():
    global divisoria
    global lugarJogo
    global botaoPrimeiraEscolha
    global botaoSegundaEscolha
    global botaoTerceiraEscolha
    global botaoQuartaEscolha
    global botaoQuintaEscolha
    global botaoVoltaMenuEscolha

    confgTela.delete(divisoria)
    confgTela.delete(lugarJogo)
    botaoPrimeiraEscolha.destroy()
    botaoSegundaEscolha.destroy()
    botaoTerceiraEscolha.destroy()
    botaoQuartaEscolha.destroy()
    botaoQuintaEscolha.destroy()
    botaoVoltaMenuEscolha.destroy()

    desenha_menu_inicial()

# Desenha o menu de escolha do jogo
def desenha_escolha_jogo():
    global divisoria
    global lugarJogo
    global botaoPrimeiraEscolha
    global botaoSegundaEscolha
    global botaoTerceiraEscolha
    global botaoQuartaEscolha
    global botaoQuintaEscolha
    global botaoVoltaMenuEscolha

    divisoria = confgTela.create_line(425,25,425,775)

    # px75 py125 sx375 sy725
    lugarJogo = confgTela.create_rectangle(75,125,375,425,fill="blue")
    lugarJogo

    botaoPrimeiraEscolha = Button(confgTela,text="3x3",command=jogo_tres)
    botaoPrimeiraEscolha.config(width=13,height=2)
    botaoPrimeiraEscolha.place(x=550,y=150)

    botaoSegundaEscolha = Button(confgTela,text="5x5",command=jogo_cinco)
    botaoSegundaEscolha.config(width=13,height=2)
    botaoSegundaEscolha.place(x=550,y=200)

    botaoTerceiraEscolha = Button(confgTela,text="7x7",command=jogo_sete)
    botaoTerceiraEscolha.config(width=13,height=2)
    botaoTerceiraEscolha.place(x=550,y=250)

    botaoQuartaEscolha = Button(confgTela,text="9x9",command=jogo_nove)
    botaoQuartaEscolha.config(width=13,height=2)
    botaoQuartaEscolha.place(x=550,y=300)

    botaoQuintaEscolha = Button(confgTela,text="Personalizado",command=jogo_personalizado)
    botaoQuintaEscolha.config(width=13,height=2)
    botaoQuintaEscolha.place(x=550,y=350)

    botaoVoltaMenuEscolha = Button(confgTela,text="Voltar",command=escolha_volta_menu)
    botaoVoltaMenuEscolha.config(width=13,height=2)
    botaoVoltaMenuEscolha.place(x=550,y=425)


# Volta para o menu inicial
def info_volta_menu():
    global labelInfoMenu
    global labelInfo
    global botaoInfoVoltaMenu

    # Desetroi todos os elementos do menu de informação
    labelInfoMenu.destroy()
    labelInfo.destroy()
    botaoInfoVoltaMenu.destroy()

    # Desenha o menu inicial
    desenha_menu_inicial()

# Desenha o menu informação
def desenha_inforamacao():
    global labelInfoMenu
    global labelInfo
    global botaoInfoVoltaMenu

    labelInfoMenu = Label(confgTela,text="Mais informaçoe")
    labelInfoMenu.config(width=28, height=3)
    labelInfoMenu.place(x=300, y=50)

    labelInfo = Label(confgTela,text="texto")
    labelInfo.config(width=50, height=18)
    labelInfo.place(x=225, y=150)

    botaoInfoVoltaMenu = Button(confgTela,text="voltar",command=info_volta_menu)
    botaoInfoVoltaMenu.config(width=13, height=3)
    botaoInfoVoltaMenu.place(x=350, y=475)

# Desenha o jogo
def novo_jogo():
    deleta_menu_inicial()
    desenha_escolha_jogo()

# Desenha o menu informaçoes
def informacao():
    deleta_menu_inicial()
    desenha_inforamacao()

# Sai do jogo
def sair():
    tela.quit()

# Desenha o menu inicial
def desenha_menu_inicial():
    global labelIncial
    global botaoJogar
    global botaoInfo
    global botaoSair

    labelIncial = Label(confgTela, text="Menu Inicial")
    labelIncial.config(width=28, height=3)
    labelIncial.place(x=300, y=50)

    botaoJogar = Button(confgTela, text="Novo Jogo",command=novo_jogo)
    botaoJogar.config(width=35,height=3)
    botaoJogar.place(x=275,y=150)

    botaoInfo = Button(confgTela,text="Informaçôes",command=informacao)
    botaoInfo.config(width=35,height=3)
    botaoInfo.place(x=275,y=225)

    botaoSair = Button(confgTela,text="Sair",command=sair)
    botaoSair.config(width=35,height=3)
    botaoSair.place(x=275,y=300)

# Deleta o menu inicial
def deleta_menu_inicial():
    global labelIncial
    global botaoJogar
    global botaoInfo
    global botaoSair

    labelIncial.destroy()
    botaoJogar.destroy()
    botaoInfo.destroy()
    botaoSair.destroy()


# Função principal
if __name__ == "__main__":
    # Declara as variaveis que serão usadas
    # Menu inicial
    labelIncial = None
    botaoJogar = None
    botaoInfo = None
    botaoSair = None

    # Menu informação
    labelInfoMenu = None
    labelInfo = None
    botaoInfoVoltaMenu = None

    # Menu escolha
    divisoria = None
    lugarJogo = None
    botaoPrimeiraEscolha = None
    botaoSegundaEscolha = None
    botaoTerceiraEscolha = None
    botaoQuartaEscolha = None
    botaoQuintaEscolha = None
    botaoVoltaMenuEscolha = None
    tamanhoJogo = None
    matrizTeste = []
    matrizVerificacao = []

    # Durante o jogo
    matrizJogo = []
    escolhaUsuario = None
    botaoEscolheu = None
    labelLinha = None
    caixaLinha = None
    labelColuna = None
    caixaColuna = None
    botaoTentativa = None
    botaoJogoVoltaMenuInicial = None
    matrizX = []
    matrizMarquina = []
    labelAviso = None
    labelAlerta = None

    # Apos o jogo
    labelVenceu = None
    botaoVenceuSair = None
    botaoVenceuJogarNovamente = None
    labelPerdeu = None
    botaoPerdeuSair = None
    botaoPerdeuJogarNovamente = None
    labelEmpate = None
    botaoEmpateSair = None
    botaoEmpateJogarNovamente = None

    # Define a tela em que o jogo sera feito
    tela = Tk()

    # Configurações da tela do jogo
    tela.title("Jogo da velha")
    tela.geometry("800x600")
    confgTela = Canvas(tela, width=800, height=600, bg="blue")

    # Faz o layout
    desenha_layout()

    # Faz o menu inicial
    desenha_menu_inicial()
    
    # Junta todos os botõe elementos na tela
    confgTela.pack()
    tela.mainloop()