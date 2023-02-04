#%%
# Задача 1
def reverse_list(spisok: list) -> list:
    if not isinstance(spisok, list):  # проверяет объект на тип
        print('type is not list')
        raise TypeError
    # reverse_spisok = spisok[::-1]
    # return reverse_spisok
    return list(reversed(spisok))
#print(reverse_list((1, 2, 3, 4, 5)))

el = [1, 2, 3]
print(el)
el.reverse()
print(el)

#%%
# Задача 2
from typing import Sequence  # тип подходящий для всех последовательностей

def drop_duplicate(seq: Sequence) -> Sequence:
    if not isinstance(seq, (list, tuple, str)):
        raise TypeError
    uniq_el = set()
    result = []
    for el in seq:
        if el not in uniq_el:
            result.append(el)
            uniq_el.add(el)
    return result

print(drop_duplicate('aaabbbcccddd'))



# %%
# Задача 3
from typing import Sequence
def count_nonuniqe(seq: Sequence) -> int:
    if not isinstance(seq, (list, tuple, str)):
        raise TypeError
    count_el = dict()
    for el in seq:
        if el not in count_el:
            count_el[el] = 1
        else: 
            count_el[el] += 1
    result = 0
    for k in count_el:
        if count_el[k] > 1:
            result += 1
    return result

print(count_nonuniqe('qweeerrrtyy'))

# %%
# Задача 4
from typing import List

def split_to_digits(num: int) -> List[int]:
    if not isinstance(num, int) or num <= 0:
        raise TypeError
    list_of_num = []
    while num > 0:
        list_of_num.append(num % 10)
        num = num // 10
    return list(reversed(list_of_num))
print(split_to_digits(45678))


# %%
# Задача 5

# Смотри скрин вк

# %%
# Задача 6

a = ['foo', 'bar', 'baz', 'egg']
b = ['bar', 'baz']
#'отсутствуют: foo, egg' Пример 1
#'foo и egg отсутствуют!' Пример 2

k = list(set(a).difference(set(b)))  # не сохраняет порядок
print(f'отсутствуют: {k}')  
# %%
# Задача 6
from typing import Sequence

a = ['foo', 'bar', 'baz', 'egg']
b = ['bar', 'baz']

# Поиск в set быстрее чем в list, поэтому лучше перевести в set

def substract_list(seq_1, seq_2: Sequence) -> list:
    mas = []
    set_seq_2 = set(seq_2)
    for el in seq_1:
        if el not in set_seq_2:
            mas.append(el)
    return mas
print(substract_list(a, b))



# %%
# Задача 7

def validate_coords(*coords) -> list:
    error = []
    list_of_errors = []
    for lat, long in coords:
        if lat < -90 or lat > 90:
            error.append(f'Неверно задана широта: {lat} (должна быть от -90.0 до 90.0)')
        if long < -90 or long > 90:
            error.append(f'Неверно задана долгота: {long} (должна быть от -180.0 до 180.0)')
        if not error:
            continue
        list_of_errors.append({
                'lat': lat,
                'long': long,
                'error': error
            })
    return list_of_errors
print(validate_coords((0.0, 1.0),
    (-35.7, -100.7),
    (-95.0, 120.5),
    (88.8, 190.5),
    (17.33, 18.46),
    (-120.0, -200.1),))

# %%
# Задача 8
from collections import defaultdict

def count_words(sen: str) -> dict:
    words = sen.split()
    res = defaultdict(int)
    for word in words:
        word = word.lower()
        # if word not in res:
        #     res[word] = 1
        # else:
        #     res[word] += 1
        res[word] += 1
    return res

print(count_words('one plus TWO equals four and four plus FOUR equals eight'))
# %%
# Задача 9

def check_branches(text: str) -> int:
    branches= []
    brackets_map = {')':'(', ']': '[', '}': '{'}
    for i, s in enumerate(text):
        if s in ['(','[','{']:
            branches.append(s)
        elif s in [')',']','}']:
            if not branches:
                return i
            last_branch = branches.pop()
            if brackets_map[s] != last_branch:
                return i
    if branches:
        return len(branches)
    return -1
print(check_branches('Hi (my [name is [ Slam]] ) Shady'))

# %%
# Задача 10
def generate_password(strength: int = 1, length: int = None, from_source: str = None) -> str:
    symbols = ''
    if from_source:
        symbol = from_source
    else:
        if strength == 0:
            symbol = string.digits
            
    if not length:
        length = random.randint(4,16)
    
    result = ''
    for i in range(length):
        result += random.choice(symbol)
    
    return result

# %%
