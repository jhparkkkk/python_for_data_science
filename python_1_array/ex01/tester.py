from array2D import slice_me
from unittest import TestCase, main


def test_mandatory():
    """mandatory tests given by the subject
    """
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


class testSliceMe(TestCase):
    def test_list_empty(self):
        """test with empty lists
        """
        family = []
        self.assertEqual(slice_me(family, 0, 1), None)

    def test_list_size(self):
        """test if subsequent lists are not the same size
        """
        family = [[1.80], [2.15, 102.7]]
        self.assertEqual(slice_me(family, 0, 1), None)

    def test_not_a_list(self):
        """test if list is type of list
        """
        family = {1, 2, 3}
        self.assertEqual(slice_me(family, 0, 1), None)
        family = (1, 2, 3)
        self.assertEqual(slice_me(family, 0, 1), None)
        family = [1, 2, 3]
        self.assertEqual(slice_me(family, 0, 1), None)

    def test_valid_list(self):
        """test with valid arguments
        """
        family = [[1], [2], [3]]
        self.assertEqual(slice_me(family, 0, 1), [[1]])
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        self.assertEqual(slice_me(family, 0, 2), [[1.8, 78.4], [2.15, 102.7]])
        self.assertEqual(slice_me(family, 1, -2), [[2.15, 102.7]])
        family = [["jee"], ["hyun"]]
        self.assertEqual(slice_me(family, 0, 1), [["jee"]])


if __name__ == "__main__":
    test_mandatory()
    main()
