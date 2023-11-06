def linear_search(lst, target):
    
    for index, element in enumerate(lst):
        if element == target:
            return index
    return None
 
lst = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]
 
# set a target value
target_value = 11
 
result = linear_search(lst, target_value)
 
if result is not None:
    print(f"Index of the target value: {result}")
else:
    print("Target value not found in the list.")



# Time Complexity
# Worst Case Complexity : O(n)
# Average Case Complexity : O(n)
# Best Case COmplexity : O(1)
