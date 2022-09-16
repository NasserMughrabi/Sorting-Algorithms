# Not in place algorithm, meaning no extra space is used (indices are used instead of new arrays)
# This algorithm is to sort an array in O(NlogN) running time
# This is not in-place sorting algorithm
# Time Complexity: O(NlogN) in all cases (best, average, worst)
# Space Complexity: O(N), left and right arrays are used every call

def merge_sort(arr) :
    
    # base case
    if len(arr) <= 1 :
        return arr
    
    # divide (iterate down)
    mid_idx = len(arr)//2 # round down
    left = arr[:mid_idx]
    right = arr[mid_idx:]

    # Copy array in O(n) - n is size of array
    # recursive
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    # conqure (iterate up)
    return merge(left_arr, right_arr, arr.copy()) 

def merge(left_arr, right_arr, new_arr) :
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left_arr) and right_idx < len(right_arr) :
        if right_arr[right_idx] < left_arr[left_idx] :
            new_arr[left_idx + right_idx] = (right_arr[right_idx])
            right_idx = right_idx +1
        else :
            new_arr[left_idx + right_idx] = (left_arr[left_idx])
            left_idx = left_idx +1

    while (left_idx < len(left_arr)) :
        new_arr[left_idx + right_idx] = (left_arr[left_idx])
        left_idx = left_idx +1
        
    while (right_idx < len(right_arr)) :
        new_arr[left_idx + right_idx] = (right_arr[right_idx])    
        right_idx = right_idx +1

    return new_arr

merge_sort([4,1,2,9,5])