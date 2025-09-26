def is_valid(s: str) -> bool:
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in pairs.values():  # opening
            stack.append(ch)
        elif ch in pairs:        # closing
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            # ignore other characters or treat as invalid depending on spec
            return False
    return not stack

# tests
print(is_valid("({[]})"))  # True
print(is_valid("([)]"))    # False
