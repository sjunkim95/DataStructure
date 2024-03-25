# 문제1 : 이진검색 이용한 수 찾기
"""
    1. N개의 정수 가 주어져 있을때 , 이 안에 X 라는 정수가 존재하는지 체크
    2. 입력 [ 1~100 사이 ]
        1.첫째 줄에 N의 자연수 입력
        2.두번째 줄에는 N개의 난수 생성
        3.세번째 줄에는 검색할 M 입력받기
    3. 출력
        1.네번째 줄에는 존재 여부 판단  [ 존재하면 1 존재하지않으면 0 ]
"""
import random

def binSearch( ary , fdata ) :
    start = 0
    end = len( ary ) -1
    while ( start<=end ) :
        mid = ( start + end ) // 2
        if fdata == ary[mid] :
            return 1
        elif fdata > ary[mid] :
            start = mid+1
        else:
            end = mid-1
    return 0

N = int(input())    # 1. N 이라는 자연수 입력받기
arr = [ random.randint(1,100) for _ in range(N) ]  # 2. N 만큼 난수 생성
arr.sort()  # 3. 정렬한다.
print( arr )
M = int( input() ) # 4. 검색할 자연수 입력받기
print(  binSearch( arr , M) ) # 5. 이진탐색 결과