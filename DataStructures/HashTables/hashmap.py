# first we have to create a new hash funtion
# we will be using the ascii value of all the chars
from typing import Hashable


class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append([key, val])

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        pass


t = Hashtable()
t['march 6'] = 130
t['march 1'] = 80
t['march 3'] = 10
t['march 8'] = 13
print(t['march 8'])
