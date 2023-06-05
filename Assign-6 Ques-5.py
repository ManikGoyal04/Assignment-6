def sort_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

text = input("Enter a hyphen-separated sequence of words: ")
print(sort_words(text))
