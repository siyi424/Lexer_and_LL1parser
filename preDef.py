# pre-define

_Keywords = {
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "False",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "None",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "True",
    "try",
    "while",
    "with",
    "yield",
}

_Operators = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "**",
    "//",
    "==",
    "!=",
    ">",
    "<",
    ">=",
    "<=",
    "and",
    "or",
    "not",
    "is",
    "is not",
    "in",
    "not in",
}

_Delimiters = {
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "@",
    ".",
    ",",
    ":",
    ";",
    "=",
    "->",
    "+",
    "-",
    "*",
    "/",
    "//",
    "%",
    "@",
}


class DFA:
    def __init__(self) -> None:
        self.__states = {
            "start": {
                ".": "Literals_Float",
                "0": "Literals_Int",
                "1": "Literals_Int",
                "2": "Literals_Int",
                "3": "Literals_Int",
                "4": "Literals_Int",
                "5": "Literals_Int",
                "6": "Literals_Int",
                "7": "Literals_Int",
                "8": "Literals_Int",
                "9": "Literals_Int",
                '"': "Literals_String",
            },
            "Keyword": {},
            "Operator": {},
            "Delimiter": {},
            "Identifier": {},
            "Literals": {
                "String": {},
                "Int": {
                    ".": "Literals_Float",
                    "0": "Literals_Int",
                    "1": "Literals_Int",
                    "2": "Literals_Int",
                    "3": "Literals_Int",
                    "4": "Literals_Int",
                    "5": "Literals_Int",
                    "6": "Literals_Int",
                    "7": "Literals_Int",
                    "8": "Literals_Int",
                    "9": "Literals_Int",
                    "+": "Literals_Imaginary",
                    "-": "Literals_Imaginary",
                },
                "Float": {
                    "0": "Literals_Float",
                    "1": "Literals_Float",
                    "2": "Literals_Float",
                    "3": "Literals_Float",
                    "4": "Literals_Float",
                    "5": "Literals_Float",
                    "6": "Literals_Float",
                    "7": "Literals_Float",
                    "8": "Literals_Float",
                    "9": "Literals_Float",
                    "e": "Literals_Scientific",
                    "E": "Literals_Scientific",
                },
                "Imaginary": {},
                "Scientific": {},
            },
        }

    def get_states(self):
        print("states: ", self.__states)

    def easy_check(self, input):
        if input in _Keywords:
            return "Keyword"
        elif input in _Operators:
            return "Operator"
        elif input in _Delimiters:
            return "Delimiter"
        return False

    def check_Literals(self, input, p):
        current = self.__states["start"]
        type = ""
        lens = len(input)
        if input[0] not in current:
            return False

        # ":" 的处理方法！
        while p < lens:
            ch = input[p]
            type = current[ch]
            next = self.__states["Literals"][type.split("_")[1]]
            if not next:
                return type

            current = next
            p += 1

        return type

    def check_complex(self, input, row):
        # check identifier
        def check_Identifier(input, l):
            # check the first ch
            if input[0].isdigit():
                return False, 0 
                       
            isLetter = True
            isDigit = True
            isUnderscore = True
            p = l - 1

            while isLetter or isDigit or isUnderscore:
                p += 1
                if p == len(input):
                    break
                ch = input[p]
                isLetter = ch.isalpha()
                isDigit = ch.isdigit()
                isUnderscore = (ch == "_")

            if p == l:
                return False, p
            return True, p

        # check "( ) ,"
        def check_delimiter(input):
            if input in _Delimiters:
                return True

        token_complex = []
        p = l = 0
        while l < len(input):
            isIdentifier, p = check_Identifier(input, l)
            if isIdentifier:
                cont = input[l:p]
                easyCheck = self.easy_check(cont)
                if easyCheck:
                    output = "row: " + str(row) + ", type: " + easyCheck + ", content: " + cont
                else:
                    output = "row: " + str(row) +  ", type: Identifier, content: " + cont
                token_complex.append(output)

                if p == len(input):
                    break
            ch = input[p : p + 1]
            isDelimiter = check_delimiter(ch)
            if isDelimiter:
                output = "row: " + str(row) + ", type: Delimiter, content: " + ch
                token_complex.append(output)

            l = p + 1
        return token_complex[:]
