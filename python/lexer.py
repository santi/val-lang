from operators import operators
from tokens import Value
from utils import is_int, is_string, is_regex


def get_token(context):
    def _get_token(raw_token):
        if operator := operators.get(raw_token, False):
            return operator(raw_token)
        elif raw_token == "this":
            return context.get(raw_token)
        elif is_int(raw_token):
            return Value(int(raw_token), "int")
        elif is_string(raw_token):
            return Value(raw_token[1:-1], "str")
        elif is_regex(raw_token):
            return Value(raw_token[1:-1], "re")
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
