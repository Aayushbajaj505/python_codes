# linerar Search
def linearSearch(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1


arr = [1, 7, 9, 5, 6, 6, 3, 5, 4, 65, 15, 64, 68]
print("element found at index: "+str(linearSearch(arr, 65)))
