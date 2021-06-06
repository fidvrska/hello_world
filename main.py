import pgzrun
WIDTH = 500
HEIGHT = 500

player = Rect((250, 250), (100, 100))


def draw():
    screen.fill('black')
    screen.draw.filled_rect(player, 'red')


def update():
    if keyboard.right and player.x < 400:
        player.x += 10
    if keyboard.left and player.x > 0:
        player.x -= 10
    if keyboard.up:
        player.y -= 10
    if keyboard.down:
        player.y += 10

#
# def on_key_down(key):
#     if key == keyboard.RIGHT:
#         print('!!')
#         player.x += 10

pgzrun.go()
