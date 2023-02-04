class BasePokemon:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    ICON = {
        'grass': '🌿',
        'electric': '⚡',
        'water': '🌊',
        'fire': '🔥'
    }

    def __str__(self):
        for cat, emoji in self.ICON.items():
            replased = self.category.replace(cat, emoji)
            if replased != self.category:
                return f'{self.name}/{replased}'
        return f'{self.name}/{self.category}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Pikachu', category='electric')
    print(bulbasaur)
