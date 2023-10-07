import sys as sys


def isInt(v):
    assert str(v).isdigit(), "argument is not an integer"


if len(sys.argv) == 1:
    sys.exit()

try:
    # verify number of arguments
    assert len(sys.argv) == 2, "more than one argument is provided"
    # extract arg
    arg = sys.argv[1]
    # Count the occurrences of '+' and '-'
    plus_count = arg.count("+")
    minus_count = arg.count("-")
    # assert that only one of these signs has been detected
    assert plus_count + minus_count <= 1, "Invalid number format"
    # erase sign
    arg = arg.replace("-", "").replace("+", "")
    # verify if arg is only digit
    isInt(arg)
    # verify if casted arg belongs to int instance
    isinstance(int(arg), int)
    # cast it to int
    number = int(arg)
    # verify if odd or even
    if number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm odd")

except AssertionError as e:
    print("AssertionError: " + str(e))
