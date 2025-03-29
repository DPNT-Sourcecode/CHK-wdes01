from lib.solutions.CHK.checkout_solution import checkout


class TestSum:
    def test_checkout_invalid_input(self):
        assert checkout("A-") == -1
        assert checkout("-") == -1
        assert checkout(" ") == -1

    def test_checkout_single_items(self):
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15

    def test_checkout_multiple_non_discount_items(self):
        assert checkout("ABCD") == 50 + 30 + 20 + 15
        assert checkout("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_discount_items_only(self):
        assert checkout("AAA") == 130
        assert checkout("BB") == 45

    def test_checkout_multiple_discount_items(self):
        assert checkout("AAAAAA") == 130 * 2
        assert checkout("BBBBBB") == 45 * 3

    #
    def test_checkout_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout("AAABBCD") == (50 * 2) + 45 + 20 + 15
        # one A promotion, one b promotion 2 a's left over
        assert checkout("AAABBCDAA") == (50 * 2) + 45 + 20 + 15

