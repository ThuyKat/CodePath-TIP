def final_value_after_operations(operations):
    '''
    Return final value of tiger after performing all operations in a list - bouncy and flouncy increments value by 1 while others decrements value by 1
    '''
    # initialise value 
    value = 1
    # simplify the conditions
    increment = {"bouncy","flouncy"}
    for operation in operations:
        if operation.lower() in increment:
            value+=1
        else:
            value-= 1
    return value
print(final_value_after_operations(["trouncy", "flouncy", "flouncy"]))

# use a set be quicker than a tuple because set built on hashmap under the hood. 
