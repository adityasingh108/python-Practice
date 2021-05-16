from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(shape):
    def __init__(self):
        self.length = 8
        self.breadth = 10

    def print_area(self):
        return self.length * self.breadth

   
        





class Circle(shape):
    def __init__(self):
        self.radius = 7
        self.pi = 3.125

    def print_area(self):
        return self.radius*self.radius*self.pi*2


class Square(shape):
    def __init__(self):
        self.length = 5
        
    def print_area(self):
        return self.length * self.length

rect = Rectangle()
circle1 = Circle()
Square1= Square()


print(rect.print_area())
print(circle1.print_area())
print(Square1.print_area())
