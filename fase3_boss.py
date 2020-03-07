from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import personagem
import random


def fase_youtube_boss(x, y, musica):
    janela = Window(1000, 700)
    janela.set_title("Youtube")

    teclado = Keyboard()

    jogador = personagem.criar()
    jogador.set_position(x, y)

    fundo = GameImage('img/fundo_youtube.png')

    plataforma = [GameImage("img/youtube_plataforma_boss.png")]

    # Posicionando as plataformas
    plataforma[0].x = 0
    plataforma[0].y = janela.height * 0.6

    # Variaveis obrigatorias de cada fase
    temptiro = 0
    tiros = []
    pulo = 0
    pulando = -1
    click = 0
    atual = 0
    animacao = 0

    # Criando o chefe
    boss = GameImage("img/youtube_boss.png")

    # Variaveis pertencentes ao Boss e Chuva
    vida_boss = 3
    contador_boss = 0
    nao_tem_boss = False
    tempo_para_aparecer = random.randint(15, 20)
    boss_pos1 = janela.width / 4 - boss.width / 2
    boss_pos2 = janela.width * 3 / 4 - boss.width / 2
    boss.set_position(boss_pos2, plataforma[0].y - boss.height)

    demonetizacao = []
    contador_tiro = 0

    vitoria = False
    morreu = False

    while True:
        fundo.draw()

        janela.draw_text("♥  " * vida_boss, janela.width * 0.41, janela.height * 0.15, 60, (255, 0, 0), "Arial", True)

        if vitoria:
            janela.draw_text("Parabéns! Siga adiante!", janela.width * 0.32, janela.height * 0.12, 40, (255, 255, 255), "Arial", True)

        if nao_tem_boss and not morreu:
            contador_boss += janela.delta_time()
            contador_tiro += janela.delta_time()

            if contador_tiro > 0.1:
                moeda = GameImage("img/demonetization.png")
                moeda.x = random.randint(0, 1000 - moeda.width)
                moeda.y = -moeda.height
                demonetizacao.append(moeda)
                contador_tiro = 0

            if contador_boss > tempo_para_aparecer:
                nao_tem_boss = False
                tempo_para_aparecer = random.randint(15, 20)
                contador_boss = 0

                if jogador.x < janela.width / 2:
                    boss.set_position(boss_pos2, plataforma[0].y - boss.height)

                else:
                    boss.set_position(boss_pos1, plataforma[0].y - boss.height)

        else:
            boss.draw()

        for i in range(len(demonetizacao)):
            if i in range(len(demonetizacao)):
                demonetizacao[i].draw()

                if not morreu:
                    demonetizacao[i].y += 400 * janela.delta_time()

                    if demonetizacao[i].collided(jogador):
                        morreu = True

                    elif demonetizacao[i].collided(plataforma[0]):
                        demonetizacao.pop(i)

        if janela.delta_time() < 1:
            if not morreu:
                animacao = personagem.mov(jogador, pulando, plataforma, janela, animacao)
                pulo, pulando, click = personagem.pulo(jogador, plataforma, pulo, pulando, click, janela)
                temptiro, atual = personagem.tiro(jogador, tiros, temptiro, atual, janela)

            if teclado.key_pressed("r"):
                fase, x, y = personagem.restart()

                return fase, x, y

        if jogador.collided(boss):
            morreu = True

        if jogador.x < 0:
            jogador.x = 0

        elif jogador.x + jogador.width > janela.width and not vitoria:
            jogador.x = janela.width - jogador.width

        elif jogador.x > janela.width:
            personagem.salvar(5, 0, 400 - jogador.height)
            return 5, 0, 400 - jogador.height

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(tiros)):
            tiros[i][0].draw()

            if tiros[i][0].collided(boss):
                tiros.pop(i)
                boss.set_position(-boss.width, 0)
                vida_boss -= 1

                if vida_boss >= 1:
                    nao_tem_boss = True

                else:
                    vitoria = True

                break

        if not musica.is_playing():
            musica.play()

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        jogador.draw()
        boss.draw()
        janela.update()
