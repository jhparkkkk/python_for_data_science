from array2D import slice_me
import unittest


def test_mandatory():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


class testSliceMe(unittest.TestCase):
    def test_list_size(self):
        print("test_list_size")
        family = [[1.80], [2.15, 102.7]]
        self.assertEqual(slice_me(family, 0, 1), None)
    
    def test_not_a_list(self):
        family = {}
        self.assertEqual(slice_me(family, 0, 1), None)

if __name__ == "__main__":
    test_mandatory()
    unittest.main()