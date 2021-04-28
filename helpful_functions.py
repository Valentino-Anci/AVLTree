# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from some_colors import bcolors
from avltree import insert

# ----------------------------------------------------------------- #
# Other helpful functions
# ----------------------------------------------------------------- #

def print_test(name):
    print(f"{bcolors.HEADER}Test {name} function:")

def print_insert(num_element, tree, value, key, color, succeed):
    if succeed:
        print(f"    {color}Element {num_element} inserted - Key: ", insert(tree, value, key))
    else:
        print(f"    {color}Element {num_element} not-inserted - Key: ", insert(tree, value, key))

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
