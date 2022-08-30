import ast
import astunparse


def convert_code_file_to_ast(input_file):
    file = open(input_file)
    ast_tree = ast.parse(file.read())
    return ast_tree


def convert_ast_to_string(ast_tree):
    code = astunparse.unparse(ast.parse(ast_tree))
    return code


def convert_string_to_code_file(str_variable, num):
    python_file_writer = open(f"function_{num}.py", "w")
    python_file_writer.write(str_variable)
    python_file_writer.close()


def calculate_complexity(ast_tree):
    for_num = 0
    while_num = 0
    if_num = 0

    for n in ast.walk(ast_tree):
        if n.__class__.__name__ == "For":
            for_num += 1
        if n.__class__.__name__ == "While":
            while_num += 1
        if n.__class__.__name__ == "If":
            if_num += 1

    print("for = ", for_num)
    print("while = ", while_num)
    print("if = ", if_num)
    print("Complexity: ", for_num + while_num + if_num + 1,'\n')


def cfg(input_file):
    ast_tree = convert_code_file_to_ast(input_file)

    num = 0
    for n in ast.walk(ast_tree):
        if isinstance(n, ast.FunctionDef):
            print('function name: ', n.name)
            code_in_str = convert_ast_to_string(n)
            convert_string_to_code_file(code_in_str, num)

            tree = convert_code_file_to_ast(f"./function_{num}.py")
            calculate_complexity(tree)
            num = num + 1


if __name__ == '__main__':
    inputFile = "./test.py"
    print('---------------Complexity of all methods---------------')
    cfg(inputFile)


