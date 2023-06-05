class BracketValidator:
    def __init__(self):
        self.opening_brackets = ['(', '[', '{']
        self.closing_brackets = [')', ']', '}']
        self.bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    def is_valid(self, s):
        stack = []

        for char in s:
            if char in self.opening_brackets:
                stack.append(char)
            elif char in self.closing_brackets:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if self.bracket_pairs[top] != char:
                    return False

        return len(stack) == 0


# Example usage:
validator = BracketValidator()

print(validator.is_valid("()"))  # True
print(validator.is_valid("()[]{}"))  # True
print(validator.is_valid("[)"))  # False
print(validator.is_valid("({[)]"))  # False
print(validator.is_valid("{{{"))  # False
