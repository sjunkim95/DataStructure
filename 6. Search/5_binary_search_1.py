# 이진검색 구현
def binarySearch(array, fdata):
    pos = -1                        # 검색된 결과의 인덱스 저장하는 변수
    start = 0                       # 시작 인덱스 변수
    end = len(array)-1              # 끝 인덱스 변수

    while start <= end:             # start부터 end까지 반복처리
        mid = (start+end) // 2      # 가운데 인덱스 구하기
        if fdata == array[mid]:     # 가운데 인덱스가 찾는 데이터와 같으면
            return mid              # 찾기 성공
        elif fdata > array[mid]:    # 만약에 찾는 데이터가 더 크면 mid + 1
            start = mid + 1         # 가운데 인덱스 1 증가 -> start를 mid로 사용
        else:                       # 만약에 찾는 데이터가 더 작으면
            end = mid - 1           # 가운데 인덱스 1 감소 -> start를 mid로 사용
    return pos
"""
    finddata = 168
    start = 0
    end = 9
                        mid = 4
               mid - 3           mid = 5

            만약에 더 크면      start = 5 end = 9 mid = 7
            만약에 더 작으면    start = 0 end = 3 mid = 1

    순서
        50 , 60 , 105 , 120 , 150 , 160 , 162 , 168 , 177 , 188

        150 [mid], 188 [end]
        start = mid+1 -> 160
        다시 돌리면
        -> mid = 7 -> 167[7]


"""


# 전역변수
# 정렬이 되어있는 배열
dataArray = [ 50 , 60 , 105 , 120 , 150 , 160 , 162 , 168 , 177 , 188 ]
finddata = int(input("검색할 데이터 : "))
position = binarySearch(dataArray, finddata)

if position == -1:
    print(finddata,"가 없습니다.")
else:
    print(finddata,"는", position,"위치에 있음")
