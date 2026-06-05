def local_maximum(grid):
    """
    accept nxn matrix, 
    return n-2 x n-2 matrix that each cell is max of 3x3 matrix in nxn matrix center around row i+1 and row j+1
    """
    n = len(grid)
    # initiate the (n-2)x(n-2) result matrix
    # result is (n-2)x(n-2) because there are n-2 possible 3x3 windows across n rows, and n-2 across n columns
    result = [[0]*(n-2) for i in range (n-2)]
    for k in range (n-2):
        p=k 
        for p in range(n-2):
            values = []
            # get values in the 3x3 matrix starting at row k, colum p and ends at row k+3, column p+3
            for row in range(k,k+3):
                for column in range(p,p+3):#(1,4) (2,5)(n-2,n+1)
                    values+=[grid[row][column]]
            #assign the max of values to result matrix at row k, column p
            result[k][p]=max(values)
     
    return result
print(local_maximum([
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]))
                
