# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict
from typing import DefaultDict


prices = {"A": 50, "B": 30, "C": 20, "D": 15}
specials = {"A": (3, 130), "B": (2, 25)}


def checkout(skus):
    cart = defaultdict(int)
    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    total = 0
    for item, count in cart.items():
        # check if we apply any discounts
        if item in specials:
            (count, special_price) = specials[item]
        else:
            total += prices[item] * count

    return total





