def step2_umbrella():
    print(
        'Утка-маляр уже давно переехал из Санкт-Петербурга, но старые '
        'привычки остались. '
    )
    print(
        'Кого же из друзей ему позвать? '
        'Быть может, это будет его давняя любовь медсестра-гусеничка '
        'Юля \N{Bug}? '
        'Или старый школьный друг петух-асфальтоукладчик Всеволод \N{Rooster}'
    )
    option = ''
    options = {'Юля': True, 'Всеволод': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return print('Наша пара попала под дождь. Зонтик очень пригодился!')
    return print('О нет! Старые друзья так заболтались, что мистер утка '
                 'забыл зонт в баре. Напомните ему за ним вернуться!')


def step2_no_umbrella():
    print('Кажется, наш отважный маляр не боится непогоды!')
    print('Как вы думаете, пошел ли все-таки дождь?')

    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return print('Мистер утка попал под дождь, промок до нитки и '
                     'ему пришлось вернуться домой. Напомните ему '
                     'проверять прогноз погоды перед прогулкой!')
    return print('Продуманный мистер утка посмотрел прогноз погоды перед '
                 'выходом. Действительно, зачем брать зонт, если не будет '
                 'дождя? Давайте пожелаем ему приятного вечера!')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()