# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from linkedlist import LinkedList, insert_in_list, length, print_list
from avlbasics import (
    AVLTree,
    AVLNode,
    delete_key,
    calulate_height,
    insert_wrapper,
    search,
    subtree_height
)
# ----------------------------------------------------------------- #
# Ejercicio 1
# ----------------------------------------------------------------- #

#                         #
# Rotate left Function    #
#                         #

def rotateLeft(A, x):
    if x.rightnode:
        y = x.rightnode
        if x.parent:
            x_parent = x.parent
            if x_parent.leftnode == x:
                x_parent.leftnode = y
            else:
                x_parent.rightnode = y
            y.parent = x_parent
        else:
            A.root = y
            y.parent = None
        if y.leftnode:
            y_leftson = y.leftnode
            y_leftson.parent = x
            x.rightnode = y_leftson
        else:
            x.rightnode = None
        y.leftnode = x
        x.parent = y
        
#                         #
# Rotate right Function   #
#                         #

def rotateRight(A, y):
    if y.leftnode:
        x = y.leftnode
        if y.parent:
            y_parent = y.parent
            if y_parent.leftnode == y:
                y_parent.leftnode = x
            else:
                y_parent.rightnode = x
            x.parent = y_parent
        else:
            A.root = x
            x.parent = None
        if x.rightnode:
            x_rightson = x.rightnode
            x_rightson.parent = y
            y.leftnode = x_rightson
        else:
            y.leftnode = None
        x.rightnode = y
        y.parent = x


# ----------------------------------------------------------------- #
# Ejercicio 2
# ----------------------------------------------------------------- #

#                         #
# Balance Factor Function #
#                         #

# Description of working of this function:
#
# 1: creation of a generic function that recives the parameters needed.
# 2: wrapper function that uses the recursivity to calculate the balanceFactor:
#     a: the function always go to the left side, then go to the right
#     b: it calculate the height of the subtrees and do the operation to calculate the balanceFactor
#        bf(node) = (right subtree height - left subtree height)
#     c: the variables leftheight and rightheight are set to "0" for the correct math working
#     d: finally asign the value of the operation to the balanceFactor field of the node
#     e: that's for each node of the subtree given

def update_bf(A, alvNode):
    if alvNode:
        update_bf_wrapper(alvNode)

def update_bf_wrapper(currentNode):
    if currentNode.leftnode:
        update_bf_wrapper(currentNode.leftnode)
        leftheight = subtree_height(currentNode.leftnode)
    else:
        leftheight = -1
    if currentNode.rightnode:
        update_bf_wrapper(currentNode.rightnode)
        rightheight = subtree_height(currentNode.rightnode)
    else:
        rightheight = -1
    currentNode.balanceFactor = rightheight - leftheight

# ----------------------------------------------------------------- #
# Ejercicio 3
# ----------------------------------------------------------------- #

#                         #
# Re-Balance Function     #
#                         #

# Description of working of this function:
# 
# 1: Create a rebalance generic function that takes the parameters needed
# 2: wrapper function that uses the recursivity
#     a: the function goes to the last left node to check that all the subtrees are balanced
#     b: if all the subtrees are balanced, it apply the rotation needed to rebalance the tree
#     c: then updates the balanceFactor and heigh of the subtree gived

def reBalance(A, alvNode):
    if alvNode:
        update_bf(A, alvNode)
        reBalance_wrapper(A, alvNode)
        calulate_height(A)

def reBalance_wrapper(A, currentNode):
    if currentNode.leftnode:
        reBalance_wrapper(A, currentNode.leftnode)
    if currentNode.rightnode:
        reBalance_wrapper(A, currentNode.rightnode)

    if currentNode.balanceFactor == 2:
        if currentNode.rightnode.balanceFactor == -1:
            rotateRight(A, currentNode.rightnode)
        rotateLeft(A, currentNode)
        update_bf(A, A.root)
    elif currentNode.balanceFactor == -2:
        if currentNode.leftnode.balanceFactor == 1:
            rotateLeft(A, currentNode.leftnode)
        rotateRight(A, currentNode)
        update_bf(A, A.root)

# ----------------------------------------------------------------- #
# Ejercicio 4
# ----------------------------------------------------------------- #

#                       #
# Insert Function       #
#                       #

def avlinsert(A, element, key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if A.root != None:
        value = insert_wrapper(A, newNode, A.root)
    else:
        A.root = newNode
        value = A.root.key
    reBalance(A, A.root)
    return value

# ----------------------------------------------------------------- #
# Ejercicio 5
# ----------------------------------------------------------------- #

#                       #
# Delete Function       #
#                       #

def avldelete(A, key):
    delete_key(A.root, key)
    reBalance(A,A.root)