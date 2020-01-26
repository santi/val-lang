from operators import OperatorGT, OperatorLT, OperatorRegex


def parse(rules):
    try:
        for tokens in rules:
            while tokens:
                operator = tokens.pop()
                if isinstance(operator, OperatorGT):
                    op1 = tokens.pop()
                    op2 = tokens.pop()
                    operator.apply(op2, op1)
                elif isinstance(operator, OperatorLT):
                    op1 = tokens.pop()
                    op2 = tokens.pop()
                    operator.apply(op2, op1)
                elif isinstance(operator, OperatorRegex):
                    regex = tokens.pop()
                    op = tokens.pop()
                    operator.apply(op, regex)
                else:
                    raise ValueError("Invalid operator")
        return True
    
    except ValueError as e:
        print(e)
        return False
