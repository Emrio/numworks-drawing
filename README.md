# numworks-drawing

> Easier drawing on Numworks calculators

[License][link-license] |
[Project on numworks][link-dl] |
[Github][link-repo] |
[Author][link-author] |
[Site][link-site]

This project contains some methods for drawing on Numworks. It uses the calculator's default `kandinsky` module.

### Usage example

```py
from drawing import *

# Makes the strokes red
Options.stroke(255, 0, 0)

# Makes a 100x50 rectangle with the top left corner at 100-100 coordinates
BasicShapes.rect(100, 100, 100, 50)
```

### Available methods

#### Options

`stroke([r: Number, g: Number, b: Number]): Number`
<br>Set a color for the strokes. If no argument specified, it returns the current color

#### BasicShapes

`point(x, y)`
<br>Draws a pixel with the selected color

`line(x1, y1, x2, y2)`
<br>Draws a line from the first coordinates to the other one.

`rect(x, y, w, h)`
<br>Draws a rectangle with no fill. The coordinates provided correspond to the top-left corner

`triangle(x1, y1, x2, y2, x3, y3)`
<br>Draws a triangle given three coordinates

`circle(x, y, r)`
<br>Draws a circle given the circle's centre and the radius

#### ComplexShapes

`setMode(mode: String)`
<br>Sets the drawing mode for complex shapes. Two modes available : `ABSOLUTE` and `RELATIVE`.<br>The `RELATIVE` mode moves a cursor that starts at `(0, 0)` when using `move()` and `line()`

`begin()`
<br>Begin complex shape

`end()`
<br>Ends a complex shape

`move(x, y)`
<br>Moves the current position to a given coordinate. If the mode is set to `RELATIVE`, the cursor is moved to the coordinates relative to the previous position.

`line(x, y)`
<br>Draws a line from current position to a given coordinate. This also moves the current coordinates.

### Limitations

This module doesn't currently support filling with colours

<!--
### FAQ
#### Why a module would be needed?
The built-in module in these calculators only allows for pixel-by-pixel drawing and implementing functions for creating shapes takes a lot of development time. This module allows you to easily implement your ideas on your calculator!

#### Why this module?
No other known projects implements all of this drawing tools in one publicly available module.
Moreover, the script has been greatly minified so it doesn't take a lot of space on your calculator. -->


<!-- The links! -->
[link-license]: https://github.com/TheEmrio/numworks-drawing/blob/master/LICENSE
[link-dl]: https://workshop.numworks.com/python/emrio/drawing
[link-repo]: https://github.com/TheEmrio/numworks-drawing
[link-author]: https://github.com/TheEmrio
[link-site]: https://emrio.fr
