import re

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_string(string):
    return re.match("'.*'", string)

def is_regex(string):
    return re.match("/.*/", string)

def is_variable(string):
    return re.match("[a-zA-Z]+[a-zA-Z0-9]*", string)

def print_context(context):
    print(context)