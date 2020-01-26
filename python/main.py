from parser import parse
from tokens import Field
from lexer import lex



def main():
    grammar = "x 3 =,'hello' /hell/ ~,4 6 <,8 5 >,this 6 <,x 4 <"

    #grammar = "x 5 ="
    context = {
        "this": Field(4, "int")
    }


    print("-" * 5 + " Lex " + "-" * 5)
    tokens = lex(grammar, context)
    print("-" * 5 + " Parse " + "-" * 5)
    result = parse(tokens)
    print("-" * 5 + " Result " + "-" * 5)
    print(f"context: {context}")
    print(f"result: {result}")



if __name__ == "__main__":
    main()