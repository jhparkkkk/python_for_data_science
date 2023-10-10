import unittest
from ft_package.count_in_list import count_in_list


class TestCountInList(unittest.TestCase):
    def test_count_in_list(self):
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "toto"), 2)
        self.assertEqual(count_in_list(["toto", "tata", "toto"], "tutu"), 0)

        print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
        print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0


unittest.main()
