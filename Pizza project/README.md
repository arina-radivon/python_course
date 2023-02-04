The project is divided into 3 parts. You can see the condition of the issue in the file Pizza project.pdf.

## pizza.py

The file has separate classes for each pizza. There is also a base class Base, from which the rest are inherited. It spelled out: 

+ A method for creating a recipe in the form of a dictionary 
+ A method for creating a recipe in the form of emoji (without words, using emoji for the convenience of children)
+ A method for comparing two pizzas, which displays the same and different ingredients.

After
```python
if __name__ == '__main__':
```
 examples of the program work are given.

## cli.py

The file contains:

+ The function of displaying the normal and children's menu. A regular menu is displayed with a description of each pizza and a welcome message.
+ An order function that accepts an order, displays a message about it and passes the order on to delivery or pickup.
+ A decorator that wraps the cooking, delivery, and pickup functions and specifies the duration time.

All functions can be used both individually and using the console. To use the listed functions using the console, you should:

Install click package. It can be done using the command in the terminal:
```python
pip install click
```

To display the menu, write in the terminal:
```python
python cli.py menu
```
The same can be done for the children's menu.

To accept an order and send it for delivery, write in the terminal (the example for pepperoni):
```python
python cli.py order pepperoni -–delivery
```

If the order is transferred for self-delivery, then don't write the flag --delivery.

## tests.py

The file provides tests for cli.py and pizza.py files.

To run the code you need:  
Install the appropriate package if you don't have it. This can be done on the command line by typing:
```python
pip install -U pytest
```
Enter in the console:
```python
python -m pytest -v tests.py
```
If you want to check test coverage, firstly, you shoul install the package:
```python
pip install -U pytest-cov
```
After that write in console:
```python
python -m pytest -q tests.py --cov
```
You can save the coverage report to an html file by typing:
```python
python -m pytest -q tests.py --cov . --cov-report html
```
