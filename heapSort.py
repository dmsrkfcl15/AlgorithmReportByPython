#202135932 김세영 힙 정렬
#오름차순으로 구현하기 위해 교과서 내용을 반대로 적용해 최대힙으로 구현

import math
import randomListCreator

def heapify(list, k, n):
    leftNode, rightNode = k * 2, k * 2 + 1
    if rightNode <= n: #양쪽 자식이 다 있는 경우
        if list[leftNode] > list[rightNode]:
            largerNode = leftNode
        else: #왼쪽 자식만 있는 경우
            largerNode = rightNode
    elif leftNode <= n:
        largerNode = leftNode
    else: #리프 노드인 경우
        return
    
    if list[k] < list[largerNode]:
        list[k], list[largerNode] = list[largerNode], list[k] #값 교환
        heapify(list, largerNode, n)


def buildHeap(list, n):
    for i in range(math.floor(n / 2), 0, -1):
        heapify(list, i, n)


def heapSort(list, n):
    buildHeap(list, n)
    print(list)
    for i in range(n, 1, -1): #n부터 2까지 반복
        list[i], list[1] = list[1], list[i] #값 교환
        heapify(list, 1, i-1)



#실행
testList = randomListCreator.makeRandomList(20)
testList.insert(0, 0) #heap에서는 인덱스를 1부터 다루어야 편하지만 파이썬에선 0부터 시작하기 때문에 가장 앞 자리에 의미없는 숫자인 0을 삽입했음
print(testList)
heapSort(testList, 20)
print(testList)