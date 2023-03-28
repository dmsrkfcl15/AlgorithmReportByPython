#202135932 김세영 퀵 정렬

import randomListCreator

def quickSort(list, p, r):
    if(p < r):
        x = list[r]
        i = p-1
        for j in range(p, r):
            if(list[j] < x):
                i += 1
                list[i], list[j] = list[j], list[i]
        
        i += 1
        list[i], list[r] = list[r], list[i]

        #현재 i는 중심의 위치
        quickSort(list, p, i-1)
        quickSort(list, i+1, r)



#실행
testList = randomListCreator.makeRandomList(20)
print(testList)
quickSort(testList, 0, 19)
print(testList)