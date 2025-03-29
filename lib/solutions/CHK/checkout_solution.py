# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
from typing import DefaultDict


prices = {"A": 50, "B": 30, "C": 20, "D": 15}
specials = {"3A": 130, "2B": 25}


def checkout(skus):
    cart = defaultdict(int)
    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1


