from load_csv import load
from unittest import TestCase, main


def test_mandatory():
    print(load("life_expectancy_years.csv"))


class testLoad(TestCase):
    def test_invalid_path(self):
        """test with invalid path
        """
        self.assertEqual(load(""), None)
        self.assertEqual(load("File/does/not.exist"), None)
        self.assertEqual(load(" "), None)
        self.assertEqual(load(""), None)
        self.assertEqual(load("2131"), None)
        self.assertEqual(load("bad.txt"), None)


if __name__ == "__main__":
    test_mandatory()
    main()
