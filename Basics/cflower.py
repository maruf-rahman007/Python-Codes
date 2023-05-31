name = input()
l= int(0)
u =int(0)
for char in name:
    if char.isupper():
        u+=1
    elif char.islower():
        l+=1

if u > l:
    print(name.upper())
else:
    print(name.lower())