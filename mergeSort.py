#202135932 김세영 병합 정렬

import math
import randomListCreator

def mergeSort(list, p, r):
    if(p < r):
        q = math.floor((p + r) / 2)
        mergeSort(list, p, q)
        mergeSort(list, q+1, r)
        #병합
        i, j = p, q+1
        tmpList = []
        while i <= q and j <= r:
            if list[i] > list[j]:
                tmpList.append(list[j]) #새로운 리스트 끝에 작은 것부터 삽입
                j += 1
            else:
                tmpList.append(list[i])
                i += 1
        
        while i <= q:
            tmpList.append(list[i])
            i += 1

        while j <= r:
            tmpList.append(list[j])
            j += 1

        i = p
        for num in tmpList:
            list[i] = num
            i += 1



#실행
testList = randomListCreator.makeRandomList(20)
print(testList)
mergeSort(testList, 0, 19)
print(testList)