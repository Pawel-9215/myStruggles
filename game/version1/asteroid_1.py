import pyglet
import math

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

import resources, load
import physicalobject
import player

game_window = pyglet.window.Window(800, 800, caption = "Meteora v0.01")

main_batch = pyglet.graphics.Batch()
score = 0
lives = 3
score_label0 = pyglet.text.Label(text="Score: ", x=10, y=game_window.height-24, batch=main_batch)
score_label = pyglet.text.Label(text=str(score), x=10, y=game_window.height-44, batch=main_batch)

player_icons = load.player_lives(lives, batch=main_batch)

def update_score(score, label): 
   label.text = str(score)
   label.draw()


level_label = pyglet.text.Label(text="Meteor Game", x=game_window.width//2, y=game_window.height-24, anchor_x='center', batch=main_batch)

player_ship = player.Player(x=400, y=400, batch=main_batch)
background = pyglet.sprite.Sprite(img=resources.background_image, x=0, y=0)

asteroids = load.asteroids(4, player_ship.position, main_batch)

game_objects = asteroids + [player_ship]



@game_window.event
def on_draw():
   game_window.clear()

   background.draw()
   
   main_batch.draw()



def update(dt):
   
   to_add = []
   global score
   global lives
   global player_icons

   for i in range(len(game_objects)):
      for j in range(i+1, len(game_objects)):
         obj_1 = game_objects[i]
         obj_2 = game_objects[j]
         if not obj_1.dead and not obj_2.dead:
            if obj_1.collides_with(obj_2):
               obj_1.handle_collision_with(obj_2)
               obj_2.handle_collision_with(obj_1)

   for obj in game_objects:
      obj.update(dt)
      to_add.extend(obj.new_objects)
      obj.new_objects = []

   game_objects.extend(to_add)

   for to_remove in [obj for obj in game_objects if obj.dead]:
         
      if to_remove.is_bullet == False:
         score += 1
         update_score(score, score_label)

      if to_remove.is_player == True and lives > 0:
         lives -= 1
         to_remove.x=400
         to_remove.y=400
         to_remove.velocity_x = 0
         to_remove.velocity_y = 0
         to_remove.rotation = 0
         to_remove.dead = False
         player_icons = load.player_lives(lives, batch=main_batch)
         return
      to_remove.delete()
      game_objects.remove(to_remove)

   

if __name__ == '__main__':
   game_window.push_handlers(player_ship)
   game_window.push_handlers(player_ship.key_handler)
   pyglet.clock.schedule_interval(update, 1/120.0)
   pyglet.app.run()
