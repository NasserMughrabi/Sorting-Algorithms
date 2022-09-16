# This is in place algorithm, meaning right and left arrays are created every time mergesort is called
# This algorithm is to sort an array in O(NlogN) running time
# This is not in-place sorting algorithm
# Time Complexity: n^2 in all cases (best, average, worst)
# Space Complexity: O(1), no extra space used

def merge_sort(arr, left_idx, right_idx) :

    if left_idx >= right_idx:
        return
    
    # divide (iterate down)
    mid_idx = left_idx + (right_idx - left_idx)//2 # round down

    # recursive
    merge_sort(arr, left_idx, mid_idx)
    merge_sort(arr, mid_idx+1, right_idx)

    # conqure (iterate up)
    return merge(left_idx, mid_idx, right_idx, arr) 

def merge(left_idx, mid_idx, right_idx, arr) :
    left_start = left_idx
    right_start = mid_idx +1
    
    while left_start < right_start and right_start <= right_idx :
        if arr[right_start] < arr[left_start] :
            swap(arr, left_start, right_start)
            left_start = left_start +1
            right_start = right_start +1
        else :
            left_start = left_start +1

    return arr

def swap(arr, left_idx, right_idx) :
    temp = arr[right_idx]
    for i in range(right_idx, left_idx, -1) :
        arr[i] = arr[i-1]
    arr[left_idx] = temp

merge_sort([4,1,2,9,5], 0, 4)