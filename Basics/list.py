numbers = [1,2,3,4,5,6,7,8,9]

# print(numbers[3],numbers[-6])

# print(numbers[1:6:1])
# print(numbers[6:1:-1])

numbers.append(10)
numbers.insert(0,0)#(index.value)

print(numbers)

if 0 in numbers:
    numbers.remove(0)
if 10 in numbers:
    numbers.remove(10)
print(numbers)
idx = numbers.index(7)
print(idx)