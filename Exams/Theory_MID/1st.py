# class Circle:
#     pi = 3.1416

#     def __init__(self, radius):
#         self.radius = radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

#     def calculate_area(self):
#         return self.pi * self.radius ** 2

# circle1 = Circle.from_diameter(15)
# print("First Circle Area:", circle1.calculate_area())  # Output: First Circle Area: 176.715

# circle2 = Circle.from_diameter(8)
# print("Second Circle Area:", circle2.calculate_area())  # Output: Second Circle Area: 50.2656

class MathUtils:
    @staticmethod
    def add_numbers(x, y):
        return x + y

    @staticmethod
    def multiply_numbers(x, y):
        return x * y

result1 = MathUtils.add_numbers(99, 101)
print("Result After Addition :", result1)  # Output: Result After Addition : 200

result2 = MathUtils.multiply_numbers(25, 4)
print("Result After Multiplication :", result2)  # Output: Result After Multiplication : 100
