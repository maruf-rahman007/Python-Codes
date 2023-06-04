class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Khabar Khaiiii ! ")
    
class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

shakib = Crickter("Shakib Al Hasan",45,"5'9",68,"Bangladesh")
shakib.eat()