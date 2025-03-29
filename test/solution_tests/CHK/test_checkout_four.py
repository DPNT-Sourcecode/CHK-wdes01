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
        assert checkout("E") == 40
        assert checkout("F") == 10
        assert checkout("G") == 20
        assert checkout("H") == 10
        assert checkout("I") == 35
        assert checkout("J") == 60
        assert checkout("K") == 80
        assert checkout("L") == 90
        assert checkout("M") == 15
        assert checkout("N") == 40
        assert checkout("O") == 10
        assert checkout("P") == 50
        assert checkout("Q") == 30
        assert checkout("R") == 50
        assert checkout("S") == 30
        assert checkout("T") == 20
        assert checkout("U") == 40
        assert checkout("V") == 50
        assert checkout("W") == 20
        assert checkout("X") == 90
        assert checkout("Y") == 10
        assert checkout("Z") == 50

    def test_checkout_multiple_non_discount_items(self):
        assert checkout("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout("AABCD") == (50 * 2) + 30 + 20 + 15

    def test_checkout_discount_items_only(self):
        assert checkout("AAAAA") == 200
        assert checkout("AAA") == 130
        assert checkout("BB") == 45

    def test_checkout_multiple_discount_items(self):
        # both promotions should be applied
        assert checkout("AAAAABAAA") == 200 + 130 + 30
        assert checkout("HHHHHHHHHHZHHHHHZHHHHHHHHHH") == 80 + 50 + 45 + 50 + 80
        assert checkout("VVZVVVZVVV") == 90 + 50 + 130 + 50 + 130

    def test_checkout_an_item_with_mutliple_special_offers(self):
        assert checkout("BBBBBB") == 45 * 3

    def test_checkout_multiple_discount_items_with_remainder(self):
        # one A promotion
        assert checkout("AAABCD") == 130 + 30 + 20 + 15
        # one B promotion
        assert checkout("AABBCD") == (50 * 2) + 45 + 20 + 15

        # one A and B promotion
        assert checkout("AAABBCDB") == (130) + (45) + 20 + 15 + 30

    def test_buy_one_get_b_free(self):
        assert checkout("EE") == 80
        assert checkout("EEB") == 80
        assert checkout("EEEBB") == (40 * 3) + 30
        assert checkout("EEEEBB") == 40 * 4

    def test_fake_buy_one_get_b_free(self):
        assert checkout("FF") == 20
        assert checkout("FFF") == 20

        assert checkout("FFFF") == 20 + 10
        assert checkout("FFFFFF") == 20 + 20

        assert checkout("UUU") == (40 * 3)
        assert checkout("UUUU") == (40 * 3)



