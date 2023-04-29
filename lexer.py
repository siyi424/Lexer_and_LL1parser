"""
input: 1. regualr grammer txt file 2. python_code txt file
output: tokens (row, indentifier, content)
"""
from preDef import DFA


class lexer:
    def __init__(self, input) -> None:
        self.tokens = []
        self.input = input

    def run(self):
        lines = self.input.splitlines()
        row = 0
        for line in lines:
            if line == []:
                row += 1
                continue

            self.__step(line, row)
            row += 1

    def __step(self, line, row):
        words = line.split()
        token = []

        p = 0
        for word in words:
            # easy pre-check
            res = my_DFA.easy_check(word)
            if res:
                output = "row: " + str(row) + ", type: " + res + ", content: " + word
                token.append(output)
                continue

            # specific check

        self.tokens.append(token)


if __name__ == "__main__":
    txt_cont = ""
    with open("./test/test_code.txt", "r") as f:
        txt_cont = f.read()

    my_DFA = DFA()
    my_lexer = lexer(txt_cont)
    my_lexer.run()
