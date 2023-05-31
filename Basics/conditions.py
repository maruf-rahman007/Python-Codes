variable = int(input())

while variable <= 10:
    if variable % 2 == 0:
        print(variable)
    variable += 1

arr = [1,2,3,4,5]

for nums in arr:
    if nums % 2 != 0:
        print(nums)
    