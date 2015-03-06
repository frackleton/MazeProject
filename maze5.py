""" A rotational, computational maze created collaboratively.

@authors: Mackenzie, Jaime, Anisha

"""

import pygame 



class Maze():
  """ Main maze class
  """
  def __init__(self):
    """ Initialize the rotating mazae game.  Use Maze.run to
        start the game """
    width = 500   #we can change later if needed
    height = 500  #we can change later if needed
    self.model = MazeModel(width, height)
    self.view = MazeView(self.model, width, height)
    self.controller = MazeController(self.model)

  def run(self):
    """ the main runloop... loop until death """
    # WE TOOK OUT THE WHILE LOOP FOR TESTING PURPOSES, REMEMBER TO ADD IT AGAIN
    while not(self.model.is_dead()):
      self.view.draw()
      self.controller.process_events()
      self.model.update()


class MazeController():
  """Keyboard Posiitons"""
  def __init__(self, model):
    self.model = model
    self.down_pressed = False
    self.up_pressed = False
    self.right_pressed = False
    self.left_pressed = False

  

  def process_events(self):
    """ process keyboard events.  This must be called periodically
        in order for the controller to have any effect on the game """
    pygame.event.pump() #ASK NINJAS
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        self.down_pressed = True
        #call function here to translate 1 unit down
    elif pygame.key.get_pressed()[pygame.K_UP]:
        self.up_pressed = True
        #call function here to translate 1 unit up
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        self.left_pressed = True
        #call function here to rotate 90 degrees left
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        self.right_pressed = True 
        #call function here to rotate 90 degrees right
    else:
      self.right_pressed = False
      self.left_pressed  = False
      self.up_pressed  = False
      self.down_pressed = False
  

class MazeModel():
  """represents the game state of our maze"""
  
  def __init__(self, width, height):
    """ Initialize the flappy model """
    self.width = width
    self.height = height
    self.board = Board(width, height)


  def get_drawables(self):
    """ Return a list of DrawableSurfaces for the model """
    return self.board.get_drawables()

  def update(self):
    """ Updates the model and its constituent parts """
    pass

  def is_dead(self):
    return False
  

class MazeView():
  def __init__(self, model, width, height):
    """ Initialize the view for the maze.  The input model
        is necessary to find the position of relevant objects
        to draw. """
    pygame.init()
    # to retrieve width and height use screen.get_size()
    self.screen = pygame.display.set_mode((width, height))
    # this is used for figuring out where to draw stuff
    self.model = model
    self.width = width
    self.height = height
  

  def draw(self):
    """ Redraw the full game window """
    self.screen.fill((0,51,102)) # COLOR
    #rectt = pygame.Rect(0, 0, 50, 60)
    #color = pygame.Color(150, 105, 0)
    #pygame.draw.rect(self.screen, color, rectt)

    tuple_rects = self.model.board.get_rects()
    for t in tuple_rects:
      pygame.draw.rect(self.screen, t[1], t[0])
    pygame.display.update()

class Board():
  """ Describes the board maze """
  def __init__(self, width, height):
    self.width = width
    self.heigth = height
    self.box_width = 50
    self.background = pygame.Surface((int(width), int(height)))
    self.fixed_point = FixedPoint(width/2.0, height/2.0)
    self.matrix = [[0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0]]

  def get_rects(self):
    # rects is a dictionary of tuples, where the keys are
    # rect objects and the values are the colors of the rects
    rects = []
    for r in range(len(self.matrix)): #loop through rows
      for c in range(len(self.matrix[r])): # loop through columns
        # get image depending on what number is in the matrix
        if self.matrix[r][c] == 0:
          color = pygame.Color(0, 0, 0)
        elif self.matrix[r][c] == 1:
          color = pygame.Color(255, 150, 125)
        else:
          color = pygame.Color(150, 125, 0)
        # get the absolute positions for the point at which to draw the squares
        width = self.box_width
        left = (width * c)
        top = (width * r)
        rectt = pygame.Rect(left, top, width, width)
        rects.append((rectt, color))
    return rects

class FixedPoint():
  """A class that keeps the one main point of the maze/board"""
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = 2
  
  def get_x(self):
    """ Get the center of the point """
    return self.x
    
  def get_y(self):
    return self.y
    
  def get_radius(self):
    return self.radius
  
  
class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """
    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect

if __name__ == '__main__':
    maze = Maze()
    maze.run()
