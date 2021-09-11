# all nodes onthe left subtree are smaller than the root node
# all the nodes on the right subtree are greatert thean the root node
# both the subtree follow the the above properties

#  TIme complexity of searching --> OLog n

# create node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegi(self, data):
        node = Node(data, self.head)
        # we create a new element and the next value will be current head
        # and then we can change it to the curretn element like this:
        self.head = node

    def insertAtEnd(self, data):
        # checking if linked list is empty
        if self.head is None:

            # if empty assign the value to head of the linked list
            self.head = Node(data, None)
            return

        # if not empty traverse throught the linked list
        itr = self.head
        while itr.next:
            itr = itr.next

        # when we reach at the last element add the data
        itr.next = Node(data, None)

    def print(self):
        abc = []
        # checking if linked list is empty
        if self.head == None:
            return "Linked List is empty"

        # start bthe iteration from the first element
        itr = self.head
        llstr = ''

        # traverset through the linked list and adding each
        # eleemt to the string for printing
        while itr:
            abc.append(itr.data)
            llstr += str(itr.data)+'-->'
            itr = itr.next
        return abc
        # print(llstr)  # priting the linked list

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def get_length(self):
        c = 0
        itr = self.head
        while itr:
            c = c+1
            itr = itr.next
        return c

    def remoive_at(self, index):
        # checking the index to be valid
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        # if we have to remove head
        if index == 0:
            # point the head pointer to the next value in the linked list
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:

            # we have to stop one place before the index we are finding to remove that
            if count == index-1:
                # the next link(which is to be removed)should point to the link after that
                itr.next = itr.next.next
                break
            # after doing that break out of hte loop
            itr = itr.next
            count = count+1

    def insert_at(self, index, data):
        # checking the index to be valid
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        # if we have to insertt at the begginning
        if index == 0:
            self.insertAtBegi(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return
        count = 1
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count, data_to_insert)
                return
            itr = itr.next
            count = count+1

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def remove_duplicates(self):
        if self.head is None:
            return

        itr = self.head

        while itr.next:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else:
                itr = itr.next

    def remove_duplicates2(self):
        itr = self.head
        s = []
        while itr:
            s.append(itr.data)
            itr = itr.next
        return self.insert_values(set(s))

    def get_middle(self):
        # intialzie two pointers
        slow = self.head
        fast = self.head
        # the slow pointer moves one at time while the fastt moves two at a time
        # when the fast pointer will be at the end the slow one will be at the middle of the linked list
        while fast.next and fast.next.next:
            # the if block modification is done for the reverse funtion
            # to return the middle of a linke dlist normally just comment it
            # if fast == self.head:
            #     fast = fast.next.next
            # else:
            slow = slow.next
            fast = fast.next.next

        return slow
        # print("THe middle element is", slow.data)

    def delete_middle(self):
        # intialzie two pointers
        slow = self.head
        fast = self.head
        prev = self.head
        # the slow pointer moves one at time while the fastt moves two at a time
        # when the fast pointer will be at the end the slow one will be at the middle of the linked list
        while slow.next and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next

    def count_int(self, target):
        count = 0
        itr = self.head
        while itr:
            if itr.data == target:
                count = count+1
            itr = itr.next
        return count

    def swap_nodes(self, x, y):
        if x == y:
            return

        x_point = None
        y_point = None

        itr = self.head
        while itr.next:
            if itr.next.data == x:
                x_point = itr
            elif itr.next.data == y:
                y_point = itr
            itr = itr.next
        # if we have found both a and b
        # in the linked list swap current
        # pointer and next pointer of these
        if x_point != None and y_point != None:

            temp = x_point.next
            x_point.next = y_point.next
            y_point.next = temp

            temp = x_point.next.next
            x_point.next.next = y_point.next.next
            y_point.next.next = temp

        return

    def last_first(self):
        # iterate over the intire list
        itr = self.head
        while itr.next:
            curr = itr
            itr = itr.next
        # make the last element the head
        self.insertAtBegi(itr.data)
        # also keep track of the second last and remove the last node
        curr.next = None
        return

    def sortedlist(self):
        itr = self.head
        temp = []
        while itr:
            temp.append(itr.data)
            itr = itr.next
        self.insert_values(sorted(temp))
        return

    def reverse(self):
        itr = self.head
        while itr:
            self.insertAtBegi(itr.data)
            itr = itr.next
        temp = self.get_middle()
        temp.next = None
        return



class binarSearchtreenode:
    


    def add_child(self, data):
        # check to see if the data already exists
        # no same data allowed in bst
        if data == self.data:
            return
        # check is value on the left is smaller
        if data < self.data:
            # check if the left node is empty
            if self.left:
                # if not empty recursively call the add child method
                self.left.add_child(data)
            else:
                # or else just add the data
                self.left = binarSearchtreenode(data)
        else:
            # same procedure for the right side
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarSearchtreenode(data)

    def inorder(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.inorder()
        # visit roottree

        elements.append(self.data)
        # viitt right sub tree
        if self.right:
            elements += self.right.inorder()
        return elements

    def search(self, val):
        if self.data == val:
            # print(True)
            return True
        # val might be in left subtree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                # print(False)
                return False
        # val might be in right subtree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                # print(False)
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            # print(self.data)
            return self.data

    def find_max(self):
        if self.right:
            return self.right .find_max()
        else:
            return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def preorder(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preorder()

        if self.right:
            elements += self.right.preorder()
        return elements

    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()

        if self.right:
            elements += self.right.postorder()

        elements.append(self.data)
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self

    def height(self, node):
        if node is None:
            return
        else:
            lheight = self.height(node.left)
            rheighth = self.height(node.right)

            if lheight > rheighth:
                return lheight+1
            else:
                return rheighth+1

# def buildtree(elements):
#     a = len(elements)
#     root = binarSearchtreenode(elements[int(a/2)])

#     for i in range(len(elements)):
#         root.add_child(elements[i])
#     return root


if __name__ == "__main__":
    root = binarSearchtreenode(1)
    root.left = binarSearchtreenode(2)
    root.right = binarSearchtreenode(3)
    root.left.left = binarSearchtreenode(4)
    root.left.right = binarSearchtreenode(5)
    print(root.height(root))
    # ll = LinkedList()
    # ll.insert_values([1, 2, 3, 4, 5, 6, 7])
    # n = ll.get_length()
    # numbers = ll.print()
    # numbers = [17, 1, 8, 20, 9, 23, 18, 34, 18, 4]
    # numbers_tree = buildtree(numbers)
    # print(numbers_tree.inorder())
    # print(numbers_tree.preorder())
    # print(numbers_tree.postorder())
    # print(numbers_tree.search(20))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    # numbers_tree.delete(20)
    # print(numbers_tree.inorder())
