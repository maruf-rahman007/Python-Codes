import math

class MATH:
   
   def __init__(self, a, b, c):
       self.a = a
       self.b = b
       self.c = c

   def sum(self):
       result = self.a + self.b + self.c
       return f'Sum of {self.a}, {self.b}, and {self.c} is--> {result}'

   def factorial(self):
       result = math.factorial(self.b)
       return f'Factorial of {self.b} is--> {result}'

num = MATH(4, 6, 8)
print(num.sum())
print(num.factorial())

"""
        The Output : 
            Sum of 4, 6, and 8 is--> 18
            Factorial of 6 is--> 720
"""