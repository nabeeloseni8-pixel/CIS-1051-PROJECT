# CIS-1051-PROJECT
Overview

I made Pocket Arcade, a small multi-game system using the micro: bit. Instead of just one, I built three different games into a single app and added a menu to switch between them. The goal was to make it feel like a mini handheld arcade. Since I was a kid, I've always liked handheld gaming consoles. When I was 7, I had a Game Boy and used to play Ultimate Spider-Man all the time. I remember bringing it everywhere until I had to give it to my younger cousin while we were on vacation in Africa. Even after that, I recently came back into handheld modding systems like the PlayStation Vita and the Nintendo 3DS, which made me even more interested in how games work and systems work. That's part of what made me choose this for my project.

Features
Startup screen displays."Pocket Acrade"
A menu system to choose between games
Press buttons A and B to switch games
Shake to start a game
Three Games
- Catch
- Reaction Time
- Dodge
Score or Time shown at the end of each game

I learned how to break my code into functions so it's more organized and easier to manage. I also learned how to use loops to keep things running and how to use variables to control which game is selected. I got better at using the accelerometer, and I learned how to use the LED grid to show movement like a player and falling objects

The hardest part was setting up multiple games in one program without messing everything up. At first, switching between games didn't work correctly; I had to fix how the game variable changed. Another issue was the motion controls. Double-tap didn't always work consistently, so I switched to using shake because it was more reliable.

I liked this project, which felt more like building something real instead of just answering questions or tasks. Seeing the games actually run on the micro made it more interesting. I would make some improvements If I had a little bit more time, like keeping track of high scores, adding better sound effects, and adding more games 

- Actual Code


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


