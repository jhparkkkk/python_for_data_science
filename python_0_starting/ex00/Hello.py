ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World!"

# tuple
ft_tuple = ft_tuple[:1] + ("France!",)


# set
# custom class that extend set's
class OrderedSet(set):
    # custom how set object is represented as a string
    def __str__(self):
        # convert sorted set into str representation
        return "{" + str(sorted(self))[1:-1] + "}"


ft_set.remove("tutu!")
ft_set.add("Paris")
ft_set = OrderedSet(ft_set)

# dict
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
