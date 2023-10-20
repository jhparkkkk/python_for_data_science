import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate a random id for each new student

    Returns:
        str: student's id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Create a class Student to store data

    Raises:
        TypeError: name and surname must be str
    """
    name: str
    surname: str
    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError('Name should be of type str')
        if not isinstance(self.surname, str):
            raise TypeError('Surname should be of type str')
        self.active = True
        self.login = self.name[0] + self.surname
        self.id = generate_id()
