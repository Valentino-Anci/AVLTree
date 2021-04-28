# ----------------------------------------------------------------- #
# Libraries
# ----------------------------------------------------------------- #

from linkedlist import LinkedList, insert_in_list, length, print_list

# ----------------------------------------------------------------- #
# Class Binay Search Tree
# ----------------------------------------------------------------- #

class BSTree:
    root = None

class BSNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None 
    value = None

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
# Insert Function       #
#                       #

def insert(A, element, key):
    newNode = BSNode()
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

#                          #
# SubTree Height Function  #
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
