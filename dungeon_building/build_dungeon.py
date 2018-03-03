import numpy as np
import cv2

def map_to_image(dungeon):
  dungeon = dungeon.astype(float)
  dungeon -= dungeon.min()
  dungeon *= (255 / dungeon.max())
  dungeon = cv2.resize(dungeon.astype(np.uint8), (400, 400), interpolation=cv2.INTER_NEAREST)
  cv2.imwrite('dungeon map.png', dungeon)


class Hallway():

  def __init__(self, start, angle):
    width = np.random.randint(5, 25)
    length = width * 5
    capped = True if np.random.rand() < .5 else False
    door_count = np.random.randint(1, 5)
    door_sides = [np.random.randint(0, 2) for _ in range(door_count)]


class Dungeon():

  def __init__(self, size):
    self.dungeon = np.zeros((size, size))


  def render(self):
    return self.dungeon



def generate(map_size=400):
  dungeon = Dungeon(map_size).render()
  return dungeon


if __name__ == '__main__':
  map_to_image(generate())




'''
hallways
  representation
    curved will require hi-resolution
    object oriented

  type
    curved
    straight
  doorways

rooms
  size
  shape
    rectangular
    circular
    random

stairs
  up or down
  type
    spiral
    split
    simple
'''
