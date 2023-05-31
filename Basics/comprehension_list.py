numbers = [45,77,22,54,23,68]
odd = []
for num in numbers:
    if num % 2 == 1:
         odd.append(num)
print(odd)

odd_num = [num for num in numbers if num % 2 == 1]
print(odd_num)