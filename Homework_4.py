numbers = []
results_list = []
with open('fizzbuzz_numbers.txt', 'r') as file:
    items = file.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(' ')])
for nums in numbers:
    for num in range(1, nums[2] + 1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            results_list.append(list("FizzBuzz"))
        elif num % nums[0] == 0:
            results_list.append(list("Fizz"))
        elif num % nums[1] == 0:
            results_list.append(list("Buzz"))
        else:
            results_list.append(num)

with open('fizzbuzz_results_new.txt', 'w' ) as file:
    file.write(str(results_list))