def freq(n,m,array):
   
   frequency = [0]*(m+1)
   for i in array:
       frequency[i] += 1
   return frequency[1:]
  
n,m=map(int,input().split())
array=list(map(int,input().split()))

for size in freq(n,m,array):
   print(size)
