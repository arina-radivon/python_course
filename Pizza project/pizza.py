class Base:
    """
    The base class for all pizzas.
    """
    def __init__(self, size: str = 'L'):
        """
        For each pizza you need: name, size and ingredients.
        A separate recipe for younger guests. No words, just emoji!
        """
        self.name = 'Pizza base'
        self.description = 'Pizza description'
        self.size = size
        self.ingredients = ['thin or fluffy dough']
        self.emoji_ingredients = ['🫓']
        self.recipe = self._dict(self.name, self.ingredients)
        self.child_recipe = self._dict(self.name, self.emoji_ingredients)

    def _dict(self, name, ingredients):
        """
        Returning a pizza recipe as a dictionary
        """
        recipe = dict()
        recipe[name] = ingredients
        return recipe

    def dict(self):
        """
        Returning a pizza information as a dictionary
        """
        pizza_inform = {
            'name': self.name,
            'size': self.size,
            'ingredients': self.ingredients,
            'emoji_ingredients': self.emoji_ingredients
        }
        return pizza_inform

    def __eq__(self, other):
        """
        Comparing two pizzas, printing the same and unique ingredients
        """
        same = list()
        unique_self = list()
        unique_other = list()

        for product in self.ingredients:
            if product in other.ingredients:
                same.append(product)
            else:
                unique_self.append(product)

        for product in other.ingredients:
            if product not in self.ingredients:
                unique_other.append(product)

        print('Same ingredients:', same)
        print(f'Unique {self.name} ingredients: ', unique_self)
        print(f'Unique {other.name} ingredients:', unique_other)

        if unique_self == [] and unique_other == []:
            return True
        else:
            return False


class Margherita(Base):
    """
    Class for everyone's favorite pizza Margherita
    """
    def __init__(self, size: str = 'L'):
        """
        For each pizza you need: name, size and ingredients
        """
        super().__init__(size)
        self.name = 'Margherita 🧀'
        self.description = 'Everyones favorite pizza with juicy Baku tomatoes.'
        self.size = size
        self.ingredients = [
                            'thin or fluffy dough',
                            'tomato sauce',
                            'mozzarella',
                            'tomatoes'
                             ]
        self.emoji_ingredients = ['🫓', '🥫', '🧀', '🍅']
        self.recipe = self._dict(self.name, self.ingredients)
        self.child_recipe = self._dict(self.name, self.emoji_ingredients)


class Pepperoni(Base):
    """
    Pepperoni pizza class. Simple and tasteful.
    """
    def __init__(self, size: str = 'L'):
        """
        For each pizza you need: name, size and ingredients
        """
        super().__init__(size)
        self.name = 'Pepperoni 🍕'
        self.description = 'Timeless classic with sausages straight from Italy'
        self.size = size
        self.ingredients = [
                            'thin or fluffy dough',
                            'tomato sauce',
                            'mozzarella',
                            'pepperoni'
                             ]
        self.emoji_ingredients = ['🫓', '🥫', '🧀', '🥓']
        self.recipe = self._dict(self.name, self.ingredients)
        self.child_recipe = self._dict(self.name, self.emoji_ingredients)


class Hawaiian(Base):
    """
    Class for Hawaiian pizza. For lovers of unusual tastes.
    """
    def __init__(self, size: str = 'L'):
        """
        For each pizza you need: name, size and ingredients
        """
        super().__init__(size)
        self.name = 'Hawaiian 🍍'
        self.description = 'Combination of soft chicken and juicy pineapples'
        self.size = size
        self.ingredients = [
                            'thin or fluffy dough',
                            'tomato sauce',
                            'mozzarella',
                            'chiken',
                            'pineapples'
                             ]
        self.emoji_ingredients = ['🫓', '🥫', '🧀', '🍗', '🍍']
        self.recipe = self._dict(self.name, self.ingredients)
        self.child_recipe = self._dict(self.name, self.emoji_ingredients)


class PizzaForPet(Base):
    """
    Pets like pizza too.
    """
    def __init__(self, size: str = 'L'):
        """
        For each pizza you need: name, size and ingredients
        """
        super().__init__(size)
        self.name = 'Pizza for your pet 🐈'
        self.description = 'Only natural products with care for your pet'
        self.size = size
        self.ingredients = [
                            'Carrot puree cake',
                            'boiled broccoli',
                            'greens',
                            'steamed beef'
                             ]
        self.emoji_ingredients = ['🥕', '🥦', '🥬', '🥩']
        self.recipe = self._dict(self.name, self.ingredients)
        self.child_recipe = self._dict(self.name, self.emoji_ingredients)


if __name__ == '__main__':
    a = Hawaiian()
    b = Pepperoni()
    print(a.recipe)  # printing recipe
    print(b.child_recipe)  # printing emoji recipe
    print(a.description)  # Combination of soft chicken and juicy pineapples
    print(a.dict())
