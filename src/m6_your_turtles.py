"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and PUT_YOUR_NAME_HERE.
"""
########################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
big_yoshi = rg.SimpleTurtle('turtle')
big_yoshi.pen = rg.Pen('Green', 3)
big_yoshi.speed = 30
size = 200
for k in range(20):
    big_yoshi.draw_circle(size)
    size = size - 10


window.tracer(25)
gamer = rg.SimpleTurtle('turtle')
gamer.pen = rg.Pen('orange', 1)
gamer.backward(20)
for k in range(1000):
    gamer.right(100)
    gamer.forward(k)

window.close_on_mouse_click()

