


def get_perms(str):

    if str == None:
        return None

    permutations = list()

    if len(str) == 0:
        permutations.append("")

    
        return permutations

    first = str[0] # Get the first character

    remainder = str[1:] # Remove the first character

    words = get_perms(remainder)

    for word in words:
        
        for j in range(len(word) + 1):
            s = insert_char_at(word, first, j)
            permutations.append(s)

    return permutations


def insert_char_at(word, c, i):
    """
    Insert char c at index i in word
    """
    start = word[:i]
    end = word[i:]
    return start + c + end
    
print(get_perms("123"))
