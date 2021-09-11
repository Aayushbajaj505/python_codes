# we divide the list into two parts sorted and unsorted
# the first element is considered sorted

# Wrost Case Time Complexity: O(n^2)
# Best Case Time Complexity:  O(n)

def insertionsort(arr):
    for x in range(1, len(arr)):
        # take one value at a time
        value_to_sort = arr[x]
        # check the value to its immediate left
        while arr[x-1] > value_to_sort and x > 0:
            arr[x], arr[x-1] = arr[x-1], arr[x]
            x = x-1  # keep going down the list untill the first element

    return arr


print(insertionsort([14, 5, 6, 7, 8, 90]))
