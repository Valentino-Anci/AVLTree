# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from avltree import (
    avldelete,
    avlinsert,
    reBalance,
    rotateLeft,
    rotateRight,
    update_bf
)

from avlbasics import (
    # Classes
    AVLTree,
    AVLNode,
    # Functions
    access,
    calulate_height,
    delete,
    insert,
    search,
    subtree_height,
    traversePostOrder,
    update
)

from helpful_functions import (
    print_avlinsert,
    print_insert,
    print_list,
    print_postorder_tree,
    print_test,
    schematic_tree_1,
    schematic_tree_2,
    schematic_tree_3,
    schematic_tree_4,
    schematic_tree_5,
    schematic_tree_6
)

from some_colors import bcolors 

# ----------------------------------------------------------------- #
# Test Tree functions
# ----------------------------------------------------------------- #

tree = AVLTree()
tree_keys = [13, 10, 9, 8, 7, 12, 11, 33, 18, 25, 24, 40]

#                       #
# Normal Insert Test    #
#                       #

print()
print_test("normal BTS Insert")
for i in range(0, len(tree_keys)):
    print_insert(i+1, tree, i+1, tree_keys[i], True)
print(f"{bcolors.HEADER}Trying to insert new node with an exsitent key:")
print_insert(13, tree, 3, 10, False)
print()
schematic_tree_1()
print_postorder_tree(tree, "key")
print()
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# Height Test           #
#                       #

print_test("subtree_height")
print(f"{bcolors.OKGREEN}   Parameters gived (tree, tree.root)")
print(f"{bcolors.OKCYAN}Height: ", subtree_height(tree.root), "\n")
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# RigthRotate Test      #
#                       #

print_test("Right Rotate")
print(f"{bcolors.OKGREEN}Trying to rotate subtree - key 9: Done!")
rotateRight(tree, tree.root.leftnode.leftnode)
print(f"{bcolors.OKCYAN}Height(10): ", subtree_height(tree.root.leftnode), "\n")
schematic_tree_2()
print_postorder_tree(tree, "key")
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# LeftRotate Test       #
#                       #

print_test("Left Rotate")
print(f"{bcolors.OKGREEN}Trying to rotate subtree - key 18: ...")
print("    In this case we have to rightrotate node: 25, and then \n    leftrotate node: 18 to have a balanced tree.")
print(f"{bcolors.OKGREEN}    Trying to rotate subtree - key 25: Done!")
rotateRight(tree, tree.root.rightnode.leftnode.rightnode)
print(f"{bcolors.OKGREEN}Trying to rotate subtree - key 18: Done!")
rotateLeft(tree, tree.root.rightnode.leftnode)
print(f"{bcolors.OKCYAN}Height(33): ", subtree_height(tree.root.rightnode), "\n")
schematic_tree_3()
print_postorder_tree(tree, "key")
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# BalanceFactor Test    #
#                       #

print_test("Update BalanceFactor")
print(f"{bcolors.OKGREEN}BalanceFactor field updated!")
update_bf(tree, tree.root)
print(f"{bcolors.OKCYAN}    Tree:")
schematic_tree_4()
print_postorder_tree(tree, "key")
print_postorder_tree(tree, "balanceFactor")
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# avlInsert Test        #
#                       #

print_test("avlInsert and reBalance")
print(f"{bcolors.OKGREEN}    For this test we have to create a new tree and insert \n    new elements...")
print("Creating Tree... Done!")
atree = AVLTree()

for i in range(0, len(tree_keys)):
    print_avlinsert(i+1, atree, i+1, tree_keys[i], True)
print(f"{bcolors.HEADER}Trying to insert new node with an exsitent key:")
print_insert(13, atree, 3, 10, False)
print()
schematic_tree_5()
print()
print_postorder_tree(atree, "key")
print_postorder_tree(atree, "balanceFactor")
print("    The tree is succesufully balanced after the insertion\n")
input(f"{bcolors.OKBLUE}Press Enter to continue...\n")

#                       #
# avlInsert Test        #
#                       #

print_test("avlDelete")
avldelete(atree, 8)
print("    Trying to delete the node key 8: Done!")
print()
schematic_tree_6()
print()
print_postorder_tree(atree, "key")
print_postorder_tree(atree, "balanceFactor")
