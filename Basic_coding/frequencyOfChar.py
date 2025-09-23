'''
Count the frequency of each character in two strings using dictionaries.
'''

def count_character_frequency(input_string):
    """
    Counts the frequency of each character in a given string.

    Args:
        input_string: The string to analyze.

    Returns:
        A dictionary where keys are characters and values are their frequencies.
    """
    frequency_dict = {}
    for char in input_string:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict

# Example usage with two strings
string1 = "hello world"
string2 = "programming"

frequency_string1 = count_character_frequency(string1)
frequency_string2 = count_character_frequency(string2)

print(f"Character frequencies in '{string1}': {frequency_string1}")
print(f"Character frequencies in '{string2}': {frequency_string2}")