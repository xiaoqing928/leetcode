'''
    时间复杂度O(N2),空间复杂度O（1）
'''

arr1 = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]

def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    return arr

def insertSort(arr):
    l = len(arr)
    for i in range(1, l):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
            else:
                break
    return arr


a = insertSort(arr1)
print(a)