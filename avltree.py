# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from linkedlist import LinkedList, insert_in_list, length, print_list

# ----------------------------------------------------------------- #
# Class AVLTree
# ----------------------------------------------------------------- #

class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None 
    value = None
    balanceFactor = None
    height = None

# ----------------------------------------------------------------- #
# AVL Basic Functions
# ----------------------------------------------------------------- #

#                       #
# Access Function       #
#                       #

def access(A, key):
    if (key != None) and not(A.root == None):
        return access_wrapper(A.root, key)

def access_wrapper(currentNode, key):
    if currentNode.key == key:
        return currentNode.value
    elif currentNode.key > key:
        if currentNode.leftnode != None:
            return access_wrapper(currentNode.leftnode, key)
    elif currentNode.key < key: 
        if currentNode.rightnode != None:
            return access_wrapper(currentNode.rightnode, key)
    else: 
        return None

#                       #
# Delete Function       #
#                       #

def delete(A, element):
    key = search(A, element)
    if key != None:
        delete_key(A.root, key)
    return key

def delete_key(currentNode, key):
    if currentNode.key > key:
        if currentNode.leftnode != None:
            if currentNode.leftnode.key == key:
                currentNode.leftnode = None
            else:
                delete_key(currentNode.leftnode, key)
    elif currentNode.key < key:
        if currentNode.rightnode != None:
            if currentNode.rightnode.key == key:
                currentNode.rightnode = None
            else:
                delete_key(currentNode.rightnode, key)

#                       #
# Height Functions      #
#                       #

def calulate_height(ATree):
    if ATree.root:
        i = 0
        height_wrapper(ATree.root, i)

def height_wrapper(currentNode, i):
    currentNode.height = i
    if currentNode.leftnode:
        height_wrapper(currentNode.leftnode, i+1)
    if currentNode.rightnode:
        height_wrapper(currentNode.rightnode, i+1)

#                          #
# Height of Node Functions #
#                          #

def subtree_height(ANode):
    if ANode:
        if ANode.leftnode or ANode.rightnode:
            return subheight_wrapper(ANode, 0, 0)
        else:
            return 0
        
def subheight_wrapper(currentNode, i, tree_height):
    if currentNode.leftnode:
        tree_height = subheight_wrapper(currentNode.leftnode, i+1, tree_height)
    if currentNode.rightnode:
        tree_height = subheight_wrapper(currentNode.rightnode, i+1, tree_height)
        
    if i > (tree_height):
        tree_height = i
    return tree_height

#                       #
# Insert Function       #
#                       #

def insert(A, element, key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if A.root != None:
        value = insert_wrapper(A, newNode, A.root)
        return value
    else:
        A.root = newNode
        return A.root.key

def insert_wrapper(A, newNode, currentNode):
    if newNode.key > currentNode.key:
        if currentNode.rightnode == None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            return insert_wrapper(A, newNode, currentNode.rightnode)
    elif newNode.key < currentNode.key:
        if currentNode.leftnode == None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            return insert_wrapper(A, newNode, currentNode.leftnode)
    else:
        return None

#                       #
# Search Function       #
#                       #

def search(A, element):
    if A.root != None:
        key = search_wrapper(A.root, element)
        return key
    else:
        return None

def search_wrapper(Node, element):
    if Node != None:
        if Node.value == element:
            return Node.key
        else:
            result = search_wrapper(Node.leftnode, element)
            if result != None:
                return result
            result = search_wrapper(Node.rightnode, element)
            if result != None:
                return result
    else:
        return None


#                       #
# Traverse in-order     #
#                       #

def traverseInOrder(A):
    List = None
    if A.root:
        List = LinkedList()
        traverseInOrderR(A.root, List)
    return List

def traverseInOrderR(currentNode, List):
    if currentNode != None:
        traverseInOrderR(currentNode.leftnode, List)
        insert_in_list(List, currentNode.key, length(List))
        traverseInOrderR(currentNode.rightnode, List)
    else:
        return None

#                       #
# Traverse post-order   #
#                       #

def traversePostOrder(A, field_you_want_to_print):
    List = None
    if A.root: 
        List = LinkedList()
        if (
            field_you_want_to_print != "value" and
            field_you_want_to_print != "key" and
            field_you_want_to_print != "balanceFactor" and
            field_you_want_to_print != "hegiht"
        ):
            print("     The field you want to print is invalid, key field'll be printed")
        traversePostOrderR(A.root, List, field_you_want_to_print)
        
    return List

def traversePostOrderR(currentNode, List, field_you_want_to_print):
    if currentNode:
        if field_you_want_to_print == "value":
            insert_in_list(List, currentNode.value , length(List))
        elif field_you_want_to_print == "balanceFactor":
            insert_in_list(List, currentNode.balanceFactor , length(List))
        elif field_you_want_to_print == "height":
            insert_in_list(List, currentNode.height , length(List))
        else:
            insert_in_list(List, currentNode.key , length(List))
        traversePostOrderR(currentNode.leftnode, List, field_you_want_to_print)
        traversePostOrderR(currentNode.rightnode, List, field_you_want_to_print)
    else:
        return None

#                       #
# Update Function       #
#                       #

def update(A, element, key):
    if not(A.root == None) and (key != None):
        return update_wrapper(A.root, key, element)
    
    
def update_wrapper(currentNode, key, element):
    if currentNode.key == key:
        currentNode.value = element
        return currentNode.key
    elif currentNode.key > key:
        if currentNode.leftnode != None:
            return update_wrapper(currentNode.leftnode, key, element)
    elif currentNode.key < key: 
        if currentNode.rightnode != None:
            return update_wrapper(currentNode.rightnode, key, element)
    else: 
        return None


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
        print("Node: ", currentNode.leftnode.key)    
        update_bf_wrapper(currentNode.leftnode)
        leftheight = subtree_height(currentNode.leftnode)
    else:
        leftheight = 0

    if currentNode.rightnode != None:
        print("Node: ", currentNode.rightnode.key)
        update_bf_wrapper(currentNode.rightnode)
        rightheight = subtree_height(currentNode.rightnode)
    else:
        rightheight = 0
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
        print("In node: ", currentNode.leftnode.key)
        reBalance_wrapper(A, currentNode.leftnode)
    if currentNode.rightnode:
        print("In node: ", currentNode.rightnode.key)
        reBalance_wrapper(A, currentNode.rightnode)

    if currentNode.balanceFactor > 1:
        print("rotating: ", currentNode.key)
        rotateLeft(A, currentNode)
        update_bf(A, A.root)
    elif currentNode.balanceFactor < -1:
        print("rotating: ", currentNode.key)
        rotateRight(A, currentNode)
        update_bf(A, A.root)

# ----------------------------------------------------------------- #
# Ejercicio 4
# ----------------------------------------------------------------- #




# ----------------------------------------------------------------- #
# Ejercicio 5
# ----------------------------------------------------------------- #

