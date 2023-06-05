import string

def is_pangram(s, alphabet=string.ascii_lowercase):
    return set(alphabet) == set(s.replace(" ", "").lower())

text = input("Enter a string: ")
print(is_pangram(text))
