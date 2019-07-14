#构建大根堆，去头部和末尾交换，堆大小减一
#heapify 继续进行相同操作
#终止条件堆的长度>1

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapInsert(arr, i):
    while arr[i] > arr[int((i-1)/2)]:
        swap(arr, i, int((i-1)/2))
        i = int((i-1)/2)

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

def heapSort(arr):
    l = len(arr) # l也可以看作堆的长度
    if l < 2:
        return
    #构建大根堆
    for i in range(l):
        heapInsert(arr, i)
    # 交换头和尾
    swap(arr, 0, l-1)
    l -= 1 #堆大小减一
    while l > 0:
        heapify(arr, 0, l)
        swap(arr, 0, l-1)
        l -= 1

arr = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]
arr2 = [2,1,3,6,0,4]

heapSort(arr2)
print(arr2)

