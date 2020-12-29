import time
import os
import random

os.system('cls')

#print('Jogo da velha com python')

#ball = str(input('Escolha X ou O: '))

jogardnv = 'sim'
jogadas = 0
quemJoga = 2 
maxjogadas = 9
vit = 'não'

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global jogadas
    global velha
    os.system('cls')
    print("Jogo da velha com python")
    print("   0   1   2")
    print("0: " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1: " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2: " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    time.sleep(0.5)
    print(f"Jogadas feitas: {jogadas}")

def jogadorjg():
    global jogadas
    global quemJoga
    global maxjogadas
    if quemJoga == 2 and jogadas<maxjogadas:
        try:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            while velha[linha][coluna] != " ":
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))
            velha[linha][coluna] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha ou coluna está inválida.")
            os.system("pause")

def pcjg():
    global jogadas
    global quemJoga
    global maxjogadas
    if quemJoga == 1 and jogadas<maxjogadas:
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna] != " ":
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
        velha[linha][coluna] = "O"
        jogadas += 1
        quemJoga = 2

def vitoriaveri():
    global velha
    vitoria = "não"
    veri = ["X", "O"]
    for sim in veri:
        vitoria = "não"
        ilinha  = 0
        icoluna = 0
        while ilinha<3:
            soma = 0
            icoluna = 0
            while icoluna<3:
                if(velha[ilinha][icoluna] == sim):
                    soma += 1
                icoluna += 1
            ilinha += 1
            if(soma == 3):
                vitoria = sim
                break
        if(vitoria != "não" ):
            break
        # coluna:
        ilinha  = 0
        icoluna = 0
        while icoluna<3:
            soma = 0
            ilinha = 0
            while ilinha<3:
                if(velha[ilinha][icoluna] == sim):
                    soma += 1
                ilinha += 1
            if(soma == 3):
                vitoria = sim
                break
            icoluna += 1
        if(vitoria != "não" ):
            break

        #diagonal1
        soma = 0
        idiag = 0
        while idiag <3:
            if(velha[idiag][idiag] == sim):
                soma += 1
            idiag += 1
        if(soma == 3):
            vitoria = sim
            break

        #diagonal2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >=0:
            if(velha[idiagl][idiagc] == sim):
                soma += 1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = sim
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxjogadas
    global vit
    jogadas = 0
    quemJoga = 2 
    maxjogadas = 9
    vit = 'não'

    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while(jogardnv == "sim"):
    while True:
        tela()
        jogadorjg()
        pcjg()
        tela()
        vit = vitoriaveri()
        if(vit != "não") or (jogadas >= maxjogadas):
            break

    print("End game")
    if(vit == "X" or vit == "O"):
        print(f"Resultado: Jogador {vit} ganhou")
    else:
        print("Empate!")
    jogardnv = input("Quer jogar novamente? ")
    if jogardnv == "não":
        break
    redefinir()