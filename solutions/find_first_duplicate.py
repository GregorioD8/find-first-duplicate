def find_first_duplicate(arr):
     """
    Finds the first duplicate value in an array.
    
    Parameters:
    arr (list): The list of integers to check for duplicates.
    
    Returns:
    int: The first duplicate value if it exists, otherwise -1.
    """
    #  Iterate through each number in the array
    unique_nums = set()
     
    for num in arr:
        # Check if the number is already in the set
        if num in unique_nums:
            return num # First duplicate found
        # Add the number to the set if not seen before
        unique_nums.add(num) 
        
    # No duplicates found return -1
    return -1

print("Expecting: 3")
print(find_first_duplicate([2, 1, 3, 3, 2]))

print("")

print("Expecting: -1")
print(find_first_duplicate([1, 2, 3, 4]))

print("")

print("Expecting: -1")
print(find_first_duplicate([]))

print("")

print("Expecting: -1")
print(find_first_duplicate([5]))

print("")

print("Expecting: 7")
print(find_first_duplicate([7, 1, 2, 3, 7]))