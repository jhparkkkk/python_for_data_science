import math


def NULL_not_found(object: any) -> int:
    type_message = {
        type(None): "Nothing",
        float: "Cheese",
        int: "Zero",
        bool: "Fake",
        str: "Empty",
    }

    message = type_message.get(type(object))
    value = object

    if isinstance(object, str):
        if value != "":
            message = "Type not found"

    if message == "Fake":
        if value != False:
            message = "Type not found"

    if message == "Zero":
        if value:
            message = "Type not found"

    if isinstance(object, float):
        try:
            if math.isnan(object):
                value = "nan"
            elif abs(object) < 1e-30:
                message = "Cheese"
            else:
                message = "Type not found"
        except TypeError:
            message = "Type not found"

    # create message to display
    if message == "Type not found":
        print(message)
        return 1
    else:
        if message == "Empty":
            print(f"{message}: {type(object)}")
        else:
            print(f"{message}: {value} {type(object)}")
        return 0
