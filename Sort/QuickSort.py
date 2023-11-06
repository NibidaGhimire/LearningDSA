def quick_sort(lst):
    length = len(lst)
    
    if length <= 1:
        return lst     
    else:
        pivot = lst.pop()
 
    elements_greater = []
    elements_smaller = []
 
    for element in lst:
       
        if element > pivot:
            elements_greater.append(element)        
        else:
            elements_smaller.append(element)
 
    return quick_sort(elements_smaller) + [pivot] + quick_sort(elements_greater)
 
list1 = [7, 2, 1, 6, 8, 5, 3, 4]
print(f"Unsorted List: {list1}")
 
sorted_list = quick_sort(list1)
print(f"Sorted List:  {sorted_list}")



# Time Complexity
# Worst Case Complexity : O(n^2)
# Average Case Complexity : O(nlogn)
# Best Case COmplexity : O(nlogn)

# Space Complexity : O(logn)