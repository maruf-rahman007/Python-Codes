# class Calculator:
#    def calculate(self,a,b):
#        def add():
#            return a+b
#        def sub():
#            return a-b
#        def mul():
#            return a*b
#        def div():
#            if b==0:
#                return "Cannot divide by zero"
#            else:
#                return a/b
#        def reminder():
#            return a % b
#        return add(),sub(),mul(),div(),reminder()
# value_calculate=Calculator()
# print(value_calculate.calculate(10,20))

# class StringUtils:
#     @staticmethod
#     def is_palindrome(word):
#         def clean_string(string):
#             return ''.join(char.lower() for char in string if char.isalnum())

#         cleaned_word = clean_string(word)
#         return cleaned_word == cleaned_word[::-1]

# word = input("Enter a word: ")

# if StringUtils.is_palindrome(word):
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2


