from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def reddit_2(x, y, musica):
    janela = Window(1000, 700)
    teclado = Keyboard()

    fundo = GameImage("img/fundo_reddit.png")

    jogador = personagem.criar()
    jogador.set_position(x, y)
    derrotado = False

    # Poscionamento das plataformas
    plataforma = []
    for i in range(11):
        plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
    plataforma[0].set_position(0, 400)
    plataforma[1].set_position(0, 300)
    plataforma[2].set_position(0, 200)
    plataforma[3].set_position(0, 100)
    for i in range(3):
        plataforma[i + 4].set_position(310 + 40 * i, 660)
    plataforma[7].set_position(650, 660)
    plataforma[8].set_position(880, 660)
    plataforma[9].set_position(920, 660)
    plataforma[10].set_position(960, 660)

    plataforma.append(GameImage("img/check.png"))
    plataforma[11].set_position(925, 500)

    # Poscionamento dos obstaculos
    obstaculo = []
    obstaculo.append(GameImage("img/reddit_upvote_direita10.png"))
    obstaculo[0].set_position(140, 100)
    obstaculo.append(GameImage("img/reddit_upvote.png"))
    obstaculo[1].set_position(190, 500)
    obstaculo.append(GameImage("img/reddit_downvote_esquerda7.png"))
    obstaculo[2].set_position(260, 20)
    obstaculo.append(GameImage("img/reddit_upvote_direita6.png"))
    obstaculo[3].set_position(260, 460)
    obstaculo.append(GameImage("img/reddit_downvote_esquerda7.png"))
    obstaculo[4].set_position(380, 300)

    # Posicionamento e variavel para o reset do pulo
    reset = GameImage("img/reset.png")
    reset.set_position(200, 440)
    cont = 5

    # Variaveis obrigatorias de cada fase
    temptiro = 0
    tiros = []
    pulo = 0
    pulando = -1
    click = 0
    atual = 0
    animacao = 0
    morreu = False

    while True:

        if 0 < janela.delta_time() < 1 and not morreu:
            cont += janela.delta_time()
            animacao = personagem.mov(jogador, pulando, plataforma, janela, animacao)
            pulo, pulando, click = personagem.pulo(jogador, plataforma, pulo, pulando, click, janela)
            temptiro, atual = personagem.tiro(jogador, tiros, temptiro, atual, janela)

            if cont >= 5:
                if jogador.collided(reset):
                    cont = 0
                    pulo += 1

            for i in range(len(tiros)):
                if tiros[i][0].collided(plataforma[11]):
                    personagem.salvar(6, jogador.x, jogador.y)
                    tiros.pop(i)
                    break

        if teclado.key_pressed("r"):
            fase, x, y = personagem.restart()

            if fase == 6:
                morreu = False
                cont = 5
                jogador.set_position(x, y)
            else:
                return fase, x, y

        for i in range(len(obstaculo)):
            if jogador.collided(obstaculo[i]):
                morreu = True

        if jogador.x + jogador.height <= 0:
            return 5, 1000 - jogador.width, 400 - jogador.height

        if jogador.x > janela.width:
            return 7, 0, jogador.y

        if jogador.y >= 700:
            morreu = True

        fundo.draw()

        for i in range(len(tiros)):
            tiros[i][0].draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(obstaculo)):
            obstaculo[i].draw()

        if cont >= 5:
            reset.draw()

        if not musica.is_playing():
            musica.play()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        jogador.draw()
        janela.update()
