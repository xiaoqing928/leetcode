'''
给定一个数组array和一个数nun，将小于num的数放在数组左侧，大于的放在右侧,等于的数放中间
要求时间复杂度O（N）,额外空间复杂度O（1）
'''

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

array = [2,5,6,7,1,3,8,5,5]
num = 5
l = -1
r = len(array)
cur = 0
while cur < r:
    if array[cur] < num:
        l += 1
        swap(array, l, cur)
        cur += 1
    elif array[cur] == num:
        cur += 1
    else:
        r -= 1
        swap(array, r, cur)

print(array)