# noinspection PyUnusedLocal
# skus = unicode string

from collections import defaultdict


prices_one = {"A": 50, "B": 30, "C": 20, "D": 15}
specials_one = {"A": (3, 130), "B": (2, 45)}


def checkout_one(skus):
    cart = defaultdict(int)
    for sku in skus:
        if sku not in prices_one:
            return -1
        cart[sku] += 1

    total = 0
    for item, count in cart.items():
        # check if we apply any discounts
        regular_price = prices_one[item]
        if item in specials_one:
            (special_count, special_price) = specials_one[item]
            number_of_deals_on_item = count // special_count
            remaining_items = count % special_count

            special_cost = special_price * number_of_deals_on_item
            regular_cost = remaining_items * regular_price

            total += special_cost + regular_cost
        else:
            total += regular_price * count

    return total


prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
specials = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}
bogo = {"E": 2}


def checkout(skus):
    cart = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        cart[sku] += 1

    total = 0

    if "E" in cart:
        number_of_e = cart["E"]
        special_count = bogo["E"]
        number_of_times = number_of_e // special_count
        cart["B"] = max(0, cart["B"] - number_of_times)

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
                    print(f"({current_count=} {special_count=}, {special_price=})")
                    number_of_deals_on_item = current_count // special_count
                    special_cost = special_price * number_of_deals_on_item

                    print(
                        f"({number_of_deals_on_item=}, at current rate of {special_price=} will cost us {special_cost=}"
                    )
                    total += special_cost
                    print(
                        f"current count currently is {current_count} and special count is {special_count}"
                    )
                    current_count -= special_count * number_of_deals_on_item
                    print(f"current count is now {current_count}")

            regular_cost = current_count * regular_price
            total += regular_cost

        else:
            total += regular_price * count

    return total


