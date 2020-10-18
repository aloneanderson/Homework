# Проверка четности числа
x = int(input("Vvedi 4islo: "))
if x % 2 == 0:
   print('4etnoe 4islo')
else:
   print('NE4etnoe 4islo')

# Проверить, является ли число нечетным, делится ли на три и на пять одновременно, но так, чтобы не делиться на 10
x = int(input("Vvedi 4islo: "))
if x % 2 != 0:
   print('NE4etnoe 4islo')
else:
   print('4etnoe 4islo')
if x % 3 == 0 and x % 5 == 0 and x % 10 != 0:
   print('Delitsa na 3 i 5 , no ne delitsa na 10')
else:
   print('Ne del1ista na 3 i na 5 odnovremenno')

# Ввести число, вывести все его делители
n = int(input('Vvedi 4islo: '))
i = 1
while i <= n:
   if n % i == 0: print(i)
   i += 1
# Ввести число, вывести его разряды
my_number = input("Vvedite 4islo: ")
for i in (my_number):
    print (i)
# Придумать свои собственные примеры на альтернативные варианты if и активное использование булевой алгебры
# Число от одного до тысячи
x = int(input("Vvedite 4islo: "))
if 1 < x <= 1000:
   print("Eto 4islo ot 1 do 1000")
else:
   print("Net")
# Свой вариант проверки четности и делится ли число на 3, 5, 10
x = int(input("Vvedi 4islo: "))
if x % 2 != 0:
   print('NE4etnoe 4islo')
else:
   print('4etnoe 4islo')
if x % 3 == 0 and x % 5 == 0:
   print('Delitsa na 3 i na 5 odnovremenno')
elif x % 3 == 0:
   print('Delitsa tolko na 3')
elif x % 5 == 0:
   print('Delitsa tolko na 5')
else:
   print('Ne delista na 3 i na 5 odnovremenno')
if x % 10 != 0:
   print('Ne delitsa na 10')
else:
   print('Delitsa na 10')
#Name
name = input("Type name: ")
res = "Привет " +name
print (res)

# Задача Fizz Buzz
fizz = int(input("Vvedi Fizz: "))
buzz = int(input("Vvedi Buzz: "))
third = int(input("Vvedite num: "))
for i in range(1, third):
   if i % fizz == 0 and i % buzz == 0:
       print("FB")
   elif i % fizz == 0:
       print("F")
   elif i % buzz == 0:
       print("B")
   else:
       print(i)

