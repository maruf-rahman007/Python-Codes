def show_digits(arr):
    for num in arr:
        charr = num[::-1]
        print(' '.join(charr))

test_case = int(input())
arr = []
while test_case != 0:
    num = input()
    arr.append(num)
    test_case -= 1
show_digits(arr)