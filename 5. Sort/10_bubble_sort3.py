# 난수 0~200 사이의 20개 생성 -> 내림차순 정렬
# 몇번 정렬이 이뤄 졌는지 정렬 횟수 출력

import random

def bubbleSort(array):
    global count
    for end in range(len(array)-1, 0, -1):
        changeYN = False
        for current in range(0, end):
            count += 1
            if array[current] > array[current+1]:
                array[current], array[current+1] = array[current+1], array[current]
                changeYN = True
        if not changeYN: # 이 부분을 빼도 정렬은 똑같음, 하지만 쓰는 이유는 정렬 횟수를 줄이기 위해서
            break
    return array

count = 0
dataArray = [ random.randint(0,200) for _ in range(10) ]
print("정렬 전:", dataArray)
dataArray = bubbleSort(dataArray)
print("정렬 후:", dataArray)
print("정렬 횟수: ", count)