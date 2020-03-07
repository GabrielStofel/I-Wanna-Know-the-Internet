from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def reddit_1(x, y, musica):
    janela = Window(1000, 700)
    janela.set_title("Reddit 1")
    teclado = Keyboard()

    fundo = GameImage("img/fundo_reddit.png")

    jogador = personagem.criar()
    jogador.set_position(x, y)

    # Poscionamento das plataformas
    plataforma = []
    for i in range(5):
        plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
    plataforma[0].set_position(0, 400)
    plataforma[1].set_position(160, 360)
    plataforma[2].set_position(400, 360)
    plataforma[3].set_position(720, 360)
    plataforma[4].set_position(960, 400)

    plataforma.append(GameImage("img/check.png"))
    plataforma[5].set_position(400, 240)

    # Poscionamento dos obstaculos
    obstaculo = []
    obstaculo.append(GameImage("img/reddit_upvote21.png"))
    obstaculo[0].set_position(80, 400)
    obstaculo.append(GameImage("img/reddit_downvote23.png"))
    obstaculo[1].set_position(40, 240 - jogador.height)
    obstaculo.append(GameImage("img/reddit_downvote.png"))
    obstaculo[2].set_position(0, 320 - jogador.height)
    obstaculo.append(GameImage("img/reddit_downvote.png"))
    obstaculo[3].set_position(960, 320 - jogador.height)

    # Posicionamento e variavel para o reset do pulo
    reset = GameImage("img/reset.png")
    reset.set_position(640, 360)
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
                if tiros[i][0].collided(plataforma[5]):
                    personagem.salvar(5, jogador.x, jogador.y)
                    tiros.pop(i)
                    break

        if teclado.key_pressed("r"):
            fase, x, y = personagem.restart()

            if fase == 5:
                morreu = False
                jogador.set_position(x, y)
            else:
                return fase, x, y

        for i in range(len(obstaculo)):
            if jogador.collided(obstaculo[i]):
                morreu = True

        if jogador.x + jogador.height < 0:
            jogador.x = 0

        if jogador.x > janela.width:
            return 6, 0, 400 - jogador.height

        if jogador.y >= 700:
            morreu = True

        fundo.draw()

        for i in range(len(tiros)):
            tiros[i][0].draw()

        if cont >= 5:
            reset.draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(obstaculo)):
            obstaculo[i].draw()

        if not musica.is_playing():
            musica.play()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        jogador.draw()
        janela.update()
