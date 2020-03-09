import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


player_image = pyglet.resource.image("ship_1.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_big_image = pyglet.resource.image("big_meteor.png")
asteroid_small_image = pyglet.resource.image("small_meteor.png")
background_image = pyglet.resource.image("background.png")
engine_flame = pyglet.resource.image("engine_flame.png")

engine_sound = pyglet.resource.media("engine.wav")

shot_sound = pyglet.resource.media("shot_1.wav", streaming=False)
expl_sound = pyglet.resource.media("expl_1.wav", streaming=False)

def center_image(image):
   #set ancor point to center
   image.anchor_x = image.width // 2
   image.anchor_y = image.height // 2


center_image(player_image)
center_image(engine_flame)
center_image(bullet_image)
center_image(asteroid_big_image)
center_image(asteroid_small_image)