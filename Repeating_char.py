def find_first_repeating_character(s):
    seen = set()
    for char in s:
        if char in seen:
            print(f"First repeating character: {char}, Memory Address: {id(char)}")
            return char, id(char)
        seen.add(char)
    print("No repeating character found.")
    return None

# Example usage
string = "abcdefabc"
find_first_repeating_character(string)
