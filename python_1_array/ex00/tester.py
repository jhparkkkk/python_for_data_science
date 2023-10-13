from give_bmi import give_bmi, apply_limit
import unittest


def test_mandatory():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


class testGiveBmi(unittest.TestCase):
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    def test_empty_height_list(self):
        self.assertEqual(give_bmi([1.89], []), None)
        self.assertEqual(give_bmi([], [68.9]), None)
        self.assertEqual(give_bmi([], []), None)

    def test_size_list_mismatch(self):
        self.assertEqual(give_bmi([1.78], [2.98, 32.31]), None)
        self.assertEqual(give_bmi([1.78, 1.49, 2.01], [2.98, 32.31]), None)

    def test_invalid_height(self):
        self.assertEqual(give_bmi(["toto"], [50.2]), None)

    def test_invalid_weight(self):
        self.assertEqual(give_bmi([1.64], ["tutu"]), None)

    def test_valid_weight_and_height_lists(self):
        self.assertEqual(give_bmi(self.height, self.weight),
                         [22.507863455018317, 29.0359168241966])


class testApplyLimit(unittest.TestCase):
    def test_empty_bmi_list(self):
        self.assertEqual(apply_limit([], 3), None)

    def test_negative_limit_value(self):
        self.assertEqual(apply_limit([2.32], -32), None)

    def test_float_limit_value(self):
        self.assertEqual(apply_limit([2.32], 32.01), None)


if __name__ == "__main__":
    test_mandatory()
    unittest.main()
