# we iterate over all the items and in every pass
# the highest item bubbles to the top of the list

# Wrost Case Time Complexity: O(n^2)
# Best Case Time Complexity:  O(n)

def bubblesort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


arr = [1, 7, 9, 5, 6, 6, 3, 5, 4, 65, 15, 64, 68]
print(bubblesort(arr))
