from lib.solutions.CHK.checkout_solution import checkout


class TestSum:
    def test_checkout_two_invalid_input(self):
        assert checkout("A-") == -1
        assert checkout("-") == -1
        assert checkout(" ") == -1

    def test_checkout_two_single_items(self):
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15
        assert checkout("E") == 40

    def test_checkout_two_multiple_non_discount_items(self):
        assert checkout("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_two_discount_items_only(self):
        assert checkout("AAAAA") == 200
        assert checkout("AAA") == 130
        assert checkout("BB") == 45
        assert checkout("EE") == 40

    def test_checkout_two_multiple_discount_items(self):
        # both promotions should be applied
        assert checkout("AAAAABAAA") == 200 + 130 + 30

    def test_checkout_two_an_item_with_mutliple_special_offers(self):
        assert checkout("EEEE") == 40 * 2
        assert checkout("BBBBBB") == 45 * 3
        assert checkout("BBBBBB") == 45 * 3

    def test_checkout_two_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout("AAABBCDB") == (130) + (45) + 20 + 15 + 30
        # one A and B and 1 E promotion
        assert checkout("AAABBCDBEE") == (130) + (45) + 20 + 15 + 30 + 40
        # one A and B and 1 E promotion, with B and E leftover
        assert checkout("AAABBEECDBE") == (130) + (45) + (40) + 20 + 15 + 30 + 40




