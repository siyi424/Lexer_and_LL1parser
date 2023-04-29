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
            "start": [],
            "Keyword": [],
            "Operator": [],
            "Delimiter": [],
            "Identifier": [],
            "Literals": {
                "String": [],
                "Int": [],
                "Float": [],
                "Imaginary": [],
            },
            "end": [],
        }

    def get_states(self):
        print("states: ", self.__states)

    def easy_check(self, input):
        if input in _Keywords:
            self.__states["Keyword"].append(input)
            return "Keyword"
        elif input in _Operators:
            self.__states["Operator"].append(input)
            return "Operator"
        elif input in _Delimiters:
            self.__states["Delimiter"].append(input)
            return "Delimiter"
        return False




    def __check_Identifier(self, input):
        pass

    def __check_Literals(self, input):
        pass
