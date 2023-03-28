#202135932 김세영 삽입 정렬

import randomListCreator

def insertionSort(list):
    print(list)
    for i in range(len(list)):
        for j in range(i, 0, -1): # i부터 1까지 반복, i=0일때, 즉 정렬된 구간이 하나인 경우 이미 정렬되어 있으므로 수행하지 않는다
            if (list[j] < list[j - 1]):
                #변수 값 교환
                list[j], list[j - 1] = list[j - 1], list[j]
            else:
                break
        print(list)

#실행
testList = randomListCreator.makeRandomList(20)
insertionSort(testList)