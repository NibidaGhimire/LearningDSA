# Replace ___ with your code

def selection_sort(lst):
    for i in range (len(lst)):
        minn = lst[i]
        for j in range(i+1,len(lst)):
            if lst[j]<minn:
                lst[j],lst[i]= lst[i], lst[j]

    return lst

def bucket_sort(lst,bucket_range):
    
    buckets = [[] for _ in bucket_range]
    
    for index, brange in enumerate(bucket_range):
        for num in lst:
            if brange[0] <= num < brange[1]:
                buckets[index].append(num)
 
    sorted_list = []
    for bucket in buckets:
        bucket = selection_sort(bucket)
        sorted_list.extend(bucket)
    
    return sorted_list
 
lst = [10, 8, 2, 1, 12, 7, 6, 14, 11, 4] 
bucket_range = [(0, 5), (5, 10), (10, 15)]
print(f"Sorted List: {bucket_sort(lst, bucket_range)}")