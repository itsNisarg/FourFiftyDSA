# Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.
# Note: The kth smallest element is determined based on the sorted order of the array.

# Method 1: Sort the array in ascending order and return the kth element O(n log n)


def method_1(arr, k):
    arr.sort(reverse=False)
    if len(arr) >= k:
        return arr[k - 1]
    return None


# Method 2: Create a max heap with k elements and return the top element O(n log k)
# Note: Usually the avaialble implementations of heap are min heap. So push negative values of the actual values to get a max heap


def method_2(arr, k):
    import heapq

    heap = []
    for a in arr:
        heapq.heappush(heap, -a)
        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0] if heap else None


# Method 3: Using k-select algorithm to find the kth smallest element in O(n) average time complexity


def method_3(arr, k):
    left = 0
    right = len(arr) - 1
    k-=1
    if len(arr)<=k:
        return None
    return _select(arr,left,right,k)


def _select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot = _partitiion(arr,left,right)

    if pivot == k:
        return arr[pivot]
    elif k < pivot:
        return _select(arr,left,pivot-1,k)
    else:
        return _select(arr,pivot+1,right,k)     # Since k is the index in the original array it remains the same


def _partitiion(arr, left, right):
    import random

    pivot = random.randint(left, right)     # Choose a random pivot idx
    pivot_val = arr[pivot]                  # Pivot value

    arr[pivot],arr[right] = arr[right],arr[pivot]    # Place pivot at the end
    print(arr, pivot_val)
    
    i=left                                  # Pointer to the place where the next element <= pivot value should be placed
    for j in range(left,right):             # Loop through the array 
        if arr[j] <= pivot_val:             # If the current element is smaller than or equal to the pivot value
            arr[i],arr[j] = arr[j],arr[i]   # Swap the current element with the element at the pointer
            i+=1                            # Move the pointer to the next position
        print(arr)
        
    arr[i],arr[right] = arr[right],arr[i]   # Place the pivot element at the correct position
    print(arr)
    return i                                # Return the pivot index


if __name__ == '__main__':
    print(method_3([7, 10, 4, 3, 20, 15], 3))

# [9,8,7,1,5,4,3,2,6]
# [1,8,7,9,5,4,3,2,6]
