# 1. 정렬이 있는 순차 검색 [ 중복 허용 ]

# 정렬이 되어있는 배열의 순차검색 정의
def seqSearch(array, fdata):
    pos = -1
    poslist = []
    size = len(array)
    for i in range(size):
        if array[i] == fdata:
            pos = i
            # poslist.append(i) -> 중복값 찾을때 사용하는 것
            break
        elif array[i] > fdata: # -> i번째 값이 내가 찾고자 하는 값보다 크다면~ break
            break
    return pos

# 전역변수
dataArray = [ 188 , 50 , 168 , 50 , 105 , 120 , 177 , 50 ]

# 정렬하기
dataArray.sort() # 오름차순

# 입력받기
findData = int(input("검색할 데이터 : "))
position = seqSearch(dataArray, findData)

if position == -1: # 만약에 반환된 배열이 비어 있으면
    print(findData, "가 없습니다.")
else: # 배열이 비어있지 않으면
    print(findData, "는", position, "번째 위치에 있음")