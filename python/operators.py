import re

class Operator:

    type = None
    context = None  # Program context passed by reference

    def __init__(self, type, context):
        self.type = type
        self.context = context

    def apply(self, op1, op2):
        raise NotImplementedError("Must subclass Operator")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"op:{str(self.type)}"

class LTOperator(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op1} < {op2}")
        if not op1 < op2:
            raise ValueError


class GTOperator(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op1} > {op2}")
        if not op1 > op2:
            raise ValueError


class RegexOperator(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op2} on {op1}")
        if not re.match(op2.value, op1.value):
            raise ValueError


class AssignOperator(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op1} = {op2}")
        self.context[op1.name] = op2

operators = {
    "<": LTOperator,
    ">": GTOperator,
    "~": RegexOperator,
    "=": AssignOperator
}