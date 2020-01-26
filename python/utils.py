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

