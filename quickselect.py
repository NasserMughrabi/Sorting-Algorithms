# This algorithm is to choose the kth smallest element in an array (not sorted array)
# This algorithm is also to find the median element in an array by passing k = len(arr)/2 - 1
# Time Complexity: O(LogN)
# Space Complexity: O(1), in place algorithm

def quickselect(arr, left_idx, right_idx, k) :
    
    # base case
    if left_idx == right_idx :
        return arr[left_idx]

    # partition the subarray between these two indecies
    pivot_idx = partition(arr, left_idx, right_idx)

    # recurse on the part that's supposed to have the k index after array is sorted
    if k < pivot_idx :
        return quickselect(arr, left_idx, pivot_idx-1, k)
    elif k > pivot_idx :
        return quickselect(arr, pivot_idx+1, right_idx, k)
    else :
        return arr[pivot_idx]


def partition(arr, left_idx, right_idx) :
    pivot_idx = right_idx
    j = left_idx
    
    for i in range(left_idx, right_idx) :
        if arr[i] < arr[pivot_idx] :
            arr[i], arr[j] = arr[j], arr[i]
            j = j+1
    
    arr[j], arr[pivot_idx] = arr[pivot_idx], arr[j]
    return j # new pivot index

arr = [8,4,0,12,11,2]
arr1 = [8,4,0,12,11,2,3,13,1,6]
k = 3
print(quickselect(arr, 0, len(arr)-1, k-1))
print(quickselect(arr1, 0, len(arr1)-1, k-1))
