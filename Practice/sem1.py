# %%
# 1 вывести все элементы a, которые есть в b
a = [0, 1, 2, 3, 4, 5]
b = [3, 4, 5]
c = []

for i in range(len(b)):
    if b[i] in a:
        c = c.append(b[i])
print(c)


# %%
# 2 создайте новый массив с уникальными значениями
a = [0, 0, 1, 1, 2, 2]

print(list(set(a))) 

# %%
# 3 создайте новый массив с четными элементами
# исходный массив
a = [0, 1, 2, 3, 4, 5]
# результат
b = [0, 2, 4]

for i in range(len(a)):
    if (int(a[i]) % 2 = 0)
        b.append(a[i])
print(b)        


# %%

# 4 создайте словарь из списка, где ключ - индекс этого элемента
# исходный массив
a = ['foo', 'bar', 'baz']
# результат
b = {0: 'foo', 1: 'bar', 2: 'baz'}
b = dict()

for ind, val in enumerate(a):
    b.update({ind: val})
print(b)

# %%
# 5 распечатайте приветствия
a = [
 'John', 'Allison', 'Brian',
 'Claire', 'Andrew'
]
#'Hi, John!'
# попробуйте разные способы форматирования

# for i in range(len(a)):  итерация по индексам, не надо так
#     print(f'Hi {a[i]}')

for element in a:  # итерация по элементам
 #   print(f'Hi, {element}')
 #   print('Hi, %s' %(element))
     print('Hi, {a}'.format(a = element))


# %%

#  6 напечатайте все элементы из a, которые отсутствуют в b

a = ['foo', 'bar', 'baz', 'egg']
b = ['bar', 'baz']
#'отсутствуют: foo, egg' Пример 1
#'foo и egg отсутствуют!' Пример 2

k = list(set(a).difference(set(b)))
print(f'отсутствуют: {k}')   

# %%

# 7 склейте 2 массива. результат - отсортированный массив
a = [0, 1, 2, 6, 7, 8]
b = [3, 4, 5]

a.extend(b)
a.sort()  # сортирует список
print(a)

# %%

# 8 создайте новый словарь из a с отсортированными ключами в обратном порядке

a = {0: 'foo', 1: 'bar', 2: 'baz'}

b = list(a.keys())[::-1]
# a.update(b = a.values)
# print(a)

print(reversed(a))

# %%

# добыть данные из внешнего API (https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0) 
# и вывести скорость и направление ветра по всем точкам

# 'направление: NW, скорость: 2'
# 'направление: NW, скорость: 3'
# 'направление: W,  скорость: 5'

import requests
import json

response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')

data = response.json()

data_1 = data.get('dataseries')
#print(data_1)

for element in data_1:
#    element['wind10m']
    print(f'направление: {element["wind10m"]["direction"]}, скорость: {element["wind10m"]["speed"]}')    

json.dumps(data_1 , indent=4)



# %%
