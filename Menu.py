# MENU
from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sound import *
from PPlay.keyboard import *
import personagem
import tutorial
import tutorial2
import fase3_b
import fase3_a
import fase3_boss
import reddit_1
import reddit_2
import reddit_3
import reddit_boss

menu = Window(1000, 700)
menu.set_title("I Wanna Know the Internet")

rato = Mouse()
teclado = Keyboard()

background = GameImage("img/menu.png")
start = GameImage("img/start-menu-botao.png")
sair = GameImage("img/exit-menu-botao.png")
load = GameImage("img/load-botao.png")
load_claro = GameImage("img/load-botao-claro.png")

start.x = menu.width / 2 - start.width / 2
start.y = menu.height * 0.6
load.x = menu.width / 2 - load.width / 2
load.y = menu.height * 0.75
load_claro.x = menu.width / 2 - load.width / 2
load_claro.y = menu.height * 0.75
sair.x = menu.width / 2 - sair.width / 2
sair.y = menu.height * 0.9

fase = -1
ini_x = 0
ini_y = 0

salvo = False

musica = Sound("audio/soundtrack-game.ogg")
musica.play()

while True:

    background.draw()
    load_claro.draw()
    if salvo:
        load.draw()
    start.draw()
    sair.draw()

    try:
        personagem.restart()
        salvo = True
    except:
        salvo = False

    if rato.is_over_object(start) and rato.is_button_pressed(BUTTON_LEFT):
        fase = 0
        ini_x = 0
        ini_y = 369
        personagem.salvar(0, 0, 369)

    if rato.is_over_object(load) and rato.is_button_pressed(BUTTON_LEFT) and salvo:
        fase, ini_x, ini_y = personagem.restart()

    if fase == 0:
        fase, ini_x, ini_y = tutorial.fase_0(ini_x, ini_y, musica)

    elif fase == 1:
        fase, ini_x, ini_y = tutorial2.fase_1(ini_x, ini_y, musica)

    elif fase == 2:
        fase, ini_x, ini_y = fase3_a.fase_youtube_1(ini_x, ini_y, musica)

    elif fase == 3:
        fase, ini_x, ini_y = fase3_b.fase_youtube_2(ini_x, ini_y, musica)

    elif fase == 4:
        fase, ini_x, ini_y = fase3_boss.fase_youtube_boss(ini_x, ini_y, musica)

    elif fase == 5:
        fase, ini_x, ini_y = reddit_1.reddit_1(ini_x, ini_y, musica)

    elif fase == 6:
        fase, ini_x, ini_y = reddit_2.reddit_2(ini_x, ini_y, musica)

    elif fase == 7:
        fase, ini_x, ini_y = reddit_3.reddit_3(ini_x, ini_y, musica)

    elif fase == 8:
        fase, ini_x, ini_y = reddit_boss.reddit_boss(ini_x, ini_y, musica)

    elif fase == 9:
        background = GameImage("img/Parabens.png")
        background.draw()

        if teclado.key_pressed("ESC"):
            exit(1)

        menu.update()

    elif rato.is_over_object(sair) and rato.is_button_pressed(BUTTON_LEFT):
        exit(1)

    if not musica.is_playing():
        musica.play()

    menu.update()
