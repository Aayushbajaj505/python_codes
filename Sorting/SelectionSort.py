# 1.find the minimum value
# 2.swap the lowest value in zero index
# 3.now the zero index is thet sorted part so we
# 4.start from the first index and repeat the first two steps
# vice versa for decending(max value insted of min)

# Time complexity = O(n^2)

def selectionsort(arr):
    for x in range(len(arr)):
        min_index = x
        # finding the minimum element in remaining unsoreted array
        for y in range(x+1, len(arr)):
            if(arr[y] < arr[min_index]):
                min_index = y
        # swap the minimum elemt with the first element
        arr[x], arr[min_index] = arr[min_index], arr[x]


arr = [1, 7, 9, 5, 6, 6, 3, 5, 4, 65, 15, 64, 68]
selectionsort(arr)
print(arr)
