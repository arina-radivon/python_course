import keyword


class MovetoPython:  # TODO: rename
    """Returns JSON object in Python dict-object and adding attributs"""
    def __init__(self, adt: dict):
        for key in adt.keys():
            temp_key = key
            if keyword.iskeyword(key):  # добавляем _ если слово ключевое
                temp_key = key + '_'

            if type(adt[key]) is dict:
                setattr(self, temp_key, MovetoPython(adt[key]))  # рекурсия
            else:
                setattr(self, temp_key, adt[key])


class ColorizeMixin:
    """Colorizes text"""
    repr_color_code = '\033[33m'  # выводим строку желтым
    end_to_base_color = '\033[0m'  # возвращаем к исходному цвету

    def __repr__(self):
        return f'{self.repr_color_code} {self.end_to_base_color}'


class Advert(ColorizeMixin, MovetoPython):
    """MovetoPython class heir. Supplements the functionality,
    imposes conditions on the attributes of the parent class."""
    def __init__(self, adt: dict):
        super().__init__(adt)

        if 'title' not in self.__dict__.keys():
            raise NameError('Oops! Your ad has not got title, but must have')

        if 'price' not in self.__dict__.keys():
            self.price = 0
        elif self.price < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        # Для корректной работы без миксина используем try-except:
        try:
            color_beauty, color_base = super().__repr__().split(sep=' ')
        except ValueError:
            color_beauty, color_base = '', ''
        return color_beauty + f'{self.title} | {self.price} ₽' + color_base


if __name__ == '__main__':

    slov_1 = {
        "title": "python",
        "price": 10,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }

    slov_2 = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок Тишково, 25"
            }
        }

    pyt = Advert(slov_1)
    corgi = Advert(slov_2)
    print(corgi.price)
    print(pyt.price)
    print(corgi.location.address)
    print(corgi.class_)
    print(corgi)
