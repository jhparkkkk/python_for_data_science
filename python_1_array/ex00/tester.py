from give_bmi import give_bmi, apply_limit
from unittest import TestCase, main


def test_mandatory():
    """mandatory tests given by the subject
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


class testGiveBmi(TestCase):
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    def test_empty_list(self):
        """test with empty lists
        """
        self.assertEqual(give_bmi([1.89], []), None)
        self.assertEqual(give_bmi([], [68.9]), None)
        self.assertEqual(give_bmi([], []), None)

    def test_size_list_mismatch(self):
        """test if the lists are not the same size
        """
        self.assertEqual(give_bmi([1.78], [2.98, 32.31]), None)
        self.assertEqual(give_bmi([1.78, 1.49, 2.01], [2.98, 32.31]), None)

    def test_invalid_height(self):
        """test if height values are int or float
        """
        self.assertEqual(give_bmi(["toto"], [50.2]), None)
        self.assertEqual(give_bmi([True], [50.2]), None)
        self.assertEqual(give_bmi([{}], [50.2]), None)
        self.assertEqual(give_bmi([[[]]], [50.2]), None)

    def test_invalid_weight(self):
        """test if weight values are int or float
        """
        self.assertEqual(give_bmi([1.64], ["tutu"]), None)
        self.assertEqual(give_bmi([1.64], [False]), None)
        self.assertEqual(give_bmi([1.64], [{}]), None)
        self.assertEqual(give_bmi([1.64], [[]]), None)

    def test_valid_weight_and_height_lists(self):
        """test with valid arguments
        """
        self.assertEqual(give_bmi(self.height, self.weight),
                         [22.507863455018317, 29.0359168241966])


class testApplyLimit(TestCase):
    def test_empty_bmi_list(self):
        """test with empty bmi list
        """
        self.assertEqual(apply_limit([], 3), None)

    def test_invalid_bmi_values(self):
        """test if bmi values in list are int or float
        """
        self.assertEqual(apply_limit(["my bmi", "your bmi"], 24), None)
        self.assertEqual(apply_limit([False, False], 24), None)
        self.assertEqual(apply_limit([{}, {}], 24), None)
        self.assertEqual(apply_limit([(), ()], 24), None)

    def test_invalid_limit_value(self):
        """test if limit is a positive integer
        """
        self.assertEqual(apply_limit([2.32], -32), None)
        self.assertEqual(apply_limit([2.32], 32.01), None)
        self.assertEqual(apply_limit([2.32], True), None)

    def test_valid_bmi_and_limit(self):
        """test with valid bmi list and limit
        """
        self.assertEqual(apply_limit(
            [22.507863455018317, 29.0359168241966], 26), [False, True])


if __name__ == "__main__":
    test_mandatory()
    main()
