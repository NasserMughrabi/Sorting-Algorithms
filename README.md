# Sorting Algorithms and Algorithm Patterns

# Divide and Conquer

- Divide and Conquer : it is an algorithm pattern where problem is divided into smaller subproblems and then each subproblem is solved/conquered individualy.

1. Divide : e.g divide array into two smaller arrays
2. Conquer : e.g recursive step (recall the same function on both or one of the smaller arrays
3. Combine : e.g merge - combine two sorted arrays

# Recursion

- The idea of recursion is that instead of conquering the problem top to bottom for graph/tree or start to end for array/string in a for/while loop, in recursion you conquer the problem from bottom to top (what's before the recursive call(s) gets executed going top to bottom for graph/tree or start to end for array/string and what's after the recursive call(s) gets executed going bottom to top for graph/tree or end to start for array/string). In short, in recursion you conquer the problem from bottom to top. What's before the recursive call(s) gets executed going top to bottom and what's after the recursive call(s) gets executed going bottom to top

- Recursion : it is an algorithm pattern where the problem is conquered bottom to top instead of top to bottom. The code will not execute what is after the recursive call until the bottom element is reached

# Merge Sort

- Merge Sort : This is a recursive divide and conquer algorithm. Array will be divided into two subarrays and then recursive calls on both halves and finally merging step. Merge step is the most important step where things are compared and combined into one array and returned to the previous instance. Merge is the most important step in this algorithm

# Quick Sort

- Quick Sort : This is a recursive divide and conquer algorithm. Array will be divided into two subarrays and then partitioned and finally recursive calls, array should be sorted by then. Partitioning is the most important step in this algorithm

- Quick Select : This is a recursive algorithm to choose the median in an array in O(logN) time. usually used with quick sort to choose the median element in an array as the pivot for quick sort. It helps making quick sort faster by selecting the median as the pivot index

- Mom Select : This is a recursive algorithm usually used with quick select to choose the median of medians which would be a good pivot to make quick select algorithm more efficient and therefore make quick sort algorithm faster.

# Bubble Sort

- Bubble Sort: This is an iterative sorting algorithm. It loops over the array using two for loops. If the array of n size it loops over the array n \* n times. Every time it makes sure it sorts the biggest element at the end of the array by comparing element i with element i+1 and swapping until the end of the array.

# Selection Sort

- Selection Sort: This is an iterative sorting algorithm. It loops over the array using two for loops. In this algorithm we assume that we have two arrays within the same array. A sorted part and unsorted part. The array start completly unsorted, then select the first element to replace with smallest element in the array if a smaller one exists. find the min element in the unsorted array starting at index 1 then at the end of array replace the min element with the selected element.

# Insertion Sort

- Insertion Sort: This is an iterative sorting algorithm. It loops over the array using two for loops. In this algorithm we assume that we have two arrays within the same array. A sorted part and unsorted part. The array start with the first element being sorted and the rest unsorted, then it takes the element next to the last element in the sorted part and sorts it in the right spot in the sorted array.
