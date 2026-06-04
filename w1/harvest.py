def harvest(veg_patch):
    """
    accept 2D matrix as vegetable patches, each cell is either 'x' or 'c',
    and return number of carrots ready to harvest =  total cells has value 'c'

    """
    n = len(veg_patch) # num row
    m = len(veg_patch[0]) # num col
    count=0
    for x in range(n):
        for y in range(m):
            if(veg_patch[x][y]=='c'):
                count+=1
    return count
print(harvest([
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]))
