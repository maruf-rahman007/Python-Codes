def sum_betwee_two(x,y):
    a = int(x)
    b = int(y)
    sum = int(0)
    while a<b:
        a+=1
        if a % 2 == 1 and a<b:
            sum+=a
    print(sum)
test_case = int(input())
while test_case != 0:
    x,y = input().split()
    a = int(x)
    b = int(y)
    if a > b :
        temp = int(a)
        a = b
        b = temp
    sum_betwee_two(a,b)