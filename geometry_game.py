from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    # Inherits from the rectangle class

    def draw(self, canvas):
        canvas.penup()  # Lifts the pen, which won't draw anything.
        canvas.goto(self.point1.x, self.point1.y)  # go to a certain coordinate. X and Y
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)  # difference between the two x points
        canvas.left(90)  # Turn left 90 degrees.
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        # ^^ Draws a square on the canvas.



class GuiPoint(Point):

    def draw(self, canvas, size=5, color='green'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Create rectangle object with random ints
rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
                      Point(randint(10, 400), randint(10, 400)))


# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

my_turtle = turtle.Turtle()
rectangle.draw(canvas=my_turtle)
user_point.draw(canvas=my_turtle)
turtle.done()
