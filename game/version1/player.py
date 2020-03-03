import pyglet
import physicalobject
import resources
import math
import bullet
from pyglet.window import key


class Player(physicalobject.PhysicalObject):

   def __init__(self, *args, **kwargs):
      super().__init__(img=resources.player_image, *args, **kwargs)
      self.thrust = 300.0
      self.rotation_speed = 200.0
      self.key_handler = key.KeyStateHandler()
      self.keys = dict(left=False, right=False, up=False)
      self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_flame, *args, **kwargs)
      self.engine_sprite.visible = False
      self.bullet_speed = 700.0
      self.reacts_to_bullets = False
   def delete(self):
      self.engine_sprite.delete()
      super(Player, self).delete()

   def fire(self):
      angle_radians = -math.radians(self.rotation-90)
      ship_radius = self.image.width/2
      bullet_x = self.x + math.cos(angle_radians) * ship_radius
      bullet_y = self.y + math.sin(angle_radians) * ship_radius
      
      new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
      
      bullet_vx = (self.velocity_x + math.cos(angle_radians)*self.bullet_speed)
      bullet_vy = (self.velocity_y + math.sin(angle_radians)*self.bullet_speed)

      new_bullet.rotation = self.rotation
      new_bullet.velocity_x = bullet_vx
      new_bullet.velocity_y = bullet_vy
      
      self.new_objects.append(new_bullet)
   
   def on_key_press(self, symbol, mods):
      if symbol == key.SPACE:
         self.fire()

   

   def update(self, dt):
      super(Player, self).update(dt)
      #print(self.rotation)
      if self.key_handler[key.LEFT]:
         self.rotation -= self.rotation_speed*dt
      if self.key_handler[key.RIGHT]:
         self.rotation += self.rotation_speed*dt

      if self.key_handler[key.UP]:
         self.engine_sprite.visible = True
         angle_radians = -math.radians(self.rotation-90)
         force_x = math.cos(angle_radians) * self.thrust * dt
         force_y = math.sin(angle_radians) * self.thrust * dt
         self.velocity_x += force_x
         self.velocity_y += force_y

         self.engine_sprite.rotation = self.rotation
         self.engine_sprite.x = self.x
         self.engine_sprite.y = self.y
         

      else:
         self.engine_sprite.visible = False
