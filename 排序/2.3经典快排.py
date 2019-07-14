'''
每次只排最后一个数
传数组整个数组，区分的是l和r，数组的边界，不用自己切。自己切的也可以再想想
参照荷兰国旗问题，将末尾数字看做num
'''
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

#以最后一个数作为比较对象
def sortProcess(arr, l, r):
    less = l-1
    for i in range(l, r+1):
        if arr[i] <= arr[r]:
            less += 1
            swap(arr, i, less)
    return less

def quickSort1(arr, l ,r):
    if l < r:
        leftboundary = sortProcess(arr, l, r)
        quickSort1(arr,l,leftboundary-1)
        quickSort1(arr,leftboundary+1,r)

# def quickSort2(arr, l, r):

arr = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]
arr1 = [5,4,3,2,1]
quickSort1(arr1,0,len(arr1)-1)
print(arr1)