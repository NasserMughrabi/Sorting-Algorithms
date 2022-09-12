# Not in place algorithm, so mid_idx is on the right side
def merge_sort(arr) :
    
    # base case
    if len(arr) <= 1 :
        return arr
    
    # divide (iterate down)
    mid_idx = len(arr)//2 # round down
    left = arr[:mid_idx]
    right = arr[mid_idx:]
    
    # print( "Going down/toend", left, right)
    # recursive
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)

    # print( "Going up/tostart", left, right)
    # conqure (iterate up)
    return merge(left_arr, right_arr, arr.copy()) 

def merge(left_arr, right_arr, new_arr) :
    left_idx, right_idx = 0, 0
    # new_arr = [0] * (len(left_arr) + len(right_arr))
    
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

    # print("merged", new_arr)
    return new_arr

merge_sort([4,1,2,9,5])
# merge_sort([1,2,3,9,4,5])
# print(merge_sort([1,2,3,9,4,5]))