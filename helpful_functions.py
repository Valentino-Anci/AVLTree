# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from some_colors import bcolors
from avlbasics import insert, traversePostOrder
from avltree import avlinsert
from linkedlist import print_list

# ----------------------------------------------------------------- #
# Other helpful functions
# ----------------------------------------------------------------- #

def print_test(name):
    print(f"{bcolors.HEADER}Test {name} function:")

def print_insert(num_element, tree, value, key, succeed):
    if succeed:
        print(f"    {bcolors.OKGREEN}Element {num_element} inserted - Key: {bcolors.OKCYAN}", insert(tree, value, key))
    else:
        print(f"    {bcolors.FAIL}Element {num_element} not-inserted - Key: ", insert(tree, value, key))


def print_avlinsert(num_element, tree, value, key, succeed):
    if succeed:
        print(f"    {bcolors.OKGREEN}Element {num_element} inserted - Key: {bcolors.OKCYAN}", avlinsert(tree, value, key))
    else:
        print(f"    {bcolors.FAIL}Element {num_element} not-inserted - Key: ", avlinsert(tree, value, key))

def schematic_tree_1():
    print(f"{bcolors.OKBLUE}                 13")
    print(R"              /       \ ")
    print("             10        33")
    print(R"           /    \    /    \ ")
    print("          9     12  18     40")
    print(R"         /      /     \ ")
    print("        8     11       25")
    print(R"       /               /")
    print("      7               24")

def schematic_tree_2():
    print(f" {bcolors.OKBLUE}             /")
    print("             10")
    print(R"           /    \ ")
    print("          8   SubTree")
    print(R"        /   \ ")
    print("       7     9")

def schematic_tree_3():
    print(Rf"{bcolors.OKBLUE}         \ ")
    print("         33")
    print(R"       /    \ ")
    print("      24    40")
    print(R"     /  \ ")
    print("    18  25")

def schematic_tree_4():
    print(f"{bcolors.OKBLUE}                 13")
    print(R"              /       \ ")
    print("             10        33")
    print(R"           /    \    /    \ ")
    print("          8     12  24    40")
    print(R"         / \    /  /  \ ")
    print("        7   9 11  18   25")

def schematic_tree_5():
    print(f"{bcolors.OKBLUE}                  18")
    print(R"               /      \ ")
    print( "             10       25")
    print(R"            /   \    /  \ ")
    print( "           8    12  24  33")
    print(R"          / \   / \       \ ")
    print( "         7   9 11 13      40")

def schematic_tree_6():
    print(f"{bcolors.OKBLUE}                  18")
    print(R"               /      \ ")
    print( "              12      25")
    print(R"            /   \    /  \ ")
    print( "           10   13  24  33")
    print(R"            \             \ ")
    print( "             11           40")

def print_postorder_tree(tree, parameter):
    print()
    print(f"{bcolors.HEADER}   TraversePostOrder Tree:")
    Lista = traversePostOrder(tree, parameter)
    if parameter == "value":
        print(f"{bcolors.OKGREEN}   List of tree values: {bcolors.OKCYAN}", end="")
    elif parameter == "key":
        print(f"{bcolors.OKGREEN}   List of tree keys: {bcolors.OKCYAN}", end="")
    elif parameter == "balanceFactor":
        print(f"{bcolors.OKGREEN}   List of tree BalanceFactor: {bcolors.OKCYAN}", end="")
    else:
        print(f"{bcolors.OKGREEN}   List of tree heights: {bcolors.OKCYAN}", end="")
    print_list(Lista)
    print()