'''
heap简单的放入和弹出使用
'''
import heapq
heap = []
list1 = [4,5,6,1,2,3]
for i in list1:
    heapq.heappush(heap, i)
while heap:
    print(heapq.heappop(heap))
'''
取前几个最大最小的数
'''
import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
