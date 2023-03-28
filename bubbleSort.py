#202135932 김세영 버블 정렬

import randomListCreator

def bubbleSort(list):
    print(list)
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if (list[j] > list[j + 1]):
                #변수 값 교환
                list[j], list[j + 1] = list[j + 1], list[j]
        print(list)

#실행
testList = randomListCreator.makeRandomList(20)
bubbleSort(testList)