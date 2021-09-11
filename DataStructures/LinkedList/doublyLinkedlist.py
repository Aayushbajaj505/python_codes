import gc


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class doublyLinkedlist:
    def __init__(self):
        self.head = None

    def addbegin(self, data):
        # assign values to the new node
        node = Node(data, self.head)
        # check if the list is empty
        if self.head is not None:
            # if not then change the prev of the current head node from
            # none to the new node
            self.head.prev = node
        # else just create the node
        self.head = node

    def print(self):
        if self.head == None:
            return
        dllstr = ''
        itr = self.head
        temp = None
        while itr:
            if itr.next == None:
                temp = itr
            dllstr += str(itr.data)+"<-->"
            itr = itr.next
        print(dllstr)

        # uncomment to print list in reverse order

        # dlla = ''
        # while temp:
        #     dlla += str(temp.data)+"<-->"
        #     temp = temp.prev
        # print(dlla)

    def addatend(self, data):
        if self.head == None:
            node = Node(data, self.head)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)
        itr.prev = itr

    def insertafter(self, prev_node, data):
        if prev_node == None:
            return
        node = Node(data, prev_node.next, prev_node)
        if node.next is not None:
            node.next.prev = node

    def delete(self, delnode):
        if delnode == None:
            return
        # if the node to be deleted is the head Node
        if delnode == self.head:
            self.head = delnode.next
        # if th enode to be deleted is not last or head
        if delnode.next is not None:
            # breaking both the links
            delnode.next.prev = delnode.prev
            delnode.prev.next = delnode.next
        else:
            # if the given node is the last node
            delnode.prev.next = None
        gc.collect()
        return

    def deleteindex(self, index):
        itr = self.head
        if index == 1:
            self.head == itr.next
            return
        count = 1
        while itr:
            if(count == index):
                self.delete(itr)
                break
            count = count+1
            itr = itr.next
        return

    def removeduplicates(self):
        if self.head == None:
            return
        itr = self.head
        while itr.next:
            if itr.data == itr.next.data:
                self.delete(itr.next)
            else:
                itr = itr.next

    def deleteallparticular(self, mark):
        # base condition
        if self.head == None:
            return
        # check if the the data is available inthe head also
        if self.head.data == mark:
            self.head = self.head.next
        # declare head
        itr = self.head
        # iterate throgh the list deleting every element which matches
        while itr.next:
            if itr.next.data == mark:
                self.delete(itr.next)
            else:
                itr = itr.next

    def length(self):
        if self.head == None:
            return
        itr = self.head
        count = 0
        while itr:
            count = count+1
            itr = itr.next
        return count

    def get_middle(self):
        fast = self.head
        slow = self.head
        while fast:
            if fast == self.head:
                fast = fast.next.next
            else:
                slow = slow.next
                fast = fast.next.next
        return slow

    def reverse(self):
        itr = self.head
        while itr:
            self.addbegin(itr.data)
            itr = itr.next
        temp = self.get_middle()
        temp.next = None
        gc.collect()

    def reverse_using_stack(self):
        stack = []
        itr = self.head
        while itr:
            stack.append(itr.data)
            itr = itr.next
        itr = self.head
        while itr:
            itr.data = stack.pop()
            itr = itr.next
        return


if __name__ == '__main__':
    dll = doublyLinkedlist()
    dll.addbegin(1)
    dll.addbegin(1)
    dll.addbegin(1)
    dll.addbegin(5)
    dll.addbegin(5)
    dll.addbegin(7)
    # dll.insertafter(dll.head.next, 6)
    # dll.deleteindex(6)
    # dll.removeduplicates()
    # dll.deleteallparticular(7)
    # print(dll.length())
    dll.print()
    dll.reverse_using_stack()
    dll.print()
