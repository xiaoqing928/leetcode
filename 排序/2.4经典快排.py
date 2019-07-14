'''
每次排多个相同的数，同荷兰国旗问题
'''

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sortProcess(arr, l, r):
    less = l-1
    more = r+1
    num = arr[r]
    while l < more:
        if arr[l] < num:
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] > num:
            more -= 1
            swap(arr, more, l)
        else:
            l += 1
    return less, more

def quickSort(arr, l, r):
    '''
    :param arr:  数组
    :param l: 最左端
    :param r: 最右端
    :return:
    '''
    if l < r:
        left,right = sortProcess(arr, l, r)
        quickSort(arr, l, left)
        quickSort(arr, right, r)

arr = [4,3,2,1,15,17,19,11111,456,67,656,362,2,343,645,3,536,6,46,45,64,7,78,9,8979,52,2323]
quickSort(arr,0,len(arr)-1)
print(arr)