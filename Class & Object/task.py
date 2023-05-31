class Calculator:

    def Addition(self,num1,num2):
        return int(num1)+int(num2)
    def Subtraction(self,num1,num2):
        return int(num1)-int(num2)
    def Multiplication(self,num1,num2):
        return int(num1)*int(num2)
    def Divition(self,num1,num2):
        return int(num1)/int(num2)
    
my_calculator = Calculator()

print("Addition of 2 num's = ",my_calculator.Addition(5,7))
print("Subtraction of 2 num's = ",my_calculator.Subtraction(5,7))
print("Multiplication of 2 num's = ",my_calculator.Multiplication(5,7))
print("Divition of 2 num's = ",my_calculator.Divition(5,7))