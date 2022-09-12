def quickselect(arr, left_idx, right_idx, k) :
    if left_idx >= right_idx :
        return arr[left_idx]

    else :
        pivot_idx = partition(arr, left_idx, right_idx)

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
            swap(arr, i, j)
            j = j+1
    
    swap(arr, j, pivot_idx)
    return j # new pivot index

def swap(arr, index1, index2) :
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

k = 3
print(quickselect([8,4,0,12,11,2], 0, 5, k-1))