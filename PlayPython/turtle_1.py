import turtle as t
t.pendown()
t.color("red")
t.forward(30)
t.color("red")
def square():
    t.forward(80)
    t.forward(80)
    t.right(80)
    t.forward(80)
    t.right(80)
    t.forward(80)
    t.right(100)
    t.forward(108)

square()
t.penup()
t.forward(100)
t.pendown()
square()
t.penup()
t.exitonclick()