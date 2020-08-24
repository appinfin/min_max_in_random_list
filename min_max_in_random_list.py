import random

def generation_random_number():
    """Ф-ция генерирует список случайных чисел"""
    random_list = []
    for n in range(10): # кол-во чисел в списке 10
        random_list.append(round(random.uniform(1, 100)/3*1.3,2))

    return random_list

received_list = generation_random_number() # полученный список случайных чисел

print('Сгенерированный массив случайных чисел:\n', received_list)
print('Минимум в списке (MIN):', min(received_list), '-', end = ' ')
print('Номер по порядку в списке:', received_list.index(min(received_list))+1)

print('Минимум в списке (MAX):', max(received_list), '-', end = ' ')
print('Номер по порядку в списке:', received_list.index(max(received_list))+1)

input()
