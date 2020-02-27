import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

import resources

game_window = pyglet.window.Window(800, 800, caption = "Meteora v0.01")

score_label = pyglet.text.Label(text="Score = 0", x=10, y=game_window.height-24)
level_label = pyglet.text.Label(text="Meteor Game", x=game_window.width//2, y=game_window.height//2, anchor_x='center')

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=400)
background = pyglet.sprite.Sprite(img=resources.background_image, x=0, y=0)

@game_window.event
def on_draw():
   game_window.clear()

   level_label.draw()
   score_label.draw()
   background.draw()
   player_ship.draw()



if __name__ == '__main__':
   pyglet.app.run()