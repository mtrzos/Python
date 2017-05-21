def is_isogram(word):
    filteredWord = ''.join(e for e in word if e.isalnum()).lower()
    return len(filteredWord) == len(set(filteredWord))
