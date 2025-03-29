# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict


prices = {"A": 50, "B": 30, "C": 20, "D": 15}
specials = {"A": (3, 130), "B": (2, 45)}


def checkout_one(skus):
    cart = defaultdict(int)
    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    total = 0
    for item, count in cart.items():
        # check if we apply any discounts
        regular_price = prices[item]
        if item in specials:
            (special_count, special_price) = specials[item]
            number_of_deals_on_item = count // special_count
            remaining_items = count % special_count

            special_cost = special_price * number_of_deals_on_item
            regular_cost = remaining_items * regular_price

            total += special_cost + regular_cost
        else:
            total += regular_price * count

    return total


