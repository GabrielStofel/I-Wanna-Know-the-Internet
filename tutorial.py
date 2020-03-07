from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem


def fase_0(inix, iniy, musica):
    teclado = Keyboard()
    janela = Window(1000, 700)

    jogador = personagem.criar()
    fundo = GameImage('img/background-1.png')
    jogador.set_position(inix, iniy)
    plataforma = [GameImage("img/plataforma-1.png"), GameImage("img/plataforma-1.png"), GameImage("img/plataforma-1.png")]
    plataforma[0].y = janela.height * 0.6
    plataforma[1].y = janela.height * 0.6
    plataforma[1].x = plataforma[1].width + 120
    plataforma[2].y = janela.height * 0.5
    plataforma[2].x = plataforma[1].x + plataforma[2].width + 160
    instrucao = [GameImage("img/instrucao1.png"), GameImage("img/instrucao2.png"), GameImage("img/instrucao3.png")]

    for i in range(3):
        instrucao[i].set_position((janela.width - instrucao[i].width)/2, 100)

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

        if janela.delta_time() < 1 and not morreu:
            animacao = personagem.mov(jogador, pulando, plataforma, janela, animacao)
            pulo, pulando, click = personagem.pulo(jogador, plataforma, pulo, pulando, click, janela)
            temptiro, atual = personagem.tiro(jogador, tiros, temptiro, atual, janela)

        if teclado.key_pressed("r"):
            fase, inix, iniy = personagem.restart()

            if fase == 0:
                morreu = False
                jogador.set_position(inix, iniy)
            else:
                return fase, inix, iniy

        if jogador.x >= janela.width:
            return 1, 0, janela.height * 0.6 - jogador.height

        if jogador.x < 0:
            jogador.x = 0

        if jogador.y >= 700:
            morreu = True

        fundo.draw()
        if jogador.x < plataforma[0].width/2 and not morreu:
            instrucao[0].draw()
        elif plataforma[1].x > jogador.x >= plataforma[0].width/2 and not morreu:
            instrucao[1].draw()
        elif jogador.x >= plataforma[1].x and not morreu:
            instrucao[2].draw()

        for i in range(3):
            plataforma[i].draw()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        for i in range(len(tiros)):
            tiros[i][0].draw()

        if not musica.is_playing():
            musica.play()

        jogador.draw()
        janela.update()



