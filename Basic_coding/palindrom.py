'''

'''

def is_palindrome_slicing(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome_slicing("madam"))  # Output: True
print(is_palindrome_slicing("hello"))  # Output: False