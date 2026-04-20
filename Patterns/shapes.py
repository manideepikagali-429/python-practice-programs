import math 
class Shape: 
    def calculate_area(self): 
    pass 
    def calculate_perimeter(self): 
    pass 
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
    def calculate_area(self): 
        return math.pi * self.radius ** 2 
    def calculate_perimeter(self): 
        return 2 * math.pi * self.radius 
 class Triangle(Shape): 
    def __init__(self, side1, side2, side3): 
        self.side1 = side1 
        self.side2 = side2 
        self.side3 = side3 
    def calculate_area(self): 
        s = (self.side1 + self.side2 + self.side3) / 2 
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)) 
    def calculate_perimeter(self): 
        return self.side1 + self.side2 + self.side3 
class Square(Shape): 
    def __init__(self, side): 
        self.side = side 
    def calculate_area(self): 
        return self.side ** 2 
    def calculate_perimeter(self): 
        return 4 * self.side 
circle = Circle(int(input())) 
print(f"Circle Area = {circle.calculate_area()}") 
print(f"Circle Perimeter = {circle.calculate_perimeter()}") 
triangle = Triangle(int(input()), int(input()), int(input())) 
print(f"Triangle Area = {triangle.calculate_area()}") 
print(f"Triangle Perimeter = {triangle.calculate_perimeter()}") 
square = Square(int(input())) 
print(f"Square Area = {square.calculate_area()}") 
print(f"Square Perimeter = {square.calculate_perimeter()}")