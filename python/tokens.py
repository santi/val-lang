
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
        return f"field:{str(self.value)}"

class Variable:
    name = None
    context = None

    def __init__(self, name, context):
        self.name = name
        self.context = context

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"var:{self.name}"

    def __getattr__(self, attr):
        if attr == 'value':
            return self.context[self.name].value
        elif attr == 'type':
            return self.context[self.name].type
        else:
            raise AttributeError(attr)
    