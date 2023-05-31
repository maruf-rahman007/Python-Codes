N = int(input())
A = list(map(int, input().split()))

maxOperations = float('inf')

for num in A:
    operations = 0
    while num % 2 == 0:
        num //= 2
        operations += 1
    maxOperations = min(maxOperations, operations)

print(maxOperations)