#Example 7: Python program to count the total number of digits in a number.

def total_count_digit(num):
    num = abs(num)
    if num == 0:
        return 1

    count = 0

    while num > 0:
        num//=10
        count += 1
    return count

num = -123457
result = total_count_digit(num)
print(result)
