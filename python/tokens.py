
class Value:

    value = None
    type = None

    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __lt__(self, other):
        if self.type != other.type:
            raise ValueError(f"incompatible comparison between {self.type} and {other.type}")
        return self.value < other.value

    def __gt__(self, other):
        if self.type != other.type:
            raise ValueError(f"incompatible comparison between {self.type} and {other.type}")
        return self.value > other.value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{str(self.type)}:{str(self.value)}"

class Field:

    value = None
    type = None

    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def __lt__(self, other):
        if self.type != other.type:
            raise ValueError(f"incompatible comparison between {self.type} and {other.type}")
        return self.value < other.value

    def __gt__(self, other):
        if self.type != other.type:
            raise ValueError(f"incompatible comparison between {self.type} and {other.type}")
        return self.value > other.value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.value)

