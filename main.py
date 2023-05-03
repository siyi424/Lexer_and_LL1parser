from lexer import lexer
from preDef import DFA
from LL1_parser import LL1_parser
from lex2parser import trans2parser

if __name__ == "__main__":
    txt_cont = ""
    with open("./test/test_code.txt", "r") as f:
        txt_cont = f.read()
    
    # DFA
    my_DFA = DFA()
    my_lexer = lexer(txt_cont, my_DFA)
    tokens = my_lexer.run()

    # parser LL1
    path = "./test/test_grammer.txt"
    my_parser = LL1_parser(path)
    my_parser.run()

    # analyze
    input = trans2parser(tokens)
    for row in input:
        print("token: ", row)
        my_parser.analyze(row)
        print("------------------------------")