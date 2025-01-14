def reverse(nums,l,r):
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]

        l += 1
        r -= 1
    return nums

nums = [1,2,3,4,5]
K = 3
nums = reverse(nums,0,len(nums)-1)
nums = reverse(nums,0,(K% len(nums))-1)
nums = reverse(nums,K,len(nums)-1)
print(nums)