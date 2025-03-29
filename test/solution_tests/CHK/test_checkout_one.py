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
        assert checkout("BBB") == 30 * 3


