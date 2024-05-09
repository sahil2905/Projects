def binary_search(list1,n):
    low=0
    high=low(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
    if list1[mid]>n:
        low=mid+1
    elif list1[mid]>n:
        high=mid-1
    else:
        return mid
    return -1
    list1=[2,4,45,81,42]
    n=45
result=binary_search()
if result ==-1:
    print("element is present")
else:
    print("element is not present")
