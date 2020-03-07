from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.keyboard import *
import random
import personagem


def reddit_boss(x, y, musica):
    janela = Window(1000, 700)
    teclado = Keyboard()

    fundo = GameImage("img/fundo_reddit.png")

    jogador = personagem.criar()
    jogador.set_position(x, y)

    # Posicionamento das plataformas
    plataforma = [GameImage("img/reddit_plataformaboss.png")]
    plataforma[0].set_position(0, 600)
    for i in range(3):
        plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
        plataforma[i + 1].set_position(80 + 40 * i, 500)
    for i in range(3):
        plataforma.append(GameImage("img/reddit_plataforma1x1.png"))
        plataforma[i + 4].set_position(80 + 40 * i, 400)

    # Variaveis do boss
    boss = Sprite("img/reddit_boss.png", 18)
    boss.set_position(800, 600 - boss.height)
    tiros_boss = []
    contador_tiro = 0
    vida = 10
    cont = 0

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

            atual = boss.get_curr_frame()
            if atual == 17:
                if vida > 0:
                    contador_tiro += janela.delta_time()
                    if contador_tiro >= 0.75:
                        contador_tiro = 0
                        imagem = random.randint(1, 3)
                        angulo = random.randint(-25, 10)
                        if imagem == 1:
                            tiros_boss.append([GameImage("img/reddit_silver.png"), angulo])
                        elif imagem == 2:
                            tiros_boss.append([GameImage("img/reddit_gold.png"), angulo])
                        else:
                            tiros_boss.append([GameImage("img/reddit_platinum.png"), angulo])
                        tiros_boss[len(tiros_boss) - 1][0].set_position(795, 505)

            elif atual != 17 and cont >= 0.02:
                cont = 0
                boss.set_curr_frame(atual + 1)

            vel = 0
            if vida > 5:
                vel = 150
            else:
                vel = 250

            removidos = 0
            for i in range(len(tiros_boss)):
                i -= removidos
                tiros_boss[i][0].x -= vel * janela.delta_time()
                tiros_boss[i][0].y += tiros_boss[i][1] * janela.delta_time()
                if tiros_boss[i][0].x <= 0:
                    tiros_boss.pop(i)
                    removidos += 1

        if teclado.key_pressed("r"):
            fase, x, y = personagem.restart()
            return fase, x, y

        if jogador.x + jogador.height < 0:
            jogador.x = 0

        if vida > 0:
            if jogador.collided(boss):
                morreu = True

        fundo.draw()

        for i in range(len(plataforma)):
            plataforma[i].draw()

        for i in range(len(tiros_boss)):
            tiros_boss[i][0].draw()
            if tiros_boss[i][0].collided(jogador):
                morreu = True

        janela.draw_text("♥  " * vida, janela.width * 0.25, janela.height * 0.15, 60, (255, 0, 0), "Arial",True)

        for i in range(len(tiros)):
            tiros[i][0].draw()

            if tiros[i][0].collided_perfect(boss):
                vida -= 1
                tiros.pop(i)
                break

        if morreu:
            janela.draw_text("Game Over, Aperte R para Recomeçar", janela.width * 0.28, janela.height * 0.08, 35, (255, 255, 255))

        if vida > 0:
            boss.draw()
        else:
            return 9, 0, 0

        if not musica.is_playing():
            musica.play()

        jogador.draw()
        janela.update()



