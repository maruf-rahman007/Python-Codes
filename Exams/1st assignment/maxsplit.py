string_in = input()
answer = []
count = 0
substring = ""

for i in string_in:
    if i == 'L':
        count += 1
    else:
        count -= 1

    substring += i

    if count == 0:
        answer.append(substring)
        substring = ""

print(len(answer))
for substring in answer:
    print(substring)