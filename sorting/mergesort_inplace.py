# In place algorithm, so mid_idx is on the left side
def merge_sort(arr, left_idx, right_idx) :
    # left_idx = 0
    # right_idx = len(arr) -1

    if left_idx >= right_idx:
        return
    
    # divide (iterate down)
    mid_idx = left_idx + (right_idx - left_idx)//2 # round down
    # print( "Going down/toend", left, right)
    # recursive
    merge_sort(arr, left_idx, mid_idx)
    merge_sort(arr, mid_idx+1, right_idx)

    # print( "Going up/tostart", left, right)
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

    print("merged", arr)
    return arr

def swap(arr, left_idx, right_idx) :
    temp = arr[right_idx]
    for i in range(right_idx, left_idx, -1) :
        arr[i] = arr[i-1]
    arr[left_idx] = temp

merge_sort([4,1,2,9,5], 0, 4)
# merge_sort([1,2,3,9,4,5])
# print(merge_sort([1,2,3,9,4,5]))