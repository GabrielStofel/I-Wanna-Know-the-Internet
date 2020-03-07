from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def fase_youtube_2(x, y, musica):
    janela = Window(1000, 700)
    janela.set_title("Youtube-b")

    teclado = Keyboard()

    jogador = personagem.criar()
    jogador.set_position(x, y)

    fundo = GameImage('img/fundo_youtube.png')

    plataforma = [GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma.png"), GameImage("img/youtube_plataforma_vertical.png"), GameImage("img/check.png")]
    plataforma[0].x = 0
    plataforma[0].y = janela.height * 0.5
    plataforma[1].x = plataforma[1].width * 1.1
    plataforma[1].y = janela.height * 0.65
    plataforma[2].x = plataforma[1].width * 2.1
    plataforma[2].y = janela.height * 0.65
    plataforma[3].x = janela.width - plataforma[1].width
    plataforma[3].y = janela.height * 0.5

    obstaculo = [GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png"), GameImage("img/thumbs-down.png")]
    obstaculo[0].set_position(plataforma[0].width + 10, plataforma[0].y + 10)
    obstaculo[1].set_position(obstaculo[0].x + (obstaculo[0].width * 2.5), obstaculo[0].y)
    obstaculo[2].set_position(obstaculo[1].x + (obstaculo[0].width * 1.2), obstaculo[0].y)
    obstaculo[3].set_position(obstaculo[2].x + (obstaculo[0].width * 1.2), obstaculo[0].y)
    obstaculo[4].set_position(obstaculo[3].x + (obstaculo[0].width * 1.2), obstaculo[0].y)
    obstaculo[5].set_position(obstaculo[4].x + (obstaculo[0].width * 1.2), obstaculo[0].y)
    obstaculo[6].set_position(obstaculo[5].x + (obstaculo[0].width * 1.2), obstaculo[0].y)
    obstaculo[7].set_position(plataforma[3].x - obstaculo[0].width - 10, obstaculo[0].y)

    # Posicionando a plataforma vertical e caixa check
    plataforma[4].x = (obstaculo[3].x + obstaculo[3].width + obstaculo[4].x) / 2 - plataforma[4].width / 2
    plataforma[4].y = obstaculo[0].y - plataforma[4].height - 20
    plataforma[5].x = janela.width * 0.9
    plataforma[5].y = janela.height * 0.3

    # Reset de Pulo da Fase
    reset = GameImage("img/reset.png")
    reset.y = janela.height * 0.5
    reset.x = (obstaculo[7].x + (obstaculo[6].x + obstaculo[6].width)) / 2 - reset.width / 2

    # Variavel para aparecer o reset do pulo
    cont = 5

    # Variaveis obrigatorias de cada fase
    temptiro = 0
    tiros = []
    pulo = 0
    pulando = -1
    click = 0
    atual = 0
    animacao = 0
    fase = 3
    morreu = False

    while True:
        if janela.delta_time() < 1:
            if not morreu:
                cont += janela.delta_time()
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

        if jogador.x >= janela.width:
            return fase + 1, 0, janela.height * 0.6 - jogador.height

        if jogador.x < 0:
            return fase - 1, janela.width - jogador.width, janela.height * 0.45 - jogador.height

        if jogador.y >= 700:
            morreu = True

        fundo.draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(obstaculo)):
            obstaculo[i].draw()

            if jogador.collided(obstaculo[i]):
                janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))
                morreu = True

        for i in range(len(tiros)):
            if i in range(len(tiros)):
                tiros[i][0].draw()

                if tiros[i][0].collided(plataforma[4]):
                    tiros.pop(i)

                elif tiros[i][0].collided(plataforma[5]):
                    personagem.salvar(fase, jogador.x, jogador.y)
                    tiros.pop(i)

        if cont >= 5:
            reset.draw()

        if not musica.is_playing():
            musica.play()

        jogador.draw()
        janela.update()


