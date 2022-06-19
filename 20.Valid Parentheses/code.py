# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# 嘗試的程式
################################
def isValid(s):
    buffer = []
    for i in s:
        buffer.append(i)
    print(buffer)
    if len(buffer) % 2 != 0:
        return False

    for i in range(len(buffer)//2):
        flag_type = 0
        if buffer[0] == '[':
            flag_type = 1
        elif buffer[0] == '{':
            flag_type = 2
        elif buffer[0] == '(':
            flag_type = 3
        if flag_type == 1:
            try:
                buffer.remove('[')
                buffer.remove(']')
            except ValueError:
                return False
        elif flag_type == 2:
            try:
                buffer.remove('{')
                buffer.remove('}')
            except ValueError:
                return False
        elif flag_type == 3:
            try:
                buffer.remove('(')
                buffer.remove(')')
            except ValueError:
                return False
    if buffer == []:
        return True
    else:
        return False


################################
input = "([)]"
print(isValid(input))
