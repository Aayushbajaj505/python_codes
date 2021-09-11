# Used to search in a sorted list
# also called middle search
# compares the target to the middle and then searches accordingly

# time complexity is O(Log n)

def binsearch(arr, x,):
    l = 0
    r = len(arr)-1
    # len-1 because the index starts from zero
    while(l <= r):
        mid = l+(r-l)//2
        if(arr[mid] == x):  # check if x is present at mid
            return mid
        elif(arr[mid] < x):  # if x is greater, ignore left half
            l = mid+1
        else:  # if x is smaller, ignore right half
            r = mid-1
    return-1


arr = [2, 3, 4, 40, 50]
print("THe element is present at: "+str(binsearch(arr, 40)))
