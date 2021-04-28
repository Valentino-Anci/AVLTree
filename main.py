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

# ----------------------------------------------------------------- #
# Some Nice Colors
# ----------------------------------------------------------------- #

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[31m'

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

#                       #
# Height Test           #
#                       #

print_test("subtree_height")
print(f"{bcolors.OKCYAN}Height: ", subtree_height(tree.root))

#                       #
# RRotate Test          #
#                       #

print_test("Right Rotate")
#rotateRight(tree, tree.root.leftnode.leftnode)
print(f"{bcolors.OKCYAN}Height: ", subtree_height(tree.root.leftnode))



# print("Test update function:")
# print("Updating element from key 13:\nSucceed: ", update(tree, -6, 13))
# print("Updating element from key 40:\nSucceed: ", update(tree, -6, 40))
# print("Updating element from non-existent key:\nReturned: ", update(tree, 7, 1))
# print()
# print("Test delete function:")
# print("Deleting the value 12, key 40:\nDeleted, Key: ", delete(tree, 12))
# print("Trying to delete a non-exsitent node:")
# print("Deleting the value 13:\nReturned: ", delete(tree, 13))
# print()
# print("Test height:")
# print()
# print("Test traversePostOrder function:")
# Lista = traversePostOrder(tree)
# print("Tested, List of tree elements:")
# print_list(Lista)
# print()
# print("Test traversePostOrder function:")
# reBalance(tree, tree.root)
# Lista = traversePostOrder(tree)
# print("Tested, List of balancedtree elements:")
# print_list(Lista)
# print()
# calulate_height(tree)
# update_bf(tree, tree.root)
# print("Test traversePostOrder balancefactor function:")
# Lista = traversePostOrder_balanceFactor(tree)
# print("Tested, List of tree elements:")
# print_list(Lista)
# print()
# calulate_height(tree)
# print("Test traversePostOrder heights function:")
# Lista = traversePostOrder_height(tree)
# print("Tested, List of tree elements:")
# print_list(Lista)