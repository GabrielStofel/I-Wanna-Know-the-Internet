from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def fase_1(x, y, musica):
    janela = Window(1000, 700)

    teclado = Keyboard()

    jogador = personagem.criar()
    fundo = GameImage('img/background-1.png')
    jogador.set_position(x, y)

    plataforma = [GameImage("img/plataforma-1.png"), GameImage("img/plataforma-1.png"), GameImage("img/plataforma-1.png"), GameImage("img/plataforma-1.png"), GameImage("img/check.png")]
    plataforma[0].y = janela.height * 0.6
    plataforma[1].y = janela.height * 0.6
    plataforma[1].x = plataforma[1].width / 3
    plataforma[1].y = janela.height * 0.6
    plataforma[1].x = janela.width - plataforma[1].width
    plataforma[2].y = janela.height * 0.6
    plataforma[2].x = plataforma[1].x - plataforma[2].width / 2
    plataforma[3].y = janela.height * 0.6
    plataforma[3].x = plataforma[0].width * 0.5
    plataforma[4].set_position(150, 300)

    instrucao = [GameImage("img/instrucao_tiro.png"), GameImage("img/instrucao_pulo_triplo.png")]

    for i in range(len(instrucao)):
        instrucao[i].set_position((janela.width - instrucao[i].width) / 2, 100)

    # Variaveis obrigatorias de cada fase
    temptiro = 0
    tiros = []
    pulo = 0
    pulando = -1
    click = 0
    atual = 0
    animacao = 0
    morreu = False

    # Variavel para aparecer o reset do pulo
    reset = GameImage("img/reset.png")
    reset.set_position(janela.width / 2, janela.height * 0.6)
    cont = 5

    while True:
        if 0 < janela.delta_time() < 1 and not morreu:
            cont += janela.delta_time()
            animacao = personagem.mov(jogador, pulando, plataforma, janela, animacao)
            pulo, pulando, click = personagem.pulo(jogador, plataforma, pulo, pulando, click, janela)
            temptiro, atual = personagem.tiro(jogador, tiros, temptiro, atual, janela)

            if jogador.x + jogador.width <= 0:
                return 0, janela.width - jogador.width, janela.height * 0.5 - jogador.height

            if jogador.x >= janela.width:
                return 2, 0, janela.height * 0.65 - jogador.height

            if jogador.y >= 700:
                morreu = True

            for i in range(len(tiros)):
                if tiros[i][0].collided(plataforma[4]):
                    personagem.salvar(1, jogador.x, jogador.y)
                    tiros.pop(i)
                    break

            if cont >= 5:
                if jogador.collided(reset):
                    cont = 0
                    pulo += 1

        if teclado.key_pressed("r"):
            fase, inix, iniy = personagem.restart()

            if fase == 1:
                cont = 5
                morreu = False
                jogador.set_position(inix, iniy)
            else:
                return fase, inix, iniy

        fundo.draw()
        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(tiros)):
            tiros[i][0].draw()

        if jogador.x < plataforma[0].width / 2 and not morreu:
            instrucao[0].draw()

        else:
            if not morreu:
                instrucao[1].draw()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        if cont >= 5:
            reset.draw()

        if not musica.is_playing():
            musica.play()

        jogador.draw()
        janela.update()
