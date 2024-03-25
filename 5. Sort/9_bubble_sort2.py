# 개선된 버블정렬

def bubbleSort(array):
    n = len(array)
    비교횟수 = 0
    for end in range(n-1, 0, -1):
        changeYN = False    # 자리 변경 여부 저장 변수
        print("싸이클 ---> ", array)
        ################################ 버블 정렬 ######################################
        for current in range(0, end):
            비교횟수 += 1
            if array[current] > array[current+1]:
                array[current], array[current+1] = array[current+1], array[current] # 자리변경 시
                changeYN = True                                                     # True임
        ######################################################################
        # 자리 변경이 한번도 존재 하지 않았으면 정렬 끝난 상태
        # 버블정렬의 특이점 : 특정 싸이클(for문)에서 자리 변경이 없을 경우 정렬 완료, 끝난것
        if not changeYN:    # changeYN이 False라면          # 만약에 자리 변경이 있을 경우 다시 비교
            break           # 반복문 종료
    print("총 비교 횟수: ", 비교횟수)
    return array

dataArray = [ 188, 162, 168, 120, 50, 150, 177, 105 ]
print("정렬 전:", dataArray)
dataArray = bubbleSort(dataArray)
print("정렬 후:", dataArray)
