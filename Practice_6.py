import math

# ПРАКТИКА / Задача курьер:
entrance = 1
num_flat = int(input('Номер квартиры?: '))
floors = int(input('Количество этажей?: '))
flats = int(input('Количество квартир на этаже?: '))
entrances = int(input('Количество подъездов?: '))


def check_flors(num_flat, floors, flats):
    if num_flat < floors * flats * entrances:
        entrance = 1
        while num_flat > floors * flats:
            num_flat -= floors * flats
            entrance += 1
        our_floor = math.ceil(num_flat / flats)
        return print('Зайди в ' + str(entrance) + ' подъезд, на ' + str(our_floor) + ' этаж')
    else:
        return print('Не номер квартиры')


check_flors(num_flat, floors, flats)


# Задача БРИЛЛИАНТ
def brilliant(num):
    if num > 0 and num % 2 != 0:
        for i in range(1, num + 1, 2):
            space = int((num - i / 2))
            print(' ' * space + '*' * i + ' ' * space)
        for i in range(num-2 ,0,- 2):
            space = int((num - i / 2))
            print(' ' * space + '*' * i + ' ' * space)
    else:
        print('Введите правильный номер')


brilliant(7)
