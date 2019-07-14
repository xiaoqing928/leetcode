
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapify(arr, cur, n):
    '''
    :param arr:数组
    :param cur: 更改的位置坐标
    :param n: 现有的堆长度（当前其实可以看作len（arr）,但实际上并不一定整个数组就是已经排好的堆）
    :return:
    '''
    l = cur * 2 + 1
    largest = cur
    while l < n:
        r = l + 1
        #左右子节点的数进行比较,取大的
        if r < n and arr[r] > arr[l]:
            largest = r
        else:
            largest = l
        if arr[largest] > arr[cur]:
            swap(arr, largest, cur)
        else:
            break
        cur = largest
        l = largest * 2 + 1

arr = [52, 656, 8979, 536, 456, 2323, 362, 19, 46, 64, 78, 17, 645, 15, 343, 1, 3, 4, 6, 3, 45, 7, 67, 2, 9, 2]
heapify(arr,0,len(arr))
print(arr)

