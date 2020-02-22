import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

label = pyglet.text.Label("Hello, world!!!!!", font_name="Arial", font_size = 16, x=window.width//2, y=window.height//2, anchor_x="center",anchor_y="center")

@window.event
def on_draw():
   window.clear()
   label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
   if button == mouse.LEFT:
    
      label.x = x
      label.y = y

pyglet.app.run()