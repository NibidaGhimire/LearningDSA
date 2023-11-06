def insertion_sort(lst):
    
    for i in range(1, len(lst)):
        key = lst[i]
        
        j = i - 1
        
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
 
        lst[j + 1] = key
    
    return lst
 
data =  [7, 4, 1, 3, 2]
 
print(f'Unsorted List: {data}')
sorted_list = insertion_sort(data)
print(f'Sorted List: {sorted_list}')



# Time Complexity
# Worst Case Complexity : O(n^2)
# Average Case Complexity : O(n^2)
# Best Case COmplexity : O(n)

# Space Complexity : O(1)