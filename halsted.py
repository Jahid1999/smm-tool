import sys
import math
import re

operators = ["=", "+", "-", "*", "\\", "^", "\"", "\'", ".", "~", "|", "[", "]", "(", ")", ";", ":", "%", ",", "!", "<", ">", "&", "{", "}"]
keywords = ["function", "global", "for", "end", "while", "if", "else", "elseif", "break", "switch", "case", "otherwise", "try", "catch", "end", "const", "import", "export", "type", "return", "true", "false", "in", "abstract", "module", "continue", "do", "join"]
n1 = {}
n2 = {}

def filter_token(token):
    tok = token
    while tok:
        tok = break_token(tok)

def break_token(token):
    op_pos = len(token)
    for op in operators:
        if token.startswith(op):
            if op not in n1:
                n1[op] = 1
            else:
                n1[op] += 1
            return token[len(op):]
        if op in token:
            op_pos = min(op_pos, token.find(op))

    remaining_token = token[:op_pos]
    for keyword in keywords:
        if remaining_token == keyword:
            # print(remaining_token)
            if keyword not in n2:
                n2[keyword] = 1
                # print(n2)
                # print("-----")
            else:
                n2[keyword] += 1

    if remaining_token not in n2:
        n2[remaining_token] = 1
    else:
        if remaining_token not in keywords:
            n2[remaining_token] += 1
            # print("***",remaining_token)

    return token[op_pos:]

def measure_halstead(N1, N2, n1, n2):
    Vocabulary = n1 + n2
    Volume = (N1 + N2) * math.log(Vocabulary, 2)
    Difficulty = ((n1 / 2) * (N2 / n2))
    Effort = Difficulty * Volume

    print("Vocabulary: ", Vocabulary)
    print("Volume: ", Volume)
    print("Difficulty: ", Difficulty)
    print("Effort: ", Effort)

def filter_comments(sourcecode_file):
    singleline_comment_op_pos = -1
    filtered_lines = []

    file = open(sourcecode_file)
    for line in file:
        if not line.strip():
            continue
        if '#' in line:
            singleline_comment_op_pos = line.find('#')

        if singleline_comment_op_pos != -1:
            filtered_lines.append(line[:singleline_comment_op_pos])
        else:
            filtered_lines.append(line)

        singleline_comment_op_pos = -1

    return filtered_lines

def main(sourcecode_file):
    lines = filter_comments(sourcecode_file)

    # print("Lines of Code: ", len(lines))
    for line in lines:
        string_line = []
        if '\"' in line:
            string_line = re.findall(r'"([^"]*)"', line)
            for a in string_line:
                line = line.replace(a, '')
                line = line.replace("\"", '')
                line = line.replace("\"", '')
        tokens = line.strip().split()
        tokens = tokens + string_line
        for token in tokens:
            filter_token(token)

    print("********** Operators <n1> **********")
    for key, value in n1.items():
        print(key + " => " + str(value))

    print("********** Operands <n2> **********")
    for key, value in n2.items():
        print(key + " => " + str(value))

    print("********** **********")
    measure_halstead(sum(n1.values()), sum(n2.values()), len(n1), len(n2))
