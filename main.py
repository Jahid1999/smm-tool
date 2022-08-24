from pycfg.pycfg import PyCFG, CFGNode, slurp
import halsted

def cfg(inputFile, outputFile):
    agruments = []

    cfg = PyCFG()
    cfg.gen_cfg(slurp(inputFile).strip())
    cfg_graph = CFGNode.to_graph(agruments)
    cfg_graph.draw(outputFile, prog='dot')

    nodes = cfg_graph.number_of_nodes()
    edges = cfg_graph.number_of_edges()
    complexity = edges - nodes + 2
    print('---------------Cyclomatic Complexity---------------')
    print("Nodes = ", nodes)
    print("Edges = ", edges)
    print("Complexity = ", complexity, "\n")

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


    print('---------------Line of Code---------------')
    print('Total Lines = ' + str(total_number_of_lines))
    print('Blank lines = ' + str(total_number_of_blank_lines))
    print('Commented lines =' + str(total_number_of_commented_lines))
    print('Executable lines = ' + str(total_number_of_lines - total_number_of_blank_lines - total_number_of_commented_lines))

if __name__ == '__main__':
    inputFile = "./test.py"
    outputFile = "cfg_output.png"
    cfg(inputFile, outputFile)
    line_of_code(inputFile)
    print('\n---------------Halstead Metric---------------')
    halsted.main(inputFile)

