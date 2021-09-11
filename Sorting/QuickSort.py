from array import array
# Divide and COnquer Algorithmm
# Divides the array into two parts and calls itself on
# both the right and the left halves

# Wrost Case Time Complexity: O(n^2)
# Best Case Time Complexity:  O(nLog n)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    item_greater = []
    item_smaller = []

    for x in arr:
        if x > pivot:
            item_greater.append(x)
        else:
            item_smaller.append(x)
    return quicksort(item_smaller) + [pivot] + quicksort(item_greater)


print(quicksort([51, 1, 1, 4694, 6, -848484, 884, 94,
      84, 8, 4, 4, 844, 4, 4, 98, 46, 49, 656, 4684]))
