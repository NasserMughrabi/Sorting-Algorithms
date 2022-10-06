# Quick sort is to sort an algorithm in a O(NlogN) running time best case
# Time Complexity: best: O(NlogN), average: O(NlogN), worst: O(N^2)
# Space Complexity: O(1), in place algorithm

def quicksort(arr, left_idx, right_idx) :

    # base case since quicksort is recursive 
    if left_idx >= right_idx :
        return 

    # partition
    pivot_idx = partition(arr, left_idx, right_idx)

    # recursive 
    quicksort(arr, left_idx, pivot_idx-1)
    quicksort(arr, pivot_idx+1, right_idx)

    return arr

def partition(arr, left_idx, right_idx) :
    pivot_idx = right_idx
    j = left_idx

    for i in range(left_idx, right_idx) :
        if arr[i] < arr[pivot_idx] :
            arr[i], arr[j] = arr[j], arr[i]
            j = j+1
    
    arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
    return j # new pivot index

arr = [1,6,2,5]
print(quicksort(arr, 0, len(arr)-1))

arr = [3,6,8,10,1,2,1]
print(quicksort(arr, 0, len(arr)-1))





    
