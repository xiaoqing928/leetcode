'''
直接构建大顶堆不容易，可以考虑两种间接实现的方法。
1.push的时候将数值取反，取出的时候再取反即可
2.面向对象，在堆中传入一个对象，重载比较的规则即可
下面是第二种方式的实现
'''
import heapq

class MinHeap():
    def __init__(self, p):
        self.p = p
    def __lt__(self, other):
        return self.p < other.p

class MaxHeap():
    def __init__(self, p):
        self.p = p
    def __lt__(self, other):
        return self.p > other.p

list1 = [4,5,6,1,2,3]
min_heap = []
max_heap = []
for i in list1:
    heapq.heappush(min_heap, MinHeap(i))
    heapq.heappush(max_heap, MaxHeap(i))
# 将堆打印出来（这个里面不一定是排序的，只是堆，满足堆的特性）
for i in min_heap:
    print(i.p)
for i in max_heap:
    print(i.p)
#堆排序输出
while min_heap:
    print('小根堆:',heapq.heappop(min_heap).p)
while max_heap:
    print('大根堆:',heapq.heappop(max_heap).p)