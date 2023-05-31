# highest =  max(12,22,3,4,6,76,89,99)
# highest =  max([12,22,3,4,6,76,89,99])
arr = [12,22,3,4,6,76,89,99]
highest =  max(arr)
count = len(arr)
total = sum(arr)
print(highest,count,total)

def any(itr):
    global arr
    for arr in itr:
        if arr:
            return True 
    return False
print(any(76))