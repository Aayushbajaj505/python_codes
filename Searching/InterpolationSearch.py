# It is an improvement over binary search for uniformly distributed elements
# binary search always go to the middle element while it may go to any position if the element to be found may be at the end or front
# to find the position to be searched istead of the middle one the formula used is

#  pos=lo+[(x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo])]

# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched


def interpolsearch(arr, x):
    lo = 0  # lo    ==> Starting index in arr[]
    hi = len(arr)-1  # hi    ==> Ending index in arr[]
    while(lo < hi):

        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        if (arr[pos] == x):
            return pos
        elif(arr[pos] < x):
            lo = pos+1
        elif(arr[pos] > x):
            hi = pos-1
        else:
            return -1


arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)

x = 18
index = interpolsearch(arr, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
