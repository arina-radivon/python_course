import pizza
import cli


def test_baseclass():
    piz = pizza.Base()
    test_ingredient = ['thin or fluffy dough']
    assert piz.ingredients == test_ingredient


def test_equal(capsys):
    piz1 = pizza.Pepperoni()
    piz2 = pizza.Margherita()
    piz1 == piz2
    out, err = capsys.readouterr()
    assert 'Same ingredients' in out
    assert 'Unique Margherita 🧀 ingredients' in out
    assert 'Unique Pepperoni 🍕 ingredients' in out


def test_margherita():
    piz = pizza.Margherita()
    test_name = 'Margherita 🧀'
    assert piz.name == test_name


def test_pepperoni():
    piz = pizza.Pepperoni()
    test_emoji_ingredients = ['🫓', '🥫', '🧀', '🥓']
    assert piz.emoji_ingredients == test_emoji_ingredients


def test_hawaiian():
    piz = pizza.Hawaiian()
    test_recipe = ['thin or fluffy dough',
                   'tomato sauce', 'mozzarella',
                   'chiken',
                   'pineapples']
    assert test_recipe in piz.recipe.values()


def test_pet():
    piz = pizza.PizzaForPet()
    test_description = 'Only natural products with care for your pet'
    assert piz.description == test_description


def test_bake(capsys):
    cli.bake(pizza.Pepperoni())
    out, err = capsys.readouterr()
    assert '🍳 Cooked in ' in out


def test_deliver(capsys):
    cli.deliver(pizza.Hawaiian())
    out, err = capsys.readouterr()
    assert '🛵 Delivered in ' in out


def test_pickup(capsys):
    cli.pickup(pizza.Margherita())
    out, err = capsys.readouterr()
    assert '🛍 Picked up in ' in out


def test_order(capsys):
    cli.order_independent('pizzaforpet', False)
    out, err = capsys.readouterr()
    assert 'Your order Pizza for your pet 🐈 in size L received' in out


def test_order_pickup(capsys):
    cli.order_independent('pepperoni', False)
    out, err = capsys.readouterr()
    assert '🛍 Picked up in' in out


def test_order_delivery(capsys):
    cli.order_independent('hawaiian', True)
    out, err = capsys.readouterr()
    assert '🛵 Delivered in ' in out


def test_menu(capsys):
    cli.menu_independent()
    out, err = capsys.readouterr()
    assert 'Only natural products with care for your pet' in out


def test_childrenmenu(capsys):
    cli.childrenmenu_independent()
    out, err = capsys.readouterr()
    assert "['🥕', '🥦', '🥬', '🥩']" in out
