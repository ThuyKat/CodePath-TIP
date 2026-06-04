def good_pairs(pile1,pile2,k):
    """
    accept lists pile1 and pile2 represents lengths of sticks
    good pair i,j when pile1[i] is divisible by pile2[j]*k
    """
    count = 0
    
    for s1 in pile1:
        for s2 in pile2:
            good_pair = s1 % (s2*k) ==0
            if(good_pair):
                count+=1
    return  count
pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1,pile2,k))
