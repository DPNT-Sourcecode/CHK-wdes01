from lib.solutions.CHK.checkout_solution import checkout_one


class TestSum:
    def test_checkout_one_invalid_input(self):
        assert checkout_one("A-") == -1
        assert checkout_one("-") == -1
        assert checkout_one(" ") == -1

    def test_checkout_one_single_items(self):
        assert checkout_one("A") == 50
        assert checkout_one("B") == 30
        assert checkout_one("C") == 20
        assert checkout_one("D") == 15

    def test_checkout_one_multiple_non_discount_items(self):
        assert checkout_one("ABCD") == 50 + 30 + 20 + 15
        assert checkout_one("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_one_discount_items_only(self):
        assert checkout_one("AAA") == 130
        assert checkout_one("BB") == 45

    def test_checkout_one_multiple_discount_items(self):
        assert checkout_one("AAAAAA") == 130 * 2
        assert checkout_one("BBBBBB") == 45 * 3

    #
    def test_checkout_one_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout_one("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout_one("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout_one("AAABBCD") == (130) + (45) + 20 + 15
        assert checkout_one("AAABBCDAAA") == (2 * 130) + (45) + 20 + 15
        #
        # one A promotion, one b promotion 2 a's left over
        assert checkout_one("AAABBCDAA") == (130) + (45) + 20 + 15 + (50 * 2)
        assert checkout_one("AAABBCDAAB") == (130) + (45) + 20 + 15 + (50 * 2) + (30)

    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    #####################################

    def test_checkout_two_invalid_input(self):
        assert checkout_one("A-") == -1
        assert checkout_one("-") == -1
        assert checkout_one(" ") == -1

    def test_checkout_two_single_items(self):
        assert checkout_one("A") == 50
        assert checkout_one("B") == 30
        assert checkout_one("C") == 20
        assert checkout_one("D") == 15
        assert checkout_one("E") == 40

    def test_checkout_two_multiple_non_discount_items(self):
        assert checkout_one("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout_one("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_two_discount_items_only(self):
        assert checkout_one("AAAAA") == 200
        assert checkout_one("AAA") == 130
        assert checkout_one("BB") == 45
        assert checkout_one("EE") == 40

    def test_checkout_two_multiple_discount_items(self):
        assert checkout_one("EEEE") == 40 * 2
        assert checkout_one("AAABBCDAAA") == (2 * 130) + (45) + 20 + 15
        # one A promotion, one b promotion 2 a's left over
        assert checkout_one("AAABBCDAA") == (130) + (45) + 20 + 15 + (50 * 2)

    def test_checkout_two_an_item_with_mutliple_special_offers(self):
        assert checkout_one("EEEE") == 40 * 2
        assert checkout_one("BBBBBB") == 45 * 3
        assert checkout_one("BBBBBB") == 45 * 3

    def test_checkout_two_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout_one("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout_one("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout_one("AAABBCDB") == (130) + (45) + 20 + 15 + 30





