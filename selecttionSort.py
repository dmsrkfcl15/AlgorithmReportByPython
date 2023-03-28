#202135932 김세영 선택 정렬

import randomListCreator

def selecttionSort(list):
    print(list)
    for i in range(len(list)): #list의 수만큼 반복
        maxNumindex = 0
        for j in range(len(list) - i):
            if (list[maxNumindex] < list[j]):
                maxNumindex = j

        #변수 값 교환, 마지막 자리에 가장 큰 값 저장
        list[-i], list[maxNumindex] = list[maxNumindex], list[-i]

        print(list)

#실행
testList = randomListCreator.makeRandomList(20)
selecttionSort(testList)

