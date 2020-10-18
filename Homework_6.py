# Задача найти самого успешного студента по среднему балу:
# 1 вариант:
names = dict(Ivan_Petrov=[2, 2, 3], Petya_Sidorov=[2, 4, 10], Rammstein_Till=[5, 12, 8], Green_Day=[9, 5, 5])
reiting = list()
for key, val in names.items():
    result = sum(names[key]) // len(names[key])
    reiting.append(result)
print(reiting)
print(names.values())

# 2 вариант:
marks_dict = {
    'surname1': [5, 3, 4],
    'surname2': [3, 3, 4],
    'surname3': [5, 5, 4]
}

def marks_calculations_var1(data):
    names = list(data.keys())
    marks = list(sum(m)/len(m) for m in data.values())
    return f'Min: {names[marks.index(min(marks))]}; Max: {names[marks.index(max(marks))]}'



