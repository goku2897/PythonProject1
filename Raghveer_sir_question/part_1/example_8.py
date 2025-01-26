#Python program to check if the given string is a palindrome.
def checkpalendrum(word):
    l = len(word)-1
    s = 0
    for i in range(l):
        if word[s] != word[l]:
            return False
        s += 1
        l -= 1
    return True

word = "radar"
if checkpalendrum(word):
    print("Yay!")
else:
    print("Nope!")
