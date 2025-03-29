# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict


prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}
specials = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    # really a bogo free deal
    "F": [(3, 20)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)],
    # really a bogo free deal
    "U": [(4, 120)],
}
# key -> (number of items needed for discount, how much we discount of pair, pair_item)
bogo = {"E": (2, "B"), "N": (3, "M"), "R": (3, "Q")}


def checkout(skus):
    cart = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    total = 0

    for item, discount_pair in bogo.items():
        if item in cart:
            # how many times do we see that item
            number_of_items = cart[item]
            (special_count, discount_item) = discount_pair

            # how many times should we apply the special
            number_of_times = number_of_items // special_count

            cart[discount_item] = max(0, cart[discount_item] - number_of_times)

    group_discount_items = ["Z", "S", "T", "Y", "X"]
    count_group_discount = sum(cart[item] for item in group_discount_items)
    number_of_times = count_group_discount // 3
    if count_group_discount >= 3:
        total += number_of_times * 45

    decrement_count = number_of_times * 3
    while decrement_count > 0:
        current_index = 0
        current_item = group_discount_items[current_index]
        print(f"{current_index} and {current_item=}")
        if cart[current_item] > 0:
            cart[current_item] -= 1
            decrement_count -= 1
        else:
            current_index = current_index + 1

    for item, count in cart.items():
        # check if we apply any discounts
        regular_price = prices[item]
        if item in specials:
            specials_list = specials[item]
            current_count = count
            for special_count, special_price in specials_list:
                if special_count > current_count:
                    continue
                    # after we applied all promotions, see if we do anything at regular cost
                    # in the case there is non left, we are adding 0
                else:
                    number_of_deals_on_item = current_count // special_count
                    special_cost = special_price * number_of_deals_on_item

                    total += special_cost
                    current_count -= special_count * number_of_deals_on_item

            regular_cost = current_count * regular_price
            total += regular_cost

        else:
            total += regular_price * count

    return total









