from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def reddit_3(x, y, musica):
    janela = Window(1000, 700)
    teclado = Keyboard()

    fundo = GameImage("img/fundo_reddit.png")

    jogador = personagem.criar()
    jogador.set_position(x, y)

    # Poscionamento das plataformas
    plataforma = [GameImage("img/reddit_plataforma1x1.png"), GameImage("img/reddit_plataforma1x1.png"), GameImage("img/check.png"), GameImage("img/reddit_plataforma1x1.png"), GameImage("img/reddit_plataforma1x1.png")]
    plataforma[0].set_position(0, 660)
    plataforma[1].set_position(960, 160)
    plataforma[2].set_position(500, 200)
    plataforma[3].set_position(200, 660)
    plataforma[4].set_position(600, 360)
    fila1 = 0
    fila2 = 0
    cont = 0
    unico = 1

    vazia = []
    for i in range(4):
        vazia.append(GameImage("img/reddit_plataformavazia.png"))
        vazia[i].set_position(200 + 200 * i, 660)
    for i in range(3):
        vazia.append(GameImage("img/reddit_plataformavazia.png"))
        vazia[i + 4].set_position(800, 560 - 100 * i)
    for i in range(4):
        vazia.append(GameImage("img/reddit_plataformavazia.png"))
        vazia[i + 7].set_position(600 - 200 * i, 360)
    for i in range(2):
        vazia.append(GameImage("img/reddit_plataformavazia.png"))
        vazia[i + 11].set_position(0, 260 - 100 * i)
    for i in range(4):
        vazia.append(GameImage("img/reddit_plataformavazia.png"))
        vazia[i + 13].set_position(200 + 200 * i, 160)

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

            if cont >= 2:
                cont = 0
                plataforma.pop(len(plataforma) - 1)
                plataforma.pop(len(plataforma) - 1)
                plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
                plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
                plataforma[3].set_position(vazia[fila1].x, vazia[fila1].y)
                plataforma[4].set_position(vazia[fila2 + 7].x, vazia[fila2 + 7].y)
                fila1 = (fila1 + 1) % 7
                fila2 = (fila2 + 1) % 10

        if teclado.key_pressed("r") and unico == 1:
            fase, x, y = personagem.restart()
            unico = 0

            if fase == 7:
                cont = 2
                morreu = False
                jogador.set_position(x, y)
            else:
                return fase, x, y
        if not teclado.key_pressed("r"):
            unico = 1

        for i in range(len(tiros)):
            if tiros[i][0].collided(plataforma[2]):
                personagem.salvar(7, jogador.x, jogador.y)
                tiros.pop(i)
                break

        if jogador.x + jogador.height <= 0:
            return 6, 1000 - jogador.width, 400 - jogador.height

        if jogador.x >= janela.width:
            return 8, 0, jogador.y

        if jogador.y >= 700:
            morreu = True

        fundo.draw()

        for i in range(len(tiros)):
            tiros[i][0].draw()

        for i in range(len(vazia)):
            vazia[i].draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        if not musica.is_playing():
            musica.play()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        jogador.draw()
        janela.update()




