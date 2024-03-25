#  퀵 정렬 구현 함수
def quickSort(array):
    n = len(array)          # 1. 배열 = 리스트의 길이
    if n <= 1:              # 만약에 배열의 길이가 1이면
        return array        # 종료
    pivot = array[ n//2 ]   # 2. ** 기준값을 중간에 있는 값으로 선정
        # 0 1 2         -> 3//2 -> 1
        # 0 1 2 3 4     -> 4//2 -> 2
        # 0 1 2 3 4 5   -> 5//2 -> 2
    left = []       # 기준보다 작은 데이터
    right = []      # 기준보다 큰 데이터

    for num in array:
        if num < pivot: # 기준보다 작으면
            left.append(num)
        elif num > pivot: # 기준보다 크면
            right.append(num)
    return quickSort(left) + [pivot] + quickSort(right)     # 재귀를 이용한 재 정렬

dataArray = [ 188, 162, 168, 120, 50, 150, 177, 105 ]
print("정렬 전:", dataArray)
dataArray = quickSort(dataArray)
print("정렬 후:", dataArray)

"""
    퀵정렬 : 기준점(가운데값) 기준, 왼쪽/오른쪽 배치
    [ 44 , 66 , 77 , 33 , 55 ]
    1. 가운데 값: 77
        2. left = [ 44 , 66 , 33 , 55 ]
        2. right = [ ]
            3. 재귀함수(left)
            [ 44 , 66 , 33 , 55 ]
            가운데값: 66
            2. left = [ 44 , 33 , 55 ]
            2. right = []
                3. 재귀함수(left)
                [ 44 , 33 , 55 ]
                가운데: 33
                2. left =  []
                2. right = [ 44 , 55 ]
                    3. 재귀함수(right)
                    [ 44 , 55 ]
                    가운데 : 55
                    left[ 44 ]
    ------------------------------------------------------------------
                    [ 44 , 66 , 77 , 33 , 55 , 88 ]
                                77
        [ 44 , 66 , 33 , 55 ]       [ 88 ]
                    66                88
    [ 44 , 33 , 55]     [ ]
            33
    [  ]        [ 44 , 55 ]
                      55
                [ 44 ]   [ ]
    * 가장 왼쪽에 있는 값이 가장 작은 수
    [ 33 , 44 , 55 , 66 , 77 , 88 ]
"""