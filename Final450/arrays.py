def reverse(arr):
    print(arr[::-1])


def maxmin(arr):
    arr.sort()
    print('Min is ' + str(arr[0]))
    print('Max is ' + str(arr[len(arr)-1]))


def negatiivepositive(arr):
    j=0
    for i in range(len(arr)):
        if (arr[i]<0):
            temp=arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j+=1
        
            
        
            


if __name__ == "__main__":
    reverse([1, 2, 9, 4, 8, 6, 7])
    maxmin([1, 2, 9, 4, 8, 6, 7])
