def findTarget(arr, target):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



a = [1,2,3,4,5,6,7]
target = 5
print(findTarget(a,target))
