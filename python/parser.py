from operators import GTOperator, LTOperator, RegexOperator, AssignOperator


def parse(rules):
    try:
        for tokens in rules:
            while tokens:
                operator = tokens.pop()
                if isinstance(operator, GTOperator):
                    op1 = tokens.pop()
                    op2 = tokens.pop()
                    operator.apply(op2, op1)
                elif isinstance(operator, LTOperator):
                    op1 = tokens.pop()
                    op2 = tokens.pop()
                    operator.apply(op2, op1)
                elif isinstance(operator, RegexOperator):
                    regex = tokens.pop()
                    op = tokens.pop()
                    operator.apply(op, regex)
                elif isinstance(operator, AssignOperator):
                    value = tokens.pop()
                    variable = tokens.pop()
                    operator.apply(variable, value)
                else:
                    raise ValueError(f"Invalid operator:{operator}")
        return True

    except ValueError as e:
        print(e)
        return False
