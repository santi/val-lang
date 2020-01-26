from operators import operators
from tokens import Value, Variable
from utils import is_int, is_string, is_regex, is_variable


def get_token(context):
    def _get_token(raw_token):
        if operator := operators.get(raw_token, False):
            return operator(raw_token, context)
        elif reference := context.get(raw_token, False):
            return reference
        elif is_int(raw_token):
            return Value(int(raw_token), "int")
        elif is_string(raw_token):
            return Value(raw_token[1:-1], "str")
        elif is_regex(raw_token):
            return Value(raw_token[1:-1], "re")
        elif is_variable(raw_token):
            return Variable(raw_token, context)
        else:
            raise ValueError(f"Invalid grammar token: {raw_token}")
    return _get_token


def lex(grammar, context):
    rules = grammar.split(",")
    tokens = []
    for rule in rules:
        raw_tokens = rule.split(" ")
        print(f"raw_tokens: {raw_tokens}")
        tokens.append(list(map(get_token(context), raw_tokens)))
        print(f"tokens: {tokens[-1]}")
    return tokens
