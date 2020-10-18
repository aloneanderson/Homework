my_list = [1, 3, 4, 5, 14, 43]
sum = 0
for i in my_list:
    sum += i
print(sum)

sum = 0
l = len(my_list)
i = 0
while i < l:
    num = my_list[i]
    i += 1
    sum += num
print(sum)

with open("Practice_3.py", "r") as f:
    for line in f:
        print(line)
b = []
with open("Practice_3.py", "r") as f:
    for line in f:
        b.append(line)
b = reversed(b)
print(''.join(b))

