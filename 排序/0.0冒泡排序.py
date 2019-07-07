'''
    时间复杂度O（N2）空间复杂度O（1）
'''

arr1 = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    return arr

def quickSort(arr):
    l = len(arr)
    if arr == None and l < 2:
        return arr
    for i in range(l):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr

a = quickSort(arr1)
print(a)