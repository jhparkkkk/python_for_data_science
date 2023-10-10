import sys
import re


def main():
    """
    The program should output a list of words from S that have a length greater than N.
    Args:
        S(str): The string to analyze
        N(int): min len a word must be to get output
    Returns:
        none
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        # Check if argv[1] is a string
        if not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")

        # Check if argv[2] is an integer
        if not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        # split argv[1] and store parts in words_list
        word_list = sys.argv[1].split()
        # for each element check for invalid character using lambda
        problemo = filter(
            lambda item: not re.match("^[a-zA-Z0-9' ']+$", item), word_list
        )
        # convert filter object to a list
        problemo_list = list(problemo)
        # if problemo_list is not empty then there's issue with argv[1]!
        if problemo_list:
            raise AssertionError("Argument should contain only alphanumeric characters")
        # get min_len from argv[2]
        min_len = int(sys.argv[2])
        # filtering list using list comprehension
        res_list = [item for item in word_list if len(item) > min_len]
        print(res_list)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
