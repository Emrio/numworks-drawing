import kandinsky as ky
import math

HEIGHT = 320
WIDTH = 222


class Options:
  stroke_color = ky.color(0, 0, 0)
  
  @staticmethod
  def stroke(r = None, g = None, b = None):
    if not (r == g == b == None):
      Options.stroke_color = ky.color(r, g, b)
    
    return Options.stroke_color

class BasicShapes:
  
  @staticmethod
  def circle(cx, cy, r):
    
    for cur in range(r):
      BasicShapes.point(cx+cur, cy+int(math.sqrt(r**2 - cur**2)))
      BasicShapes.point(cx+cur, cy+int(-math.sqrt(r**2 - cur**2)))
      BasicShapes.point(cx-cur, cy+int(math.sqrt(r**2 - cur**2)))
      BasicShapes.point(cx-cur, cy+int(-math.sqrt(r**2 - cur**2)))
      
      BasicShapes.point(cx+int(math.sqrt(r**2 - cur**2)), cy+cur)
      BasicShapes.point(cx+int(math.sqrt(r**2 - cur**2)), cy-cur)
      BasicShapes.point(cx-int(math.sqrt(r**2 - cur**2)), cy+cur)
      BasicShapes.point(cx-int(math.sqrt(r**2 - cur**2)), cy-cur)
      
  @staticmethod
  def rect(x, y, w, h):
    BasicShapes.line(x, y, x+w, y)
    BasicShapes.line(x, y, x, y+h)
    BasicShapes.line(x, y+h, x+w, y+h)
    BasicShapes.line(x+w, y, x+w, y+h)
  
  @staticmethod
  def triangle(x1, y1, x2, y2, x3, y3):
    BasicShapes.line(x1, y1, x2, y2)
    BasicShapes.line(x2, y2, x3, y3)
    BasicShapes.line(x3, y3, x1, y1)
  
  @staticmethod
  def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    BasicShapes.line(x1, y1, x2, y2)
    BasicShapes.line(x2, y2, x3, y3)
    BasicShapes.line(x3, y3, x4, y4)
    BasicShapes.line(x4, y4, x1, y1)
  
  @staticmethod
  def point(x, y):
    ky.set_pixel(x, y, Options.stroke())
  
  @staticmethod
  def line(x1, y1, x2, y2):
    x_length = abs(x1 - x2)
    y_length = abs(y1 - y2)

    if x1 > x2:
      return BasicShapes.line(x2, y2, x1, y1)

    try:
      slope = (y2-y1) / (x2-x1)
    except ZeroDivisionError as e:
      # Can't calculate slope due to 0 division (vertical lines)
      x = x1
      for y in range(min(y1, y2), max(y1, y2)):
        ky.set_pixel(x, y, Options.stroke())
      return
    
    for x in range(x_length):
      y = round(slope * x)
      ky.set_pixel(x1+x, y1+y, Options.stroke())
      

class ComplexShapes:
  
  mode = "ABSOLUTE"
  
  # These are not used if mode is set to ABSOLUTE
  cur_x = None
  cur_y = None
  
  @staticmethod
  def setMode(MODE):
    if MODE.upper() == "ABSOLUTE":
      ComplexShapes.mode = "ABSOLUTE"
    elif MODE.upper() == "RELATIVE":
      ComplexShapes.mode = "RELATIVE"

  @staticmethod
  def begin():
    ComplexShapes.cur_x = 0
    ComplexShapes.cur_y = 0
  
  @staticmethod
  def move(x, y):
    if ComplexShapes.mode == "RELATIVE":
      ComplexShapes.cur_x += x
      ComplexShapes.cur_y += y
    else:
      ComplexShapes.cur_x = x
      ComplexShapes.cur_y = y

  @staticmethod
  def line(x, y):
    if ComplexShapes.mode == "RELATIVE":
      BasicShapes.line(ComplexShapes.cur_x, ComplexShapes.cur_y, ComplexShapes.cur_x+x, ComplexShapes.cur_y+y)
    else:
      BasicShapes.line(ComplexShapes.cur_x, ComplexShapes.cur_y, x, y)
      
    ComplexShapes.move(x, y)
  
  @staticmethod
  def end():
    ComplexShapes.cur_x = None
    ComplexShapes.cur_y = None
