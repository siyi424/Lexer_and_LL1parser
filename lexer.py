"""
input: 1. regualr grammer txt file 2. python_code txt file
output: tokens (row, indentifier, content)
"""


class lexer:
    def __init__(self, input, dfa) -> None:
        self.tokens = []
        self.input = input
        self.dfa = dfa

    def run(self):
        lines = self.input.splitlines()
        row = 1
        for line in lines:
            if not line.strip() or line.lstrip().startswith("#"):
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
            res = self.dfa.easy_check(word)
            if res:
                output = "row: " + str(row) + ", type: " + res + ", content: " + word
                token.append(output)
                continue

            # check literals
            # deal with eg. "123:"
            colon_last = False
            if word[-1] == ":":
                word = word[0:-1]
                colon_last = True
            res = self.dfa.check_Literals(word, p)
            if res:
                output = "row: " + str(row) + ", type: " + res + ", content: " + word
                token.append(output)
                if colon_last:
                    output = "row: " + str(row) + ", type: Delimiter, content: :"
                    token.append(output)
                continue

            # check identifier and complex word
            if colon_last:
                word += ":"
            token_complex = self.dfa.check_complex(word, row)
            token += token_complex

        self.tokens.append(token)
        print(token)
