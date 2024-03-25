# 버블 정렬 구현
def BubbleSort(array):
    n = len(array)                                  # 배열의 길이
    for end in range(n-1, 0, -1):                   # end: 비교 끝지점 : 마지막 인덱스부터 0인덱스전까지 -1씩 감소 반복
        print("싸이클 ---> ", array)
        for current in range(0, end):               # current : 현재 비교대상 : 0번 인덱스부터 end까지 1씩 증가
            if array[current] > array[current + 1]: # 4. 현재 값이 다음값보다 더 크면   
                array[current], array[current + 1] = array[current + 1], array[current] # 교체
    return array

dataArray = [ 188, 162, 168, 120, 50, 150, 177, 105 ]
print("정렬 전:", dataArray)
dataArray = BubbleSort(dataArray)
print("정렬 후:", dataArray)

"""
    알고리즘[ = 순서도]
    [ 44 , 33 , 77 , 55 ]
    1. n = 4
        2. end = 3
            3. current = 0
                4. 44 > 33 : True : 교체        [ 33 , 44 , 77 , 55 ]
            3. current = 1
                4. 44 > 77 : False :
            3. current = 2
                4. 77 > 55 : True : 교체        [ 33 , 44 , 55 , 77 ]
        2. end = 2
            3. current = 0
                4. 33 > 44 : False
            3. current = 1
                4. 44 > 55 : False
        2. end = 1
            3. current = 0
                4. 33 > 44 : False
    ------------------------------------------------
    이런식으로면 비교를 3번 -> 2번 -> 1번 이런식으로 시간을 많이 잡아먹는다
"""