# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Method 1 : Built in functions

def method_1(arr):
    return max(arr), min(arr)

# Method 2 : Loop over with extra space O(1)

def method_2(arr):
    minres = float('inf')      # max float val possible
    maxres = float('-inf')     # min float val possible

    for a in arr:
        minres = min(a, minres)
        maxres = max(a, maxres)
    
    return minres, maxres