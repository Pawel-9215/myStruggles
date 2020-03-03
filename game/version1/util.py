import pyglet, math

def distance(point_1=(0,0), point_2=(0,0)): #return distance between two points
   return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

