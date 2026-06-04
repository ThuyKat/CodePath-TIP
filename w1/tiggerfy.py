def tiggerfy(word):
    """
    Returns a string that has t, i, gg, er removed give a string
    """
    remove_list = {'t','i','gg','er'}
    result = ''
    i = 0
    while i<len(word):
        one_char = word[i].lower()
        two_char = word[i:i+2].lower()
        if one_char in remove_list:
            i+=1
        elif two_char in remove_list:
            i+=2
        else:
            result+=one_char  
            i+=1  
    return result
print(tiggerfy("Trigger"))
