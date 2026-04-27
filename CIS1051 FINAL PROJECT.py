from microbit import *
import random
import music

game = 0
games = ["CATCH", "REACT", "DODGE"]

def startup():
    display.scroll("POCKET")
    display.show(Image.HAPPY)
    sleep(500)
    display.scroll("ARCADE")
    music.play(music.POWER_UP)
    display.clear()

def show_menu():
    display.scroll(games[game])
    display.show(str(game + 1))

def catcher_game():
    player_x = 2
    ball_x = random.randint(0, 4)
    ball_y = 0
    score = 0

    start_time = running_time()

    while running_time() - start_time < 20000:
        display.clear()

        if button_a.was_pressed() and player_x > 0:
            player_x = player_x - 1

        if button_b.was_pressed() and player_x < 4:
            player_x = player_x + 1

        display.set_pixel(ball_x, ball_y, 9)
        display.set_pixel(player_x, 4, 9)

        sleep(400)

        ball_y = ball_y + 1

        if ball_y == 4:
            if ball_x == player_x:
                score = score + 1
                music.pitch(700, 100)
            else:
                music.pitch(200, 100)

            ball_x = random.randint(0, 4)
            ball_y = 0

    display.scroll("SCORE")
    display.scroll(str(score))

def reaction_game():
    display.scroll("WAIT")
    sleep(random.randint(2000, 5000))

    display.show(Image.SQUARE)
    start = running_time()

    while True:
        if button_a.was_pressed() or button_b.was_pressed():
            reaction_time = running_time() - start
            display.scroll(str(reaction_time))
            display.scroll("MS")
            break

def dodge_game():
    player_x = 2
    enemy_x = random.randint(0, 4)
    enemy_y = 0
    score = 0

    while True:
        display.clear()

        if button_a.was_pressed() and player_x > 0:
            player_x = player_x - 1

        if button_b.was_pressed() and player_x < 4:
            player_x = player_x + 1

        display.set_pixel(enemy_x, enemy_y, 9)
        display.set_pixel(player_x, 4, 9)

        sleep(400)

        enemy_y = enemy_y + 1

        if enemy_y == 4:
            if enemy_x == player_x:
                display.show(Image.SKULL)
                music.play(music.WAWAWAWAA)
                sleep(1000)
                display.scroll("SCORE")
                display.scroll(str(score))
                break
            else:
                score = score + 1
                enemy_x = random.randint(0, 4)
                enemy_y = 0


def play_game():
    if game == 0:
        catcher_game()

    if game == 1:
        reaction_game()

    if game == 2:
        dodge_game()

startup()
show_menu()

while True:
    if button_a.was_pressed():
        game = game - 1

        if game < 0:
            game = 2

        show_menu()

    if button_b.was_pressed():
        game = game + 1

        if game > 2:
            game = 0

        show_menu()

    if accelerometer.was_gesture("shake"):
        display.scroll("START")
        play_game()
        display.scroll("MENU")
        show_menu()