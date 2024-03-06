# Data Structures & Algorithms Project
# Types of Data Structures and their Implementations
# Stacks, Queues, Linked Lists, Trees
print("Project on Implementation of various kinds of data structures: ")
while True:
    print("Select one of the following data structures to implement: ")
    print("1. Stacks\n2. Queues\n3. Linked Lists\n4. Trees\n5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Stack implementation: ")
        print("A Stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle.\nA stack can be defined as a container in which insertion and deletion can be done from the one end known as the top of the stack.")
        stack = []
        while True:
            print("Select one of the following operations that can be performed on the stack: ")
            print("1. Push Operation\n2. Pop Operation\n3. Peek Operation\n4. IsEmpty Operation\n5. Display\n6. Application\n7. Exit\n")
            
            option = int(input("Select your choice: "))

            if option == 1:
                element = int(input("Enter the element to push into stack: "))
                stack.append(element)
        
            if option == 2:
                if stack:
                    pop_element = stack.pop()
                    print("Popped element: ", pop_element)
                else:
                    print("Stack is empty to pop elements.")
            
            if option == 3:
                if stack:
                    peek_element = stack[-1]
                    print("Peek (or) Top element: ", peek_element)
                else:
                    print("Stack is empty.")
            
            if option == 4:
                if len(stack) == 0:
                    print("Stack is empty.")
                else:
                    print("Stack is not empty, size of stack = ", len(stack))
            
            if option == 5:
                print("Stack: ")
                for ele in stack[::-1]:
                    print(ele)

            if option == 6:
                print("Some of the applications of stacks are as follows: ")
                print("Evaluation of Arithematic Expressions\nBacktracking\nReverse a Data\nProcessing Function calls\n")
                
            if option == 7:
                print("Stack implementation program terminated.")
                break
    if choice == 2:
        print("Queue data structure implementation: ")
        while True:
            
            print("Select the type of queue to implement: ")
            print("1. Linear queue\n2. Circular Queue\n3. Double-ended Queue\n4. Exit")

            option1 = int(input("Enter your choice: "))

            if option1 == 1:
                lqueue = []
                while True:
                    print("Select one of the following operations that can be performed on the stack: ")
                    print("1. Enque Operation\n2. Deque Operation\n3. Peek Operation\n4. IsEmpty Operation\n5. Display\n6. Application\n7. Exit\n")

                    option2 = int(input("Select your choice: "))

                    if option2 == 1:
                        element = int(input("Enter the element to push into the queue: "))
                        lqueue.append(element)
                    if option2 == 2:
                        if len(lqueue) > 0:
                            lqueue.pop(0)
                        else:
                            print("Queue is empty.")
                    if option2 == 3:
                        if len(lqueue) > 0:
                            print("Front element of queue: ", lqueue[0])
                        else:
                            print("Queue is empty.")
                    if option2 == 4:
                        if len(lqueue) == 0:
                            print("Empty queue")
                        else:
                            print("Non-empty queue")
                            print(lqueue)
                    if option2 == 5:
                        print(lqueue)
                    if option2 == 6:
                        print("Some applications of queue data structure are as follows: ")
                        print("1. Queues are used in Breadth-first search backtracking algorithm.\n2. Queues are used in CPU Scheduling.\n3. Queues are used in Memory management.")
                    if option2 == 7:
                        print("Linear queue implementation terminated.")
                        break

            if option1 == 2:
                size = int(input("Enter the size for the Circular queue: "))
                cqueue = [None] * size
                front = rear = -1
                while True:
                    
                    print("Select one of the following operations to perform on the circular queue:")
                    print("1. Enqueue\n2. Dequeue\n3. Empty operation\n4. IsFull operation\n5. Display\n6. Exit")
                    option3 = int(input("Enter your choice: "))

                    if option3 == 1:
                        value = int(input("Enter the element to push into the queue: "))
                        if (rear + 1) % size == front:
                            print("Circular queue is full.")
                        elif front == -1 and rear == -1:
                            front = rear = 0
                        else:
                            rear = (rear + 1) % size
                        cqueue[rear] = value
                    
                    if option3 == 2:
                        if front == -1 and rear == -1:
                            print("Queue is empty.")
                        elif front == rear:
                            print("Dequeued element:", cqueue[front])
                            front = rear = -1
                        else:
                            print("Dequeued element:", cqueue[front])
                            front = (front + 1) % size
                    
                    if option3 == 3:
                        if front == -1 and rear == -1:
                            print("Queue is empty.")
                        else:
                            print("Queue is not empty.")
                    if option3 == 4:
                        if (rear + 1) % size == front:
                            print("Circular queue is full.")
                        else:
                            print("Circular queue is not full.")
                    if option3 == 5:
                        print(cqueue)
                    if option3 == 6:
                        print("Circular Queue implementation terminated.")
                        break
            
            if option1 == 3:
                deque = []
                while True:
                    print("Select any of the following operations to perform on Double-ended queue: ")
                    print("1. Delete-front\n2. Delete-rear\n3. Push-front\n4. Push-rear\n5. Empty operation\n6. Display\n7. Exit")
                    option4 = int(input("Enter the option: "))

                    if option4 == 1:
                        if deque:
                            deque.pop(0)
                        print("Double-ended queue empty.")
                    if option4 == 2:
                        if deque:
                            deque.pop()
                        print("Double-ended queue empty.")
                    if option4 == 3:
                        item = int(input("Enter the element to push: "))
                        deque.insert(0, item)
                    if option4 == 4:
                        item1 = int(input("Enter the element to push: "))
                        deque.append(item1)
                    if option4 == 5:
                        if len(deque) == 0:
                            print("Double-ended queue is empty.")
                        else:
                            print("Double-ended queue is not empty.")
                    if option4 == 6:
                        print("Double-ended queue:", deque)
                    if option4 == 7:
                        print("Double-ended queue implementation terminated.")
                        break

            if option1 == 4:
                print("Queues data structure implementation terminated.")
                break 
    
    if choice == 3:
        print("Linked list implementation: ")
        while True:
            print("Select the type of Linked list to implement: ")
            print("1. Singly Linked list\n2. Doubly-Linked list\n3. Circular Linked list\n4. Exit")
            
            option5 = int(input("Enter the option: "))
            if option5 == 1:
                print("Single Linked list implementation: ")
                class Node:
                    def __init__(self, data):
                        self.data = data
                        self.next = None
                class Linkedlist:
                    def __init__(self):
                        self.head = None
                    def insertion_end(self, element):
                        new_node = Node(element)
                        if self.head == None:
                            self.head = new_node
                        else:
                            temp = self.head
                            while temp.next != None:
                                temp = temp.next
                            temp.next = new_node
                    def deletion_end(self):
                        if self.head == None:
                            print("Deletion from empty linked list not possible.")
                        elif self.head.next == None:
                            self.head = None
                        else:
                            temp = self.head
                            while temp.next.next != None:
                                temp = temp.next
                            temp.next = None
                    def size(self):
                        count = 0
                        temp = self.head
                        while temp != None:
                            temp = temp.next
                            count += 1
                        return count
                    def traversal(self):
                        temp = self.head
                        while temp!= None:
                            print(temp.data, end = " -> ")
                            temp = temp.next
                        print()
                ll = Linkedlist()
                while True:
                    print("Select the linked list operation to perform: ")
                    print("1. Insertion operation\n2. Deletion operation\n3. Traversal\n4. size\n5. Exit")
                    option6 = int(input("Enter the choice: "))
                    if option6 == 1:
                        e = int(input("Enter the value to insert into linked list: "))
                        ll.insertion_end(e)
                    if option6 == 2:
                        ll.deletion_end()
                    if option6 == 3:
                        ll.traversal()
                    if option6 == 4:
                        print("Size: ", ll.size())
                    if option6 == 5:
                        print("Singly linked list implementation terminated.")
                        break
            
            if option5 == 2:
                print("Double Linked list implementation: ")
                class dNode:
                    def __init__(self, data):
                        self.data = data
                        self.prev = None
                        self.next = None
                class DoubleLinkedList:
                    def __init__(self):
                        self.head = None
                    def insertion_end(self, ele):
                        new_node = dNode(ele)
                        if self.head is None:
                            self.head = new_node
                        else:
                            temp = self.head
                            while temp.next:
                                temp = temp.next
                            temp.next = new_node
                            new_node.prev = temp
                    def delete_end(self):
                        if self.head is None:
                            print("Double linked list is empty can't delete. ")
                        if self.head.next is None:
                            self.head = None
                            return
                        curr = self.head
                        while curr.next:
                            curr = curr.next
                        curr.prev.next = None
                    def traversal(self):
                        if self.head is None:
                            print("Double linked list empty.")
                        else:
                            curr = self.head
                            while curr:
                                print(curr.data, end = " <-> ")
                                curr = curr.next
                            print()
                    def size(self):
                        count = 0
                        if self.head is None:
                            print("Double linked list empty. Size = 0")
                        else:
                            curr = self.head
                            while curr:
                                count += 1
                                curr = curr.next
                            return count
                dll = DoubleLinkedList()
                while True:
                    print("Select the double linked list operation to perform: ")
                    print("1. Insertion operation\n2. Deletion operation\n3. Traversal\n4. size\n5. Exit")
                    option7 = int(input("Enter the option to perform the operation: "))
                    if option7 == 1:
                        variable = int(input("Enter the element to append into Double-Linked List: "))
                        dll.insertion_end(variable)
                    if option7 == 2:
                        dll.delete_end()
                    if option7 == 3:
                        dll.traversal()
                    if option7 == 4:
                        print("Size: ", dll.size())
                    if option7 == 5:
                        print("Doubly linked list implementation terminated.")
                        break
            
            if option5 == 3:
                print("Circular Linked list implementation: ")
                class cNode:
                    def __init__(self, data):
                        self.data = data
                        self.next = None
                class CircularLinkedList:
                    def __init__(self):
                        self.head = None
                    def insert_end(self, element):
                        new_node = cNode(element)
                        if not self.head:
                            self.head = new_node
                            new_node.next = self.head
                        else:
                            curr = self.head
                            while curr.next != self.head:
                                curr = curr.next
                            curr.next = new_node
                            new_node.next = self.head
                    def insert_front(self, element):
                        new_node = cNode(element)
                        if not self.head:
                            self.head = new_node
                            new_node.next = self.head
                        else:
                            new_node.next = self.head
                            curr = self.head
                            while curr.next != self.head:
                                curr = curr.next
                            curr.next = new_node
                            self.head = new_node
                    def delete_end(self):
                        if self.head is None:
                            print("Circular linked list empty.")
                        elif self.head.next == self.head:
                            self.head = None
                        else:
                            curr = self.head
                            while curr.next.next != self.head:
                                curr = curr.next
                            curr.next = self.head
                    def count(self):
                        count = 0
                        curr = self.head
                        while curr.next != self.head:
                            count += 1
                            curr = curr.next
                        return count
                    def traversal(self):
                        if not self.head:
                            print("Circular linked list empty.")
                            return
                        curr = self.head
                        while True:
                            print(curr.data, end = " - ")
                            curr = curr.next
                            if curr == self.head:
                                break
                        print()
                    def is_circular(self):
                        if self.head is None:
                            return False
                        slow = self.head
                        fast = self.head.next
                        while fast is not None and fast.next is not None:
                            if slow == fast:
                                return True
                            slow = slow.next
                            fast = fast.next.next
                        return False

                cll = CircularLinkedList()
                while True:
                    print("Select one of the following operations to perform: ")
                    print("1. Insert-end operation\n2. Insert-front operation\n3. delete-end operation\n4. Size\n5. Display operation\n6. Verify Circular or not\n7. Exit")
                    option8 = int(input("Enter the option: "))
                    if option8 == 1:
                        e = int(input("Enter the element to insert in the circular linked list: "))
                        cll.insert_end(e)
                    if option8 == 2:
                        r = int(input("Enter the element to insert in front of circular linked list: "))
                        cll.insert_front(r)
                    if option8 == 3:
                        cll.delete_end()
                    if option8 == 4:
                        print("Size of circular linked list: ", cll.size())
                    if option8 == 5:
                        cll.traversal()
                    if option8 == 6:
                        print("Is it Circular Linked List: ", cll.is_circular())
                    if option8 == 7:
                        print("Circular linked list implementation terminated.")
                        break 

            if option5 == 4:
                print("Linked lists data structure implementation terminated.")
                break
    
    if choice == 4:
        print("Trees data structure implementation: ")
        while True:
            print("Select the type of Tree to implement: ")
            print("1. Binary Search Tree\n2. AVL Tree\n3. Exit")

            tree_choice = int(input("Enter your choice: "))

            if tree_choice == 1:
                print("Binary-search Tree implementation: ")
                class TreeNode:
                    def __init__(self, data):
                        self.data = data
                        self.left = None
                        self.right = None
                class BinarySearchTree:
                    def __init__(self, root):
                        self.root = TreeNode(root)
                    def insertion(self, data, root = None):
                        if root is None:
                            root = self.root
                        if data <= root.data:
                            if root.left is None:
                                root.left = TreeNode(data)
                            else:
                                self.insertion(data, root.left)
                        if data > root.data:
                            if root.right is None:
                                root.right = TreeNode(data)
                            else:
                                self.insertion(data, root.right)
                    def search(self, root, key):
                        if root is None or root.data == key:
                            return root
                        else:
                            if key > root.data:
                                return self.search(root.right, key)
                            if key < root.data:
                                return self.search(root.left, key)
                    def pre_order_traversal(self, node = None):
                        if node == None:
                            node = self.root
                        print(node.data, end = " ")
                        if node.left:
                            self.pre_order_traversal(node.left)
                        if node.right:
                            self.pre_order_traversal(node.right)
                    def in_order_traversal(self, node = None):
                        if node == None:
                            node = self.root
                        if node.left:
                            self.in_order_traversal(node.left)
                        print(node.data, end = " ")
                        if node.right:
                            self.in_order_traversal(node.right)
                    def post_order_traversal(self, node = None):
                        if node == None:
                            node = self.root
                        if node.left:
                            self.post_order_traversal(node.left)
                        if node.right:
                            self.post_order_traversal(node.right)
                        print(node.data, end = " ")
                root = int(input("Enter root value for the Binary-search tree: "))
                bst = BinarySearchTree(root)
                while True:
                    print("Select one of the following operations to perform on the Binary-search tree: ")
                    print("1.insertion\n2. search opertion\n3. Pre-Order traversal\n4. In-Order traversal\n5. Post-Order traversal\n6. Exit")
                    option9 = int(input("Enter your choice: "))
                    if option9 == 1:
                        ele = int(input("Enter the node to push into the Binary-search tree: "))
                        bst.insertion(ele)
                    if option9 == 2:
                        key = int(input("Enter the key value to search in Binary-search tree: "))
                        result = bst.search(bst.root, key)
                        if result:
                            print("Key found: ", result)
                        else:
                            print("Key Not Found.")
                    if option9 == 3:
                        print("Pre-Order Traversal: ") 
                        bst.pre_order_traversal()
                        print()
                    if option9 == 4:
                        print("In-Order Traversal: ") 
                        bst.in_order_traversal()
                        print()
                    if option9 == 5:
                        print("Post-Order Traversal: ") 
                        bst.post_order_traversal()
                        print()
                    if option9 == 6:
                        print("Binary search tree implementation terminated.")
                        break

            if tree_choice == 2:
                print("AVL Tree implementation: ")
                class AVLNode:
                    def __init__(self, key):
                        self.key = key
                        self.left = None
                        self.right = None
                        self.height = 1

                class AVLTree:
                    def __init__(self):
                        self.root = None

                    def getHeight(self, node):
                        if not node:
                            return 0
                        return node.height

                    def getBalance(self, node):
                        if not node:
                            return 0
                        return self.getHeight(node.left) - self.getHeight(node.right)

                    def rotateRight(self, y):
                        x = y.left
                        T2 = x.right

                        x.right = y
                        y.left = T2

                        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
                        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
                        return x

                    def rotateLeft(self, x):
                        y = x.right
                        T2 = y.left

                        y.left = x
                        x.right = T2

                        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
                        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
                        return y

                    def insert(self, key):
                        self.root = self._insert(self.root, key)

                    def _insert(self, root, key):
                        if not root:
                            return AVLNode(key)
                        elif key < root.key:
                            root.left = self._insert(root.left, key)
                        else:
                            root.right = self._insert(root.right, key)

                        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
                        balance = self.getBalance(root)

                        if balance > 1:
                            if key < root.left.key:
                                return self.rotateRight(root)
                            else:
                                root.left = self.rotateLeft(root.left)
                                return self.rotateRight(root)

                        if balance < -1:
                            if key > root.right.key:
                                return self.rotateLeft(root)
                            else:
                                root.right = self.rotateRight(root.right)
                                return self.rotateLeft(root)
                        return root

                    def preorder(self, root):
                        if root:
                            print(root.key, end=' ')
                            self.preorder(root.left)
                            self.preorder(root.right)
                avl_tree = AVLTree()
                while True:
                    print("Select one of the following operations that can be performed on the AVL Tree: ")
                    print("1. Insert\n2. Preorder Traversal\n3. Exit")

                    avl_option = int(input("Select your choice: "))

                    if avl_option == 1:
                        key = int(input("Enter the key to insert into AVL Tree: "))
                        avl_tree.insert(key)
                    if avl_option == 2:
                        print("Preorder Traversal of AVL Tree:")
                        avl_tree.preorder(avl_tree.root)
                        print()
                    if avl_option == 3:
                        print("AVL Tree implementation terminated.")
                        break

            if tree_choice == 3:
                print("Trees data structure implementation terminated.")
                break

    if choice == 5:
        print("Program terminated.")
        break