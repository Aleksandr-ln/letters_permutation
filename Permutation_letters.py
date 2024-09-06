def check_letter(letter, prefix):
    flag = False
    
    for i in range(0, len(prefix)):
        if letter == prefix[i]:
            flag = True
            break
    
    return flag

def permutation_letters(letters, length=-1, prefix=None):
    
    '''Creates all possible strings using letters. Each character is used only once.'''
    
    length = len(letters) if length == -1 else length
    prefix = prefix or []
    
    if length == 0:
        print(*prefix, end=" ", sep="")
        return
    for i in range(0, len(letters)):
        if check_letter(letters[i], prefix):
            continue
        prefix.append(letters[i])
        permutation_letters(letters, length-1, prefix)
        prefix.pop()
        
lst = ['a', 'e', 'i', 'o','u']
permutation_letters(lst)