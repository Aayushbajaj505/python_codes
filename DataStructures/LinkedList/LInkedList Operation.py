# Create a node
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

        # checking if linked list is empty
        if self.head == None:
            return "Linked List is empty"

        # start bthe iteration from the first element
        itr = self.head
        llstr = ''

        # traverset through the linked list and adding each
        # eleemt to the string for printing
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)  # priting the linked list

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
        curr=self.head
        prev,next=None
        while curr:
            next=curr.next
            curr.next = prev
            prev=curr
            curr = next
            
            
        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([11, 12, 5, 9, 6, 13, 20])
    ll.print()
    # ll.insert_after_value("mango", "apple")  # insert apple after mango

    # ll.remoive_at(2)
    # print(ll.count_int(5))
    # ll.remove_duplicates()
    # ll.swap_nodes(12, 13)
    # ll.last_first()
    # ll.sortedlist()
    # ll.reverse()
    # ll.get_middle()
    # ll.get_middle()
    # print(ll.get_length())
    # ll.head = ll.mergesort(ll.head)
    ll.print()

    # ll.remove_by_value("orange")  # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()
