import re

TransDict = {"Keyword": "k", "Operator": "o", "Identifier": "i", "Literals": "l"}


def trans2parser(tokens):
    """
    eg.
    input-tokens: ['row: 22, type: Identifier, content: c', 'row: 22, type: Delimiter, content: +', 'row: 22, type: Delimiter, content: =', 'row: 22, type: Literals_Int, content: 1']
    output: i+=l
    """
    Outputs = []
    for row in tokens:
        output = ""
        for item in row:
            # select type info
            tp = ""
            match = re.search(r"type:\s*(\w+)", item)
            if match:
                tp = match.group(1)
            # process with Literals_Int/...
            if "Literals_" in tp:
                tp = "Literals"

            # transform
            if tp in TransDict:
                tp = TransDict[tp]
                output += tp
            else:
                # type: Delimiter . , + = < , choose content as output
                match = re.search(r"content:\s*(\w+)", item)
                if match:
                    tp = match.group(1)
                    output += tp
        Outputs.append(output)
    print("Output transformed token is: ", Outputs)
    return Outputs
