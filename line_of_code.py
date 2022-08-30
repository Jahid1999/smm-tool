
def line_of_code(inputFile):
    total_number_of_lines = 0
    total_number_of_blank_lines = 0
    total_number_of_commented_lines = 0

    f = open(inputFile)
    for line in f:
        total_number_of_lines += 1

        line_without_white_space = line.strip()
        if not line_without_white_space:
            total_number_of_blank_lines += 1
        elif line_without_white_space.startswith('#'):
            total_number_of_commented_lines += 1

    f.close()

    print('---------------Line of Code---------------')
    print('Total Lines = ' + str(total_number_of_lines))
    print('Blank lines = ' + str(total_number_of_blank_lines))
    print('Commented lines =' + str(total_number_of_commented_lines))
    print('Executable lines = ' + str(total_number_of_lines - total_number_of_blank_lines - total_number_of_commented_lines))


if __name__ == '__main__':
    inputFile = "./test.py"
    line_of_code(inputFile)


# def cfg_raw(inputFile):
#     file = open(inputFile)
#     ast_tree = ast.parse(file.read())
#
#     # exec(compile(ast_tree, filename="", mode="exec"))
#     # print(ast.dump(ast_tree, indent=2))
#
#     forNum = 0
#     whileNum = 0
#     ifNum = 0
#
#     for n in ast.walk(ast_tree):
#         if n.__class__.__name__ == "For":
#             forNum += 1
#         if n.__class__.__name__ == "While":
#             whileNum += 1
#         if n.__class__.__name__ == "If":
#             ifNum += 1
#
#     print("Fors", forNum)
#     print("Whiles", whileNum)
#     print("Ifs", ifNum)
#     print("Complexity: ", forNum+whileNum+ifNum+1)

