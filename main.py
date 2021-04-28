# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from avltree import (
    
    # Classes
    AVLTree,
    AVLNode,
    
    # Functions
    access,
    calulate_height,
    delete,
    insert,
    reBalance,
    rotateLeft,
    rotateRight,
    search,
    subtree_height,
    traversePostOrder,
    update,
    update_bf
)

from linkedlist import print_list

from helpful_functions import *

from some_colors import bcolors 

# ----------------------------------------------------------------- #
# Test Tree functions
# ----------------------------------------------------------------- #

tree = AVLTree()

#                       #
# Insert Test           #
#                       #

print_test("insert")
tree_keys = [13, 10, 9, 8, 7, 12, 11, 33, 18, 25, 24, 40]
for i in range(0, len(tree_keys)):
    print_insert(i+1, tree, i+1, tree_keys[i], bcolors.OKGREEN, True)
print(f"{bcolors.HEADER}Trying to insert new node with an exsitent key:")
print_insert(13, tree, 3, 10, bcolors.FAIL, False)
print()
schematic_tree_1()
print()

#                       #
# Height Test           #
#                       #

print_test("subtree_height")
print(f"{bcolors.OKCYAN}Height: ", subtree_height(tree.root), "\n")

#                       #
# RigthRotate Test      #
#                       #

print_test("Right Rotate")
print(f"{bcolors.OKGREEN}Trying to rotate subtree - key 9: Done")
rotateRight(tree, tree.root.leftnode.leftnode)
print(f"{bcolors.OKCYAN}Height: ", subtree_height(tree.root.leftnode), "\n")
schematic_tree_2()
print()
