# 1. 정렬이 없는 순차 검색 [ 중복검색 ] -> 리스트를 선언하라

# 중복 검색이 가능한 순차검색 정의
def seqSearch(array, fdata):
    poslist = []        # 검색된 여러개를 저장하기 위한 배열 선언
    size = len(array)
    for i in range(size):
        if array[i] == fdata:
            poslist.append(i)   # 동일한 데이터의 인덱스를 배열 저장
    return poslist # 검색된 여러개를 반환

# 전역변수
dataArray = [ 188 , 50 , 168 , 50 , 105 , 120 , 177 , 50 ]

# 입력받기
findData = int(input("검색할 데이터 : "))
position = seqSearch(dataArray, findData)

if position == []: # 만약에 반환된 배열이 비어 있으면
    print(findData, "가 없습니다.")
else: # 배열이 비어있지 않으면
    print(findData, "는", position, "번째 위치에 있음")