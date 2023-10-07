import sys as sys


def getUserInput():
    """
    Get user input from command line or via prompt

    Raises:
        AssertionError: if more than one argument is provided.

    Returns:
        str: input provided by the user
    """
    try:
        assert len(sys.argv) <= 2, "Only one argument allowed"
        if len(sys.argv) == 1:
            userInput = input("What is the text to count?\n")

            if userInput == "":
                getUserInput()
                exit()
            userInput = userInput.replace("\r", " ")
        else:
            userInput = sys.argv[1]

        print(f"user input is:", userInput, "|")
        return userInput
    except AssertionError as e:
        print("AssertionError:", e)


def countCharacters(userInput: str):
    """
    Count different types of characters in input string.

    Args:
        userInput(str): The input string to analyze.

    Returns:
        none

    Prints character counts for the following types:
        - Upper letters
        - Lower letters
        - Punctuation marks
        - Spaces (including carriage returns)
        - Digits
    """
    characterType = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0,
    }

    conditions_typeLabels = [
        (str.isupper, "upper letters"),
        (str.islower, "lower letters"),
        (str.isspace, "spaces"),
        (str.isdigit, "digits"),
    ]

    for char in userInput:
        for condition, typeLabel in conditions_typeLabels:
            if condition(char):
                characterType[typeLabel] += 1
                break
        else:
            if char == "\r":
                characterType["spaces"] += 1
            characterType["punctuation marks"] += 1

    print(f"The text contains {len(userInput)} characters:")
    for element in characterType:
        print(f"{characterType[element]} {element}")


def main():
    userInput = getUserInput()
    countCharacters(userInput)


# your tests and your error handling
if __name__ == "__main__":
    main()
