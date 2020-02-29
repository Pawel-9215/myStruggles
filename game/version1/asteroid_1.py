import pyglet
import math

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

import resources, load
import physicalobject

game_window = pyglet.window.Window(800, 800, caption = "Meteora v0.01")

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score = 0", x=10, y=game_window.height-24, batch=main_batch)
level_label = pyglet.text.Label(text="Meteor Game", x=game_window.width//2, y=game_window.height-24, anchor_x='center', batch=main_batch)

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=400, batch=main_batch)
background = pyglet.sprite.Sprite(img=resources.background_image, x=0, y=0)

asteroids = load.asteroids(4, player_ship.position, main_batch)

game_objects = asteroids



@game_window.event
def on_draw():
   game_window.clear()

   background.draw()
   
   main_batch.draw()

def update(dt):
   for obj in game_objects:
      obj.update(dt)

if __name__ == '__main__':
   pyglet.clock.schedule_interval(update, 1/120.0)
   pyglet.app.run()
