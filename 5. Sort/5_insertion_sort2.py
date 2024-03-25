# 삽입정렬 Insertion Sort

def insertionSort(array):
    n = len(array)                                      # 배열의 길이 변수
    for end in range(1, n):                             # 인덱스 1부터 마지막 인덱스까지 반복
        for current in range(end, 0, -1):               # 마지막 인덱스(end)부터 0까지 -1씩 감소 반복
            if array[current-1] > array[current]:       # 만약에 앞에 있는 인덱스보다 더 크면 치환을 한다. 
                # temp 없이 두 변수 교체/치환하는것
                array[current-1], array[current] = array[current], array[current-1]
    return array

dataarray = [188, 162, 268, 120, 50, 150, 177, 105]

print("정렬 전 ---->", dataarray)
dataarray = insertionSort(dataarray)
print("정렬 후 ---->", dataarray)

"""
    알고리즘 [ 순서도 ]
    [ 55 , 77 , 66 ]
    1. n = 3
        2. end = 1 일때
            3. current = 1
                4. 55(인덱스 0) > 77(인덱스 1) False  -> 교체 x
            3. current = 0
        2. end = 2 일때
            3. current = 2
                4. 77 > 66 -> True -> 교체 o
            3. current = 1
                4. 55 > 66 -> False -> 교체 x
"""