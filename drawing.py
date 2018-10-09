import kandinsky as k, math
HEIGHT=320;WIDTH=222
class Options:
 str=k.color(0,0,0)
 def stroke(r=None,g=None,b=None):
  if not(r==g==b==None):
   Options.str=k.color(r,g,b)
  return Options.str
class BasicShapes:
 def circle(cx,cy,r):
  for cur in range(r):
   a=int(math.sqrt(r**2-cur**2));p=BasicShapes.point;p(cx+cur,cy+a)(cx+cur,cy-a)(cx-cur,cy+a)(cx-cur,cy-a)(cx+a,cy+cur)(cx+a,cy-cur)(cx-a,cy+cur)(cx-a,cy-cur)
 def rect(x,y,w,h):
  l=BasicShapes.line;l(x,y,x+w,y)(x,y,x,y+h)(x,y+h,x+w,y+h)(x+w,y,x+w,y+h)
 def triangle(x1,y1,x2,y2,x3,y3):
  l=BasicShapes.line;l(x1,y1,x2,y2)(x2,y2,x3,y3)(x3,y3,x1,y1)
 def point(x,y):
  k.set_pixel(x,y,Options.stroke());return BasicShapes.point
 def line(x1,y1,x2,y2):
  b=BasicShapes
  if x1>x2:
   b.line(x2,y2,x1,y1);return b.line
  try:
   slope=(y2-y1)/(x2-x1)
  except ZeroDivisionError as e:
   for y in range(min(y1,y2),max(y1,y2)):
    k.set_pixel(x1,y,Options.stroke())
   return b.line
  for x in range(abs(x1-x2)):
   k.set_pixel(x1+x,y1+round(slope*x),Options.stroke())
  return b.line
class ComplexShapes:
 mode="ABSOLUTE";cur_x=cur_y=None
 def setMode(MODE):
  ComplexShapes.mode="RELATIVE"if MODE.upper()=="RELATIVE"else"ABSOLUTE"
 def begin():
  c=ComplexShapes
  c.cur_x=c.cur_y=0
 def move(x,y):
  c=ComplexShapes
  c.cur_x=c.cur_x+x if c.mode=="RELATIVE"else x;c.cur_y=c.cur_y+y if c.mode=="RELATIVE"else y
 def line(x,y):
  c=ComplexShapes
  if c.mode=="RELATIVE":
   BasicShapes.line(c.cur_x,c.cur_y,c.cur_x+x,c.cur_y+y)
  else:
   BasicShapes.line(c.cur_x,c.cur_y,x,y)
  c.move(x,y)
 def end():
  c=ComplexShapes
  c.cur_x=c.cur_y=None
