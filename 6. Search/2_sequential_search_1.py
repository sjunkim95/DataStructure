# 1. 정렬이 없는 순차 검색

# 순차검색 함수 정의 [ for문 이용한 ]
def seqSearch(array, fdata): # 인수: 배열, 검색데이터
    pos = -1                    # 검색 성공시의 인덱스 위치로 사용할 변수 [ -1: 없다 ]
    size = len(array)           # 배열의 사이즈
    for i in range(size):       # 배열의 길이만큼 반복
        if array[i] == fdata:   # i번째 인덱스의 데이터와 검색데이터가 같으면
            pos = i             # [동일한] 검색한 데이터의 인덱스를 저장
            break               # 검색 성공시 바로 검색 종료
    return pos

# 전역변수
dataArray = [ 188 , 150 , 168 , 162 , 106 , 120 , 177 , 50 ]

# 입력받기
findData = int(input("검색할 데이터 : "))
position = seqSearch(dataArray, findData)

if position == -1: # -1이면 인덱스 없다
    print(findData, "가 없습니다.")
else: # 검색 성공
    print(findData, "는", position, "번째 위치에 있음")