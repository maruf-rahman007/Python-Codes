class Pen:
    name = 'Matadore'

    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

my_pen = Pen("Maruf",5,'Black')
print(my_pen.name,my_pen.price,my_pen.color)
