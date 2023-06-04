class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!Woof!Woof!"

class Bulldog(Dog):
    def run(self):
        return f"{self.name} is running."

doggo = Bulldog("Tomy")

print(doggo.name)   # Output: Tomy
print(doggo.speak())   # Output: Woof!Woof!Woof!
print(doggo.run())   # Output: Tomy is running..
