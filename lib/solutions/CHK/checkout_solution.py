# noinspection PyUnusedLocal
# skus = unicode string

inventory = {"A": 50, "B": 30, "C": 20, "D": 15}


def checkout(skus):
    for sku in skus:
        if sku not in inventory:
            return -1

