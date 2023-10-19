from S1E9 import Character, Stark
import unittest as ut


def test_mandatory():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    try:
        hodor = Character("hodor")
        print(hodor.__doc__)
    except TypeError as error:
        print(f"TypeError: {error}")


class testStarckClass(ut.TestCase):
    """test Starck class

    Args:
        ut (unittest.TestCase): module for ut
    """

    def test_invalid_first_name(self):
        """test Starck class instanciation with invalid first_name param
        """
        with self.assertRaises(AssertionError) as cm:
            Stark(42)
        self.assertEqual(str(cm.exception), 'first_name must be str')

        with self.assertRaises(AssertionError):
            Stark({})

        with self.assertRaises(AssertionError) as cm:
            Stark(3.14)
        self.assertEqual(str(cm.exception), 'first_name must be str')

        with self.assertRaises(AssertionError):
            Stark(False)

    def test_invalid_is_alive(self):
        """test Starck class instanciation with invalid is_alive param
        """
        with self.assertRaises(AssertionError) as cm:
            Stark("Ned", 123)
        self.assertEqual(str(cm.exception), 'is_alive must be bool')

        with self.assertRaises(AssertionError):
            Stark("to", "to")
        with self.assertRaises(AssertionError) as cm:
            Stark("Ned", [[[]]])
        self.assertEqual(str(cm.exception), 'is_alive must be bool')

        with self.assertRaises(AssertionError):
            Stark("to", "false")


class testCharacterClass(ut.TestCase):
    """test Character class instantiation
     Args:
        ut (unittest.TestCase): module for ut
    """

    def test_instantiate_with_abstract_method(self):
        """test if abstract class Character containing an abstract method
raises error in case it is instanciated.
        """
        with self.assertRaises(TypeError):
            Character('Ned')


if __name__ == "__main__":
    test_mandatory()
    ut.main()
