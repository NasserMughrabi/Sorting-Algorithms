def quicksort(arr, left_idx, right_idx) :

    # base case since quicksort is recursive 
    if len(arr) <= 1 :
        return arr

    if left_idx >= right_idx :
        return 

    # partition
    pivot_idx = partition(arr, left_idx, right_idx)

    # recursive 
    quicksort(arr, left_idx, pivot_idx-1)
    quicksort(arr, pivot_idx+1, right_idx)

    print(arr)
    return arr

def partition(arr, left_idx, right_idx) :
    pivot_idx = right_idx
    j = 0

    for i in range(left_idx, right_idx) :
        if arr[i] < arr[pivot_idx] :
            swap(arr, i, j)
            j = j+1
    
    swap(arr, j, pivot_idx)
    return j # new pivot index

def swap(arr, index1, index2) :
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

quicksort([1,6,2,5], 0, 3)





    
