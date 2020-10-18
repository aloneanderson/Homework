# ПРАКТИКА
# Привести к верхнему и нижнему регистру:
def to_upperCase(word):
    return print(word.upper())


to_upperCase('hello my friend')


def to_lowerCase(word):
    return print(word.lower())


to_lowerCase('ЛЮБОЕ СЛОВО')

# Применить функции с помощью map к списку строк:
my_list = ['just', 'a', 'random', 'words']
list(map(to_upperCase, my_list))
list(map(to_lowerCase, my_list))


# Возвести в квадрат:
def square(i):
    return print(i * i)


square(8)

# Возвести в квадрат простые числа с помощью map:
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 44, 768, 242, 4]
list(map(square, my_numbers))

# Посчитать частоту встретившихся слов в файле через функиции и map(без цикла):
with open('MyHappyEnding_lyrics.txt', 'r') as file:
    r = file.read()


def same_word(word):
    if word in total_words:
        total_words[word] += 1
    else:
        total_words[word] = 1


total_words = dict()
list(map(lambda x: same_word(''.join(filter(str.isalpha, x.lower()))), r.split()))
print(total_words)

# Fizz_buzz с функицями и map
numbers = []
with open('fizzbuzz_numbers.txt', 'r') as file:
    items = file.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(' ')])
def fizz_buzz(arr):
    results = ""
    for x in range(1, arr[-1] + 1):
        if not x % arr[0] and not x % arr[1]:
            results += 'FB'
        elif not x % arr[0]:
            results += 'F'
        elif not x % arr[1]:
            results += 'B'
        else:
            results += str(x)
    return results


def fizz_buzz_lists():
    return list(map(fizz_buzz, numbers))

# Пример ZIP
a = [5, 6, 7, 8]
b = [100, 400, 600, 1000]
words = ['Hello', 'my', 'dear', 'friend']
res = list(zip(a, b, words))
print(res)

for x1, x2, x3 in res:
    print(x1, x2, x3)
result = zip(a,b, words)
coll1,coll2,coll3 = zip(*result)
print(coll1,coll2,coll3)
