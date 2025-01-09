def find_missing_number(nums):
    n = len(nums)+1
    expected_sum = n *(n+1)//2
    total_sum = sum(nums)
    missing_sum = expected_sum - total_sum
    return missing_sum


n =[1,2,3,5,6]
print("The missing number is",find_missing_number(n))