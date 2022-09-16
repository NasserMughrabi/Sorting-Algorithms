# This algorithm is a faster implementation of quick select where I use momselect to choose the median of median in an array to be the pivot_index for partition (to choose good pivot) and then do the normal quick select to find the median/kth smallest. The idea of mom select is to choose a good pivot for partition which will make quick select faster by avoiding choosing a bad pivot and spending more time finding the median.
# Time Complexity : TBD
# Space Complexity : TBD

def momselect(arr, k) :

        # mom select to find median of medians
        m = len(arr)//5
        remainder = len(arr) % 5
        medians = []
        
        # split array into arrays of five elements
        for i in range(m) :
            left = 5*i
            right = 5*(i+1)-1
            medians.append(medianOfFive(arr, left, right))
        if remainder > 0 :
            left = len(arr)-remainder
            right = left+remainder-1
            medians.append(medianOfFive(arr, left, right))

        # find good pivot (median of medians)
        mom_value = momselect(medians, len(medians)//2)
        
        # find the index of mom_value in the arr
        for i in range(len(arr)) :
            if arr[i][0] == mom_value :
                pivot_idx = i

        left_arr, right_arr, piv_value = partition(arr, pivot_idx)

        # if the k(targeted index) is on the left array, then recurse on left array
        if k < len(left_arr) : # new pivot index
            return momselect(left_arr, k)
        # if the k(targeted index) is on the right array, then recurse on right array
        elif k > len(left_arr) :
            return momselect(right_arr, k-len(left_arr)-1)
        # if the pivot_idx is equal to the targeted index, then the element we looking for is sorted
        else :
                return piv_value

# Sort the array where 
def partition(array, pivot_index):
    '''return some version of a partitioned array'''
    lesser = []
    greater = []
    piv_value = array[pivot_index][0]
    for pair in array:
        if pair[0] < piv_value:
            lesser.append(pair)
        elif pair[0] > piv_value:
            greater.append(pair)
    return lesser, greater, piv_value

# find the median in n=5 array
def medianOfFive(arr, left_idx, right_idx) :
    new_arr = []
    for i in range(left_idx, right_idx+1):
        new_arr.append(arr[i])

    new_arr = sorted(new_arr)
    return new_arr[len(new_arr)//2]
