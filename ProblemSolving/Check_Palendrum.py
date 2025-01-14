def checkPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:  # Check if characters don't match
            return False  # Not a palindrome
        l += 1  # Move left pointer
        r -= 1  # Move right pointer
    return True  # All characters matched, it's a palindrome

# Test the function
input_string = "madam"
if checkPalindrome(input_string):
    print("{input_string} is a Palindrome".format(input_string=input_string))
else:
    print("{input_string} is not a Palindrome".format(input_string=input_string))
