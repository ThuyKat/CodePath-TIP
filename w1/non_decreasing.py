def non_decreasing(nums):
    """
    check if nums can be non-decreasing by modifying at most one element
    """
    count = 0
    for index,num in enumerate(nums):
        if index < len(nums)-1 and num > nums[index+1]:
            count+=1
    return count <=1
print(non_decreasing([4,2,1]))
