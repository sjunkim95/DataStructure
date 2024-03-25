# 정렬 별 성능 차이
import random
import time
################### 퀵 정렬 ####################
def quickSort( ary ) :
    n = len( ary )
    if n <= 1 :
        return ary
    pivot = ary[ n//2 ]
    left , mid , right = [],[],[]       # 왼쪽 가운데 오른쪽
    for num in ary :
        if num < pivot :            #기준보다 더 작으면
            left.append(num)
        elif num > pivot :          #기준보다 더 크면
            right.append(num)
        else:                       #기준과 동일하면
            mid.append(num)
    return quickSort( left ) + mid +quickSort( right )
#############################################
################### 선택 정렬 ####################
def selectionSort( ary ) :
    n = len( ary )                      # 1. 배열=리스트 의 길이
    for i in range( 0 , n-1 ) :         # 2. 배열의 모든 인덱스 반복 [ 0 ~ 마지막인덱스까지 ]
        minIdx = i                      # 3. i = 비교기준
        for k in range( i+1 , n ) :     # 4. k = 비교대상
            if ary[minIdx] > ary[k] :   # 5. 만약에 비교기준이 더 크면 [ > : 오름차순 , < : 내림차순 ]
                minIdx = k              # 6. 최솟값 인덱스 교체
        # 교체
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary
#############################################
################### 삽입 정렬 ####################
def insertionsort( ary ) :
    n = len( ary )                          # 배열의 길이 변수
    for end in range( 1 , n ) :             # 인덱스 1부터 마지막 인덱스까지 반복
        for cur in range( end , 0 , -1 ) :  # end 부터 0까지 -1씩 감소 반복
            if ary[cur-1] > ary[cur] :      # 만약에 앞에 있는 인덱스보다 더 크면
                # tmp 없이 두 변수 교체방식
                ary[cur-1] , ary[cur]  = ary[cur] , ary[cur-1]
    return ary
#############################################
################### 버블 정렬 ####################
def bubbleSort( ary ) :
    n = len( ary )
    for end in range( n-1 , 0 , -1 ) :
        changeYN = False                # 자리 변경 여부 저장 변수
        print(" 싸이클 --> " , ary )
        ######################### 버블 정렬 #############################
        for cur in range( 0, end ) :
            if ary[cur] > ary[cur+1] :
                ary[cur] , ary[cur+1] = ary[cur+1] , ary[cur]   # 자리 변경
                changeYN = True     # true
        ############################################################
        # 자리 변경이 한번도 존재 하지 않았으면 정렬 끝난 상태
        # 버블정렬의 특이점 : 특정 싸이클에서 자리 변경이 한번도 없을경우 정렬 완료~~~~
        if not changeYN :   # 만약에 False         # 만약에 자리 변경이 있을경우 다시 비교
            break           # 반복문 종료
    return ary
#############################################
tempAry = [random.randint(10000,99999) for _ in range(10000) ]
start = time.time()
print( "퀵정렬 : " , quickSort(tempAry) )
end = time.time()
print( "퀵정렬의 소요시간 %10.3f 초  " % (end-start) )

start = time.time()
print( "선택정렬 : " , selectionSort(tempAry) )
end = time.time()
print( "선택정렬 소요시간 %10.3f 초  " % (end-start) )

start = time.time()
print( "삽입정렬 : " , insertionsort(tempAry) )
end = time.time()
print( "삽입정렬 소요시간 %10.3f 초  " % (end-start) )

start = time.time()
print( "버블정렬 : " , bubbleSort(tempAry) )
end = time.time()
print( "버블정렬 소요시간 %10.3f 초  " % (end-start) )