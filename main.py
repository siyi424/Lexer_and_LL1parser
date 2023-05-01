from lexer import lexer
from preDef import DFA
from LL1_parser import LL1_parser

if __name__ == "__main__":
    txt_cont = ""
    with open("./test/test_code.txt", "r") as f:
        txt_cont = f.read()

    my_DFA = DFA()
    my_lexer = lexer(txt_cont, my_DFA)
    my_lexer.run()

    path = "./test/test_grammer.txt"
    my_parser = LL1_parser(path)