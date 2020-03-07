from PPlay.keyboard import *
from PPlay.sprite import *


def criar():
    personagem = Sprite('img/player.png', 6)
    return personagem


def restart():
    arq = open("checkpoint.txt", 'r')
    fase = int(arq.readline())
    x = arq.readline()
    x = int(x.strip("\n"))
    y = arq.readline()
    y = int(y.strip("\n"))
    arq.close()

    return fase, x, y


def salvar(fase, x, y):
    arq = open("checkpoint.txt", 'w')

    arq.write(str(fase))
    arq.write("\n")

    for i in range(len(str(x))):
        if str(x)[i] != ".":
            arq.write(str(x)[i])

        else:
            break

    arq.write("\n")
    for i in range(len(str(y))):
        if str(y)[i] != ".":
            arq.write(str(y)[i])

        else:
            break


def mov(jogador, pulando, plataforma, janela, animacao):
    animacao += janela.delta_time()
    teclado = Keyboard()
    atual = jogador.get_curr_frame()
    if teclado.key_pressed("LEFT"):
        if atual < 3:
            animacao = 0
            jogador.set_curr_frame(5)
        elif atual >= 3 and animacao >= 0.2:
            animacao = 0
            if atual == 3:
                jogador.set_curr_frame(5)
            else:
                jogador.set_curr_frame(atual - 1)
        jogador.x -= 200 * janela.delta_time()
        for i in range(len(plataforma)):
            if pulando != 0 and jogador.collided(plataforma[i]):
                jogador.x += 200 * janela.delta_time()

    if teclado.key_pressed("RIGHT"):
        if atual >= 3:
            animacao = 0
            jogador.set_curr_frame(0)
        elif atual < 3 and animacao >= 0.2:
            animacao = 0
            if atual == 2:
                jogador.set_curr_frame(0)
            else:
                jogador.set_curr_frame(atual + 1)
        jogador.x += 200 * janela.delta_time()
        for i in range(len(plataforma)):
            if pulando != 0 and jogador.collided(plataforma[i]):
                jogador.x -= 200 * janela.delta_time()

    return animacao


def pulo(jogador, plataforma, pulo, pulando, click, janela):
    teclado = Keyboard()
    if pulo != 0:
        if teclado.key_pressed("z") and click == 0:
            pulando = 65
            pulo -= 1
            click = 1
        if not teclado.key_pressed("z"):
            click = 0

    if pulando > 0:
        jogador.y -= 300 * janela.delta_time()
        pulando -= 1
        if pulando == 0:
            pulando = -1
        for i in range(len(plataforma)):
            if jogador.collided(plataforma[i]):
                jogador.y += 300 * janela.delta_time()

    if pulando == 0:
        jogador.y -= 300 * janela.delta_time()
        pulando -= 1
        if pulando == 0:
            pulando = -1

    if pulando < 0:
        jogador.y += 300 * janela.delta_time()
        for i in range(len(plataforma)):
            if jogador.collided(plataforma[i]):
                while jogador.collided(plataforma[i]):
                    jogador.y -= 1 * janela.delta_time()
                jogador.y += 1 * janela.delta_time()

    if pulando <= 0:
        for i in range(len(plataforma)):
            if jogador.x + jogador.width >= plataforma[i].x and jogador.x <= plataforma[i].x + plataforma[i].width and plataforma[i].y + 10 >= jogador.y + jogador.height >= plataforma[i].y:
                pulando = 0
                pulo = 2

    return pulo, pulando, click


def tiro(jogador, tiros, temptiros, atual, janela):
    teclado = Keyboard()
    temptiros += janela.delta_time()
    frame = jogador.get_curr_frame()
    if teclado.key_pressed("x") and temptiros >= 0.5:
        if atual == 0:
            tiros.append([Sprite("img/tiro_0.png"), frame])
            if frame < 3:
                tiros[(len(tiros)) - 1][0].set_position(jogador.x + jogador.width, jogador.y + 0.25 * jogador.height)
            else:
                tiros[(len(tiros)) - 1][0].set_position(jogador.x, jogador.y + 0.25 * jogador.height)
            temptiros = 0
            atual = 1
        else:
            tiros.append([Sprite("img/tiro_1.png"), frame])
            if frame < 3:
                tiros[(len(tiros)) - 1][0].set_position(jogador.x + jogador.width, jogador.y + 0.25 * jogador.height)
            else:
                tiros[(len(tiros)) - 1][0].set_position(jogador.x, jogador.y + 0.25 * jogador.height)
            temptiros = 0
            atual = 0

    for i in range(len(tiros)):
        if tiros[i][1] < 3:
            tiros[i][0].x += 400 * janela.delta_time()
        else:
            tiros[i][0].x -= 400 * janela.delta_time()

    erro = 0
    for i in range(len(tiros) - erro):
        i -= erro
        if tiros[i][0].x <= 0 or tiros[i][0].x + tiros[i][0].width >= janela.width:
            tiros.pop(i)
            erro += 1

    return temptiros, atual
