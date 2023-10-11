from give_bmi import give_bmi, apply_limit
import unittest


def test_mandatory():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


class testGiveBmi(unittest.TestCase):
    def test_size_mismatch(self):
        self.assertEqual(give_bmi([1.78], [2.98, 32.31]), None)

    def test_invalid_height(self):
        self.assertEqual(give_bmi(["toto"], [50.2]), None)

    def test_invalid_weight(self):
        self.assertEqual(give_bmi([1.64], ["tutu"]), None)


if __name__ == "__main__":
    test_mandatory()
    unittest.main()

