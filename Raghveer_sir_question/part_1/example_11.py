#Python program to count the number of even and odd numbers from a series of numbers.

def count_for_even_and_odd(num):
    odd_count = 0
    even_count = 0
    for i in range(num):
        if i %2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count,even_count


num = int(input("enter a num to give total odd and even count: "))
result = count_for_even_and_odd(num)
print(result)
