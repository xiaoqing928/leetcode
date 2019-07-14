# 构建大根堆
# 新加入一个结点，只要比父位置大就交换,之后指针到父节点位置，直到到头为止。

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapInsert(arr, i):
    while arr[i] > arr[int((i-1)/2)]:
        swap(arr, i, int((i-1)/2))
        i = int((i-1)/2)

arr = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]
l = len(arr)
for i in range(l):
    heapInsert(arr, i)
print(arr)
# print(int((0-1)/2))