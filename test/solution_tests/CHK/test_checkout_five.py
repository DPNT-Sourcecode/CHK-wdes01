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
        assert checkout("K") == 70
        assert checkout("L") == 90
        assert checkout("M") == 15
        assert checkout("N") == 40
        assert checkout("O") == 10
        assert checkout("P") == 50
        assert checkout("Q") == 30
        assert checkout("R") == 50
        assert checkout("S") == 20
        assert checkout("T") == 20
        assert checkout("U") == 40
        assert checkout("V") == 50
        assert checkout("W") == 20
        assert checkout("X") == 17
        assert checkout("Y") == 20
        assert checkout("Z") == 21

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
        assert checkout("HHHHHHHHHHZHHHHHZHHHHHHHHHH") == 80 + 21 + 45 + 21 + 80
        assert checkout("VVZVVVZVVV") == 90 + 21 + 130 + 21 + 130

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

        assert checkout("NNM") == (40 * 2) + 15
        assert checkout("NNN") == (40 * 3)

        assert checkout("RRQ") == (50 * 2) + 30
        assert checkout("RRRQ") == (50 * 3)

        # acts like 3 Rs and 3 Qs, 3Qs has promotion
        assert checkout("QQQQRRR") == (50 * 3) + (80)

    def test_fake_buy_one_get_b_free(self):
        assert checkout("FF") == 20
        assert checkout("FFF") == 20

        assert checkout("FFFF") == 20 + 10
        assert checkout("FFFFFF") == 20 + 20

        assert checkout("UUU") == (40 * 3)
        assert checkout("UUUU") == (40 * 3)

    def test_group_discount(self):
        assert checkout("SS") == 40
        assert checkout("SSS") == 45
        assert checkout("XY") == 17 + 20

        assert checkout("SSTXYZ") == 45 + 45

        # we should favor decrementing the most expensive ones first
        assert checkout("ZZZS") == 45 + 20
        assert checkout("STXS") == 62
        assert checkout("STXZ") == 62
