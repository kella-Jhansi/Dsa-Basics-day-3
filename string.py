def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]= key
    return arr        
text = input("enter the number of elements:")
ch= list(text)
print(ch)
sort_chars= insertion_so