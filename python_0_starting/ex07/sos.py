import sys
import re


def main():
    """
    takes a string as an argument and encodes it into Morse Code.
    Args:
        to_encode : string to encode
    Returns:
        none
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert re.match("^[a-zA-Z0-9' ']+$", sys.argv[1]), "the arguments are bad"
        # convert argv[1] to upper letters
        to_encode = sys.argv[1].upper()

        # create list with encoded character
        encoded_list = [NESTED_MORSE[char] for char in to_encode]

        reformated_list = [item if item != "/ " else " " for item in encoded_list]

        print("".join(reformated_list))

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
