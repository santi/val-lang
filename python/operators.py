import re

class Operator:

    type = None

    def __init__(self, type):
        self.type = type

    def apply(self, op1, op2):
        raise NotImplementedError("Must subclass Operator")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Operator({str(self.type)})"

class OperatorLT(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op1} < {op2}")
        if not op1 < op2:
            raise ValueError


class OperatorGT(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op1} > {op2}")
        if not op1 > op2:
            raise ValueError


class OperatorRegex(Operator):
    def apply(self, op1, op2):
        print(f"Applying {op2} on {op1}")

        
        if not re.match(op2.value, op1.value):
            raise ValueError

operators = {
    "<": OperatorLT,
    ">": OperatorGT,
    "~": OperatorRegex
}