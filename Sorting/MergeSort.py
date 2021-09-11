def mergesort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2  # Mid of Array

        # DIviding the Aray elements
        L = arr[:mid]
        R = arr[mid:]

        # Sorting both the halves
        mergesort(L)
        mergesort(R)

        i = j = k = 0

        # Main Sorting happens here
        while i < len(L) and j < len(R):
            if(L[i] < R[j]):
                arr[k] = L[i]
                i = i+1
            else:
                arr[k] = R[j]
                j = j+1
            k = k+1

        # checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


arr = [12, 11, 13, 5, 6, 7]
print(mergesort(arr))
