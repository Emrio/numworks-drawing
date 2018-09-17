#This script is minified. Check emrio.fr/projects for the source code
import kandinsky as ky, math
HEIGHT=320;WIDTH=222
class Options:
  stroke_color=ky.color(0,0,0)
  def stroke(r=None,g=None,b=None):
    if not(r==g==b==None):
      Options.stroke_color=ky.color(r,g,b)
    return Options.stroke_color
class BasicShapes:
  def circle(cx,cy,r):
    for cur in range(r):
      a=int(math.sqrt(r**2-cur**2))
      BasicShapes.point(cx+cur,cy+a)
      BasicShapes.point(cx+cur,cy-a)
      BasicShapes.point(cx-cur,cy+a)
      BasicShapes.point(cx-cur,cy-a)
      BasicShapes.point(cx+a,cy+cur)
      BasicShapes.point(cx+a,cy-cur)
      BasicShapes.point(cx-a,cy+cur)
      BasicShapes.point(cx-a,cy-cur)
  def rect(x,y,w,h):
    BasicShapes.line(x,y,x+w,y)
    BasicShapes.line(x,y,x,y+h)
    BasicShapes.line(x,y+h,x+w,y+h)
    BasicShapes.line(x+w,y,x+w,y+h)
  def triangle(x1,y1,x2,y2,x3,y3):
    BasicShapes.line(x1,y1,x2,y2)
    BasicShapes.line(x2,y2,x3,y3)
    BasicShapes.line(x3,y3,x1,y1)
  def quad(x1,y1,x2,y2,x3,y3,x4,y4):
    BasicShapes.line(x1,y1,x2,y2)
    BasicShapes.line(x2,y2,x3,y3)
    BasicShapes.line(x3,y3,x4,y4)
    BasicShapes.line(x4,y4,x1,y1)
  def point(x,y):
    ky.set_pixel(x,y,Options.stroke())  
  def line(x1,y1,x2,y2):
    if x1>x2:
      return BasicShapes.line(x2,y2,x1,y1)
    try:
      slope=(y2-y1)/(x2-x1)
    except ZeroDivisionError as e:
      for y in range(min(y1,y2),max(y1,y2)):
        ky.set_pixel(x1,y,Options.stroke())
      return
    for x in range(abs(x1-x2)):
      ky.set_pixel(x1+x,y1+round(slope*x),Options.stroke())
class ComplexShapes:
  mode="ABSOLUTE";cur_x=cur_y=None
  def setMode(MODE):
    ComplexShapes.mode="RELATIVE"if MODE.upper()=="RELATIVE"else"ABSOLUTE"
  def begin():
    ComplexShapes.cur_x=ComplexShapes.cur_y=0
  def move(x,y):
    ComplexShapes.cur_x=ComplexShapes.cur_x+x if ComplexShapes.mode=="RELATIVE"else x
    ComplexShapes.cur_y=ComplexShapes.cur_y+y if ComplexShapes.mode=="RELATIVE"else y
  def line(x,y):
    if ComplexShapes.mode=="RELATIVE":
      BasicShapes.line(ComplexShapes.cur_x,ComplexShapes.cur_y,ComplexShapes.cur_x+x,ComplexShapes.cur_y+y)
    else:
      BasicShapes.line(ComplexShapes.cur_x,ComplexShapes.cur_y,x,y)
    ComplexShapes.move(x,y)
  def end():
    ComplexShapes.cur_x=ComplexShapes.cur_y=None
