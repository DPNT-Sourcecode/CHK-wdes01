from lib.solutions.CHK.checkout_solution import checkout_two


class TestSum:
    def test_checkout_two_invalid_input(self):
        assert checkout_two("A-") == -1
        assert checkout_two("-") == -1
        assert checkout_two(" ") == -1

    def test_checkout_two_single_items(self):
        assert checkout_two("A") == 50
        assert checkout_two("B") == 30
        assert checkout_two("C") == 20
        assert checkout_two("D") == 15
        assert checkout_two("E") == 40

    def test_checkout_two_multiple_non_discount_items(self):
        assert checkout_two("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout_two("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_two_discount_items_only(self):
        assert checkout_two("AAAAA") == 200
        assert checkout_two("AAA") == 130
        assert checkout_two("BB") == 45
        assert checkout_two("EE") == 40

    def test_checkout_two_multiple_discount_items(self):
        # both promotions should be applied
        assert checkout_two("AAAAABAAA") == 200 + 130 + 45

    def test_checkout_two_an_item_with_mutliple_special_offers(self):
        assert checkout_two("EEEE") == 40 * 2
        assert checkout_two("BBBBBB") == 45 * 3
        assert checkout_two("BBBBBB") == 45 * 3

    def test_checkout_two_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout_two("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout_two("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout_two("AAABBCDB") == (130) + (45) + 20 + 15 + 30
        # one A and B and 1 E promotion
        assert checkout_two("AAABBCDBEE") == (130) + (45) + 20 + 15 + 30 + 40
        # one A and B and 1 E promotion, with B and E leftover
        assert checkout_two("AAABBEECDBE") == (130) + (45) + (40) + 20 + 15 + 30 + 40



