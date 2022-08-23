import sys
import math
import re

operators = ["=", "+", "-", "*", "\\", "^", "\"", "\'", ".", "~", "|", "[", "]", "(", ")", ";", ":", "%", ",", "!", "<",
             ">", "&", "{", "}"]

keywords = ["function", "global", "for", "end", "while", "if", "else", "elseif", "break", "switch", "case", "otherwise",
            "try", "catch", "end", "const", "import", "export", "type", "return",
            "true", "false", "in", "abstract", "module", "continue", "do", "join"]

comment_sign = "#"
# multiline_comment_start_op = "#="
# multiline_comment_end_op = "=#"

n1 = {}
n2 = {}


def token_filtration(token):
    temp_token = token
    while temp_token:
        temp_token = break_token(temp_token)


def break_token(token):
    operator_position = len(token)
    for operator in operators:
        if token.startswith(operator):
            if operator not in n1:
                n1[operator] = 1
            else:
                n1[operator] += 1
            return token[len(operator):]
        if operator in token:
            operator_position = min(operator_position, token.find(operator))

    remaining_token = token[:operator_position]
    for keyword in keywords:
        if remaining_token == keyword:
            print(remaining_token)
            if keyword not in n2:
                n2[keyword] = 1
                print(n2)
                print("-----")
            else:
                n2[keyword] += 1

    if remaining_token not in n2:
        n2[remaining_token] = 1
    else:
        if remaining_token not in keywords:
            n2[remaining_token] += 1
            # print("***",remaining_token)

    return token[operator_position:]


def calculate_halstead_metrics(N1, N2, n1, n2):
    Vocabulary = n1 + n2
    Volume = (N1 + N2) * math.log(Vocabulary, 2)
    Difficulty = ((n1 / 2) * (N2 / n2))
    Effort = Difficulty * Volume

    print("Vocabulary: ", Vocabulary)
    print("Volume: ", Volume)
    print("Difficulty: ", Difficulty)
    print("Effort: ", Effort)


def comments_section_filtration(coded_file):
    comment_sign_position = -1
    # multiline_comment_start_operator_position = -1
    # multiline_comment_end_operator_position = -1
    filtered_lines = []
    inside_comment = False

    file = open(coded_file)
    for line in file:
        if not line.strip():
            continue
        if comment_sign in line:
            comment_sign_position = line.find(comment_sign)

        if comment_sign_position != -1:
            filtered_lines.append(line[:comment_sign_position])
        else:
            filtered_lines.append(line)

        comment_sign_position = -1

    return filtered_lines


def main(coded_file):
    lines = comments_section_filtration(coded_file)

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
            token_filtration(token)

    for key, value in n1.items():
        print(key + " = " + str(value))

    for key, value in n2.items():
        print(key + " = " + str(value))

    print("JSON of n1: ", n1)
    print("JSON of n2: ", n2)
    calculate_halstead_metrics(sum(n1.values()), sum(n2.values()), len(n1), len(n2))


if __name__ == "__main__":
    # argn = len(sys.argv)
    main("test.py")

# https://github.com/IntelLabs/HPAT.jl/blob/master/examples/queries_devel/q26/halstead-calculator.py
