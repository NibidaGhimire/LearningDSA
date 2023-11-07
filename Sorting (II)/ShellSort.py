# Replace ___ with code

def insertion_sort(lst, interval):
        for i in range(interval, len(lst)):
            key = lst[i]            
            j = i - interval          
            while j >= 0 and key < lst[j]:
                lst[j + interval] = lst[j]
                j = j - interval    
            lst[j + interval] = key
        return lst

def shell_sort(n):
    interval=n//2

    while interval>0:
        insertion_sort(lst,interval)
        interval=interval//2
    
    return lst

lst = list(map(int, input().split()))
size = len(lst)
# function call
shell_sort(size)
print(lst)


#Time Complexity :
    #Best Case Complexity : O(n)
    #Worst Case Complexity : O(n*(log(n))^2)

#Space Complexity : O(n)