#ПРАКТИКА
# Сумма списка через for
my_list = [1, 3, 4, 5, 14, 43]
sum = 0
for i in my_list:
    sum += i
print(sum)
# Сумма списка через while
sum = 0
l = len(my_list)
i = 0
while i < l:
    num = my_list[i]
    i += 1
    sum += num
print(sum)
# Написать программу которая выводит сама себя
with open("Practice_3.py", "r") as f:
    for line in f:
        print(line)
# Написать программу которая выводит сама себя задом наперед
b = []
with open("Practice_3.py", "r") as f:
    for line in f:
        b.append(line)
b = reversed(b)
print(''.join(b))
# Банкомат выдаетс сумму максимально возможными купюрами
my_list = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] #Вариант с двумя for
result_list = []
summ = 874
for _ in range(0, summ):
    for i in my_list:
        if summ >= i:
            result_list.append(i)
            summ -= i
            break
print(result_list)

my_list = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] #Вариант с одним for
result_list = []
summ = int(input('Введите нужную сумму: '))
index = 0
for _ in range(0, summ):
    if summ > 0:
        if summ >= my_list[index]:
            summ -= my_list[index]
            result_list.append(my_list[index])
        else:
            index += 1
print(result_list)


bank_value = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] #Вариант через while
result = int(input("Введи сумму: "))
number = 0
while result:
    if result >= bank_value[number]:
        result -= bank_value[number]
        print("Заберите деньги: " + str(bank_value[number]))
    else:
        number += 1
# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz, выводите.
numbers = []
with open('fizzbuzz_numbers.txt', 'r') as f:
    items = f.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(' ')])
for nums in numbers:
    for num in range(1, nums[2] + 1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            print('FB', end=' ')
        elif num % nums[0] == 0:
            print('F', end=' ')
        elif num % nums[1] == 0:
            print('B', end=' ')
        else:
            print(num, end=' ')
# Переделать вторую задачу так, чтобы результат писался в другой файл
numbers = []
results = []
with open('fizzbuzz_numbers.txt', 'r') as file:
    items = file.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(' ')])
for nums in numbers:
    for num in range(1, nums[2] + 1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            results.append("FB")
        elif num % nums[0] == 0:
            results.append("F")
        elif num % nums[1] == 0:
            results.append("B")
        else:
            results.append(num)
print(results)

with open('fizzbuzz_results.txt', 'w' ) as file:
    file.write(str(results))