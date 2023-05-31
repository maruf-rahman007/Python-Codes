# n=int(input())
# arr=list(map(int,input().split()))
# temp={}
# for num in arr:
#    if num not in temp:
#        temp[num]=1
#    else:
#        temp[num]+=1
# ans=0
# for num1,num2 in temp.items():
#    if num1>num2:
#        ans+=num2
#    else:
#        ans+=num2-num1
# print(ans)




n = int(input())
arr = list(map(int, input().split()))

temp = {}
for num in arr:
    temp[num] = temp.get(num, 0) + 1

ans = 0
for num, count in temp.items():
    if num > count:
        ans += count
    else:
        ans += count - num

print(ans)