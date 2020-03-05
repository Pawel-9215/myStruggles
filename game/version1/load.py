import pyglet
import random
from random import randint
import math
import resources
import physicalobject
import util
import asteroid

def asteroids(num_asteroids, player_position, batch=None):
   asteroids = []
   #asteroid_types = [resources.asteroid_big_image, resources.asteroid_small_image]
   for i in range(num_asteroids):
      asteroid_x, asteroid_y = player_position
      while util.distance((asteroid_x, asteroid_y), player_position) < 100:
         asteroid_x = randint(0,800)
         asteroid_y = randint(0,800)
      #asteroid_size = randint(0,1)
      new_asteroid = asteroid.Asteroid(x = asteroid_x, y = asteroid_y, batch=batch)
      new_asteroid.rotation = randint(0,360)
      new_asteroid.velocity_x = random.random()*40
      new_asteroid.velocity_y = random.random()*40
      asteroids.append(new_asteroid)
   return asteroids



def player_lives(num_lives, batch=None):
   player_lives = []
   for i in range(num_lives):
      new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=785-i*30, y=785, batch=batch)
      new_sprite.scale = 0.5
      player_lives.append(new_sprite)
   return player_lives
