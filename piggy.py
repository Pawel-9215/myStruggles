import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()

label = pyglet.text.Label("Hello, world!!!!!", font_name="Arial", font_size = 16, x=window.width//2, y=window.height//2, anchor_x="center",anchor_y="center")
w = 12
@window.event
def on_draw():
   global w

   window.clear()
   label.draw()
   some_points(w)
   

def some_points(ab):

   pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
   ('v2i', (10, ab, 30, 35))
   )


@window.event
def on_mouse_press(x, y, button, modifiers):
   global w
   if button == mouse.LEFT:
      print("x = ", x, "y = ", y)
      label.x = x
      label.y = y
      w += 2

pyglet.app.run()