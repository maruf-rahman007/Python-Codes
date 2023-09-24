class Product:
    def __init__(self,name,price,quantity) -> None:
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

class Store:
    def __init__(self) -> None:
        self.__product_price = {}
        self.__product_quantity = {}
        self.__profit = 0
    def add_product(self,name,price,quantity):
        product = Product(name,price,quantity)
        
        self.__product_price[product.product_name] = product.product_price
        self.__product_quantity[product.product_name] = product.product_quantity

    def show_products(self):
        print("All product's Price :",self.__product_price)
        print("All product's Quantity :",self.__product_quantity)
    
    def buy_product(self,name,quantity):
        if name in self.__product_price and self.__product_quantity[name] >= quantity:
            print("Product is Available ")
            self.__product_quantity[name] = self.__product_quantity[name] - quantity
            self.__profit = self.__profit + (5*self.__product_price[name]/100)
            print("Here is Your ",name)
        else:
            print("Product Unavailable ")
            
    def profit(self):
        print("Your Profit is ",self.__profit)
    
class Shop(Store):
    def __init__(self,name) -> None:
        self.shop_name = name
        super().__init__()
        
shop1 = Shop("Apple BD")
shop1.add_product("iPhone 13 pro max",999,10)
shop1.add_product("HP Pavilion",85000,1)

shop1.show_products()
shop1.buy_product("iPhone 13 pro max",3)
shop1.show_products()
shop1.profit()
