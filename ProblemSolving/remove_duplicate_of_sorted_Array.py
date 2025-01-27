def removeDuplicates(nums):
    if not nums:
        return 0

    white_index = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[white_index] = nums[i]
            white_index += 1
    return white_index,nums[:white_index]

array = [1,1,2,3,4,4,5,5]
print(removeDuplicates(array))