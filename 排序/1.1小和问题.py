'''
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组
的小和。
例子：
[1,3,4,2,5]
'''
def merge(arr, l, m, r):
    help = []
    i, p1, p2 = 0, l, m + 1
    res = 0
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            res += (r - p2 + 1) * arr[p1]
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    if p1 <= m:
        for i in range(p1,m+1):
            help.append(arr[i])
    if p2 <= r:
        for i in range(p2, r + 1):
            help.append(arr[i])
    return res

def mergeSort(arr, l, r):
    if l == r:
        return 0
    mid = int((l + r) / 2)
    return mergeSort(arr, l, mid) + mergeSort(arr, mid+1, r) + merge(arr, l, mid, r)

arr = [1,2,3,4,5]
res = mergeSort(arr, 0, 4)
print(res)