from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def fase_youtube_1(x, y, musica):
    janela = Window(1000, 700)
    janela.set_title("Youtube-a")

    teclado = Keyboard()

    jogador = personagem.criar()
    jogador.set_position(x, y)

    fundo = GameImage('img/fundo_youtube.png')

    plataforma = [GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/check.png")]
    plataforma[0].set_position(0, janela.height * 0.65)
    plataforma[1].set_position(plataforma[0].width + 10, janela.height * 0.31)
    plataforma[2].x = plataforma[1].width * 2.1
    plataforma[2].y = janela.height * 0.7
    plataforma[3].x = janela.width - plataforma[1].width
    plataforma[3].y = janela.height * 0.45
    plataforma[4].set_position(plataforma[3].x + plataforma[1].width / 2, janela.height * 0.25)

    obstaculo = [GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"),
                 GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png")]

    obstaculo[0].set_position(plataforma[0].width + 10, plataforma[0].y + 10)
    obstaculo[1].set_position(obstaculo[0].x, obstaculo[0].y - (obstaculo[0].height * 1.4))
    obstaculo[2].set_position(obstaculo[1].x, obstaculo[1].y - (obstaculo[1].height * 1.4))
    obstaculo[3].set_position(obstaculo[2].x, obstaculo[2].y - (obstaculo[2].height * 1.4))
    obstaculo[4].set_position(obstaculo[3].x, obstaculo[3].y - (obstaculo[3].height * 1.4))
    obstaculo[5].set_position(plataforma[1].x + plataforma[1].width - obstaculo[5].width, plataforma[0].y + 10)
    obstaculo[6].set_position(plataforma[1].x + plataforma[1].width - obstaculo[5].width, obstaculo[5].y - (obstaculo[5].height * 1.4))
    obstaculo[7].set_position(plataforma[1].x + plataforma[1].width - obstaculo[5].width, obstaculo[6].y - (obstaculo[6].height * 1.4))
    obstaculo[8].set_position(plataforma[1].x + plataforma[1].width - obstaculo[5].width, obstaculo[7].y - (obstaculo[7].height * 1.4))
    obstaculo[9].set_position(plataforma[1].x + plataforma[1].width - obstaculo[5].width, obstaculo[8].y - (obstaculo[8].height * 1.4))
    obstaculo[10].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, plataforma[1].y + 100)
    obstaculo[11].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[10].y - (obstaculo[10].height * 1.4))
    obstaculo[12].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[11].y - (obstaculo[11].height * 1.4))
    obstaculo[13].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[12].y - (obstaculo[12].height * 1.4))
    obstaculo[14].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[13].y - (obstaculo[13].height * 1.4))
    obstaculo[15].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[14].y - (obstaculo[14].height * 1.4))
    obstaculo[16].set_position(plataforma[2].width / 2 + plataforma[2].x - 20, obstaculo[15].y - (obstaculo[15].height * 1.4))
    obstaculo[17].set_position(plataforma[3].x, plataforma[0].y + 10)
    obstaculo[18].set_position(obstaculo[17].x, obstaculo[0].y - (obstaculo[17].height * 1.4))
    obstaculo[19].set_position(obstaculo[18].x, obstaculo[1].y - (obstaculo[18].height * 1.4))

    # Reset de Pulo da Fase
    reset = GameImage("img/reset.png")
    reset.y = janela.height * 0.5
    reset.x = janela.width * 0.15
    reset2 = GameImage("img/reset.png")
    reset2.y = janela.height * 0.4
    reset2.x = janela.width * 0.15
    reset3 = GameImage("img/reset.png")
    reset3.y = reset.y
    reset3.x = plataforma[2].x + (plataforma[2].width * 0.75)

    # Variavel para aparecer o reset do pulo
    cont = 5
    cont2 = 5
    cont3 = 5

    # Variaveis obrigatorias de cada fase
    temptiro = 0
    tiros = []
    pulo = 0
    pulando = -1
    click = 0
    atual = 0
    animacao = 0
    fase = 2
    morreu = False

    while True:
        if janela.delta_time() < 1:
            if not morreu:
                cont += janela.delta_time()
                cont2 += janela.delta_time()
                cont3 += janela.delta_time()
                animacao = personagem.mov(jogador, pulando, plataforma, janela, animacao)
                pulo, pulando, click = personagem.pulo(jogador, plataforma, pulo, pulando, click, janela)
                temptiro, atual = personagem.tiro(jogador, tiros, temptiro, atual, janela)

            if teclado.key_pressed("r"):
                fase, x, y = personagem.restart()

                if fase == 3:
                    morreu = False
                    jogador.set_position(x, y)

                else:
                    return fase, x, y

            if cont >= 5:
                if jogador.collided(reset):
                    cont = 0
                    pulo += 1

            if cont2 >= 5:
                if jogador.collided(reset2):
                    cont2 = 0
                    pulo += 1

            if cont3 >= 5:
                if jogador.collided(reset3):
                    cont3 = 0
                    pulo += 1

        if jogador.x >= janela.width:
            return fase + 1, 0, janela.height * 0.5 - jogador.height

        if jogador.x + jogador.width <= 0:
            return fase - 1, janela.width - jogador.width, janela.height * 0.6 - jogador.height

        if jogador.y >= 700:
            morreu = True

        fundo.draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(obstaculo)):
            obstaculo[i].draw()

            if jogador.collided(obstaculo[i]):
                morreu = True
                janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.08, janela.height * 0.1, 35, (255, 255, 255))

        for i in range(len(tiros)):
            if i in range(len(tiros)):
                tiros[i][0].draw()

                if tiros[i][0].collided(plataforma[4]):
                    personagem.salvar(fase, jogador.x, jogador.y)
                    tiros.pop(i)

        if cont >= 5:
            reset.draw()

        if cont2 >= 5:
            reset2.draw()

        if cont3 >= 5:
            reset3.draw()

        if not musica.is_playing():
            musica.play()

        jogador.draw()
        janela.update()


