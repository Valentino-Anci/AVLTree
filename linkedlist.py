# ----------------------------------------------------------------- #
# Class linkedlist
# ----------------------------------------------------------------- #

class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None

# ----------------------------------------------------------------- #
# Basic linkedlist functions
# ----------------------------------------------------------------- #

def add(L, element):
    newnode = Node()
    newnode.nextNode = L.head
    newnode.value = element
    L.head = newnode

def add_to_end(l, element):
	if l.head == None:
		add(l, element)
		return

	new_node = Node()
	new_node.value = element
	current_node = l.head 

	while current_node:
		if not current_node.nextNode: 
			current_node.nextNode = new_node
			return
		current_node = current_node.nextNode

def search(L, element):
    current = L.head
    position = 0
    while current != None:
        if element == current.value:
            return position
        current = current.nextNode
        position += 1
    return None

def insert_in_list(L, element, position):
    if position == 0:
        add(L, element)
        return 0
    elif position <= length(L):
        current = L.head
        counter = 0
        while counter < position - 1:
            current = current.nextNode
            counter += 1
        newnode = Node()
        newnode.value = element
        newnode.nextNode = current.nextNode
        current.nextNode = newnode
        return counter + 1
    else:
        print("Not inserted")
        return None

def delete_position(L, position):
    long = length(L)
    if position == 0:
        L.head = L.head.nextNode
    else:
        current = L.head
        counter = 0
        if position == long-1:
            while counter < long-2:
                counter += 1
                current = current.nextNode
            current.nextNode = None
        elif position > long-1 or position < 0:
            print("Out of range")
        else:
            while counter < position-1:
                counter += 1
                current = current.nextNode
            current.nextNode = current.nextNode.nextNode

def delete_element(L, element):
    position = search(L, element)
    if position != None:
        delete_position(L, position)
    else:
        print("Element doesn´t exist")

def length(L):
    current = L.head
    counter = 0
    while current != None:
        current = current.nextNode
        counter += 1
    return counter

def access(L, position):
    current = L.head
    counter = 0
    while current != None:
        if counter == position:
            return current.value
        counter += 1
        current = current.nextNode
    return None

def update(L, element, position):
    if position == 0:
        L.head.value = element
        return 0
    elif position <= length(L):
        current = L.head
        counter = 0
        while position > counter:
            current = current.nextNode
            counter += 1
        current.value = element
        return counter
    else:
        return None

def print_list(List):
    if List != None:
        print("[", end="")
        current = List.head
        while current != None:
            if current.nextNode != None:
                print (current.value, " ", end="")
            else:
                print (current.value, end="")
            current = current.nextNode
        print("]")
    else:
        print("ERROR: Can´t print list!")

def search_min_node(L):
    if L.head == None:
        return None
    else:
        current = L.head
        min_value = current.value
        min_node = current
        while current != None:
            if current.value < min_value:
                min_value = current.value
                min_node = current
            current = current.nextNode
        return min_node

def search_max_node(L):
    if L.head == None:
        return None
    else:
        current = L.head
        max_value = current.value
        max_node = current
        while current != None:
            if current.value > max_value:
                max_value = current.value
                max_node = current
            current = current.nextNode
        return max_node

def search_min_value(L):
    current = search_min_node(L)
    return current.value

def search_max_value(L):
    current = search_max_node(L)
    return current.value

def search_min_position(L):
    return search(L, search_min_value(L))

def search_max_position(L):
    return search(L, search_max_value(L))

def copy_list(L):
    long_node = length(L)
    newlist = LinkedList()
    temp = long_node - 1
    for i in range(0, long_node):
        current = L.head
        i = 0
        while i < temp:
            current = current.nextNode
            i += 1
        temp -= 1
        add(newlist, current.value)
    return newlist

def add_lists(firsL, secondL):
    if firsL != None and secondL != None:
        currentfirst = firsL.head
        while currentfirst.nextNode != None:
            currentfirst = currentfirst.nextNode
        currentfirst.nextNode = secondL.head
        print_list(firsL)
        return firsL

def sorted_list(L):
    current = L.head
    total = 0
    counter = 0
    while current.nextNode != None:
        if current.value < current.nextNode.value:
            total += 1
        counter += 1
        current = current.nextNode
    if total == counter:
        return True
    else: 
        return False
