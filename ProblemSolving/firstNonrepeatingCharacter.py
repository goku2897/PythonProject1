def get_first_none_repeating_character(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char,0) + 1

    for i in char_count:
        if char_count[i] == 1:
            return "The first non repeating character is " +i

    return "There is no non repeating character"

String_character = "abcdefabcf"
print(get_first_none_repeating_character(String_character))