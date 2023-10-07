from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

print("\nmy tests:")
NULL_not_found(0.0000000000000000)
NULL_not_found(3.14)
NULL_not_found(True)
NULL_not_found(20)
NULL_not_found("                ")
NULL_not_found("**(@*#(!))")
NULL_not_found(-0)
