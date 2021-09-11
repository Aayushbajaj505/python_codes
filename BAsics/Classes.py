class Point:
    # class level attribute same for all instances
    default_color = "red"

    # constructor in python
    def __init__(self, x, y):
        # whereas x,y are instance attributes and
        # take whatever value we provide them
        self.x = x
        self.y = y
        # by doing this we can fetch the
        # values of the parameters while using
        # this object

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


# point = Point(1, 2)
# print(point.default_color) # class level attribute
# point.draw()

    # to see the diffrence uncomment it

# this is a tedious process and
# we might have to repeat the base parameters again and again
# so insted we define a class method
# which has the intital values

point = Point.zero()
# also called a factory method

print(point.x)
point.draw()
