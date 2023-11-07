# Replace ___ with your code

def selection_sort(lst):
    for i in range (len(lst)):
        minn = lst[i]
        for j in range(i+1,len(lst)):
            if lst[j]<minn:
                lst[j],lst[i]= lst[i], lst[j]

    return lst

def bucket_sort(lst):
    bucket1=[]
    bucket2=[]
    bucket3=[]

    for value in lst:
        if 0<=value<5:
            bucket1.append(value)
        elif 5<=value<10:
            bucket2.append(value)
        else:
            bucket3.append(value)

    bucket1=selection_sort(bucket1)
    bucket2=selection_sort(bucket2)
    bucket3=selection_sort(bucket3)

    sortedlist=bucket1+bucket2+bucket3
    return sortedlist


lst = list(map(int, input().split()))
print(bucket_sort(lst))