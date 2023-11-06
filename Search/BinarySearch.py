#With Recursion
def binary_search(lst, target, low, high):
 
    if high >= low:
        mid = (high + low) // 2
 
        if lst[mid] == target:
            return mid
 
        elif lst[mid] > target:
            return binary_search(lst, target, low, mid-1)
        
        else:
            return binary_search(lst, target, mid + 1, high)
 
    else:
        return None
 
lst = [3, 4, 5, 6, 7, 8, 9]
 
# target value to be searched for
target = 5
 
result = binary_search(lst, target, 0, len(lst)-1)
 
if result is not None:
    print(f"Element {target} is found at index {result}")
else:
    print("f{target} is not found in the list")


# Time Complexity
# Worst Case Complexity : O(logn)
# Average Case Complexity : O(logn)
# Best Case COmplexity : O(1)

# Space Complexity : O(1)


#Without recursion

# def binary_search(lst, target):
#     low = 0
#     high = len(lst) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
        
#         if target == lst[mid]:
#             return mid
#         elif target < lst[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
    
#     return None
 
# lst = [4, 5, 6, 7, 8, 9, 10]
 
# # set a target value
# target_value = 7
 
# result = binary_search(lst, target_value)
 
# if result is not None:
#     print(f"Element {target_value} is found at index {result}")
# else:
#     print(f"{target_value} is not found in the list")