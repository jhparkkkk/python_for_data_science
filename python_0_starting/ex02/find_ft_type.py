def all_thing_is_obj(object: any) -> int:
    # dictionary with message associated with type name
    type_message = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "Brian is in the kitchen",
    }

    message = (
        type_message.get(type(object))
        if type_message.get(type(object))
        else "Type not found"
    )

    if message == "Type not found":
        print(message)
    else:
        print(f"{message}: {type(object)}")
    return 42
