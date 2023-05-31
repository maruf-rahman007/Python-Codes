class Shop:

    def __init__(self,byer):
        self.byer = byer
        self.cart =[] #instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


user_1 = Shop('Maruf')
user_1.add_to_cart("Airpods")
user_1.add_to_cart("iPhone")

print(user_1.cart)

user_2 = Shop('Rafim')
user_2.add_to_cart("Mac")
user_2.add_to_cart("Bike")

print(user_2.cart)