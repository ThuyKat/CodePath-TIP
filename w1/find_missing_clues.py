def find_missing_clues(clues, lower, upper):
    """
    given upper, lower integers and an array of unique integers in [upper,lower] range
    Return shortest sorted list of ranges that covers all missing nums - not in nums but belong to [upper,lower]
    """
    result = []
    missing = []
    for x in range(lower,upper+1):
        if x not in clues:
            missing+=[x]
        else:
            if missing:
                result+=[[missing[0],missing[-1]]]
                missing = []
    if missing:
        result+=[[missing[0],missing[-1]]]
    return result
print(find_missing_clues([0, 1, 3, 50, 75],0,99))
