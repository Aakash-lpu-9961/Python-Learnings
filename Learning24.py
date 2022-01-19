# Snake Water Gun Game In Python

import random


"""
    Snake + Gun = Gun
    Water + Snake = Snake
    Gun + water = Water
    Snake + Snake = Tie
    Water + Water = Tie
    Gun + Gun = Tie
"""

lst = ["Snake", "Water", "Gun"]
b= random.choice(lst)

for items in lst:
    print(lst)