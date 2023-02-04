import click
import pizza
from random import randint


pizza_list = {
    'margherita': pizza.Margherita,
    'pepperoni': pizza.Pepperoni,
    'hawaiian': pizza.Hawaiian,
    'pizzaforpet': pizza.PizzaForPet
}


@click.group()
def cli():
    pass


def log(report='🎯 Made an order in {} minutes!'):
    """
    The decorator to display the runtime.
    In this case, it is a random number from 20 to 40
    """
    def decor(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(report.format(randint(20, 40)))
        return wrapper
    return decor


@log('🍳 Cooked in {} minutes!')
def bake(pizza):
    """
    Something about cooking
    """
    pass


@log('🛵 Delivered in {} minutes!')
def deliver(pizza):
    """
    Something about delivering
    """
    pass


@log('🛍 Picked up in {} minutes!')
def pickup(pizza):
    """
    Something about picking up
    """
    pass


def order_independent(pizza: str, delivery: bool):
    """Taking orders and preparing to sending"""
    order_pizza = pizza_list[pizza.lower()]()
    print(f'Your order {order_pizza.name} in size {order_pizza.size} received')
    bake(order_pizza)
    if delivery:
        deliver(order_pizza)
    else:
        pickup(order_pizza)


def menu_independent():
    """Print menu"""
    print('Welcome to our family pizzeria! You can choose the proposed ' +
          'pizza option, as well as add additional ingredients.')
    for piz in pizza_list.values():
        print(piz().description)
        print(piz().recipe)


def childrenmenu_independent():
    """Print children's menu"""
    for piz in pizza_list.values():
        print(piz().child_recipe)


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Separation the function for using independently of decorators"""
    order_independent(pizza, delivery)


@cli.command()
def menu():
    """Separation the function for using independently of decorators"""
    menu_independent()


@cli.command
def childrenmenu():
    """Separation the function for using independently of decorators"""
    childrenmenu_independent()


if __name__ == '__main__':
    cli()
