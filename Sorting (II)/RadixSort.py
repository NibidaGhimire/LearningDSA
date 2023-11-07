# Replace ___ with your code

def counting_sort(lst, place):
    
    size = len(lst)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = lst[i] // place
        count[index % 10] += 1
        
    #ascending
    # for i in range(1, 10):
    #     count[i] += count[i - 1]

    #Descending
    for i in range(8, -1,-1):
        count[i] += count[i + 1]
    

    i = size - 1
    while i >= 0:
        index = lst[i] // place
        output[count[index % 10] - 1] = lst[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        lst[i] = output[i]

def radix_sort(lst):
    maxm=max(lst)
    length= len(str(maxm))

    place=1
    for i in range(length):
        counting_sort(lst,place)
        place*=10
    return lst

data = list(map(int, input().split()))
radix_sort(data)
print(data)


# Time Complexity: O(nd) => O(n)[if d is very small]