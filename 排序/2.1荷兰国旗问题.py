'''
给定一个数组array和一个数num，将小于等于num的数放在数组左侧，大于的放在右侧
要求时间复杂度O（N）,额外空间复杂度O（1）
'''

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

array = [2,5,6,7,1,3,8,5,5]
num = 5
stat = -1 #记录左侧的边界
for i in range(len(array)):
    if array[i] <= num:
        stat += 1
        swap(array, stat, i)
print(array, stat)










