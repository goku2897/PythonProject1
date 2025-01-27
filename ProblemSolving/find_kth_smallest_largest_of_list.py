import heapq

def kth_smallest(arr, k):
    if k <= 0 or k > len(arr):
        raise ValueError(f"k={k} is out of bounds for the array length {len(arr)}.")
    return heapq.nsmallest(k, arr)[-1]

def kth_largest(arr, k):
    if k <= 0 or k > len(arr):
        raise ValueError(f"k={k} is out of bounds for the array length {len(arr)}.")
    return heapq.nlargest(k, arr)[-1]

# Example Usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))  # Output: 7
print(kth_largest(arr, k))  # Output: 10

# Test with an invalid k
k = 10
try:
    print(kth_smallest(arr, k))  # Raises a ValueError
except ValueError as e:
    print(e)