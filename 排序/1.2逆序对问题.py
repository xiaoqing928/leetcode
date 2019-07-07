'''
在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对。
整个过程就是一个分治的思想
'''

def merge1(arr, l, m, r):
    help = []
    i, p1, p2 = 0, l, m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] > arr[p2]:
            for i in range(p1, m+1):
                print(arr[i], arr[p2])
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1
    if p1 <= m:
        for i in range(p1, m + 1):
            help.append(arr[i])
    if p2 <= r:
        for i in range(p2, r + 1):
            help.append(arr[i])
    le = len(help)
    for i in range(le):
        arr[l + i] = help[i]

def mergeSort(arr, l, r):
    if l == r:
        return
    mid = int((l + r) / 2)
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge1(arr, l, mid, r)

'''
    这个是逆序对出现的次数
'''
class Solution:
    global count
    count = 0
    def merge1(self, arr, l, m, r):
        help = []
        i, p1, p2 = 0, l, m + 1
        while p1 <= m and p2 <= r:
            if arr[p1] > arr[p2]:
                    global count
                    count += (m - p1 + 1)
            if arr[p1] < arr[p2]:
                help.append(arr[p1])
                p1 += 1
            else:
                help.append(arr[p2])
                p2 += 1
        if p1 <= m:
            for i in range(p1, m + 1):
                help.append(arr[i])
        if p2 <= r:
            for i in range(p2, r + 1):
                help.append(arr[i])
        le = len(help)
        for i in range(le):
            arr[l + i] = help[i]

    def mergeSort(self, arr, l, r):
        if l == r:
            return
        mid = int((l + r) / 2)
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge1(arr, l, mid, r)

    def InversePairs(self, data):
        # write code here
        self.mergeSort(data, 0, len(data)-1)
        return count % 1000000007

arr1 = [5,4,3,2,1]
# mergeSort(arr1, 0, 4)
a = Solution()
r = a.InversePairs(arr1)
print(r)