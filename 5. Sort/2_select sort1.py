# 선택 정렬 [ 최솟값 위치 찾기 ]
def findMinIdx( ary ):                  # 1. 함수에 인수로 배열 넣기
    minIdx = 0                          # 2. 최솟값 값의 인덱스 위치 저장하는 변수
    for i in range( 1, len(ary) ):      # 3. 배열길이만큼 반복문
        if (ary[minIdx] > ary[i]):      # 4. 만약에 해당 인덱스가 다음 인덱스보다 크면 ( > 최솟값, < 최댓값)
            minIdx = i                  # 5. 최솟값 인덱스 교체
    return minIdx                       # 최솟값 인덱스를 return 하는것

testary = [ 55, 83, 33, 77]
minpos = findMinIdx(testary)            # return 한 최솟값이 minpos에 담길것
print("최솟값 찾기 -----> ", testary[minpos])
"""
    알고리즘 [ = 순서도 ]
    1. ary[0] : 55 -> 2. 조건 : 55 > 88 false
                      2. 조건 : 55 > 33 true    3. mididx = 2 교체
                      2. 조건 : 33 > 77 false
"""
before = [ 188, 162, 168, 120, 50, 150, 177, 105 ]      # 정렬 전
after = [ ] # 정렬 후

print("정렬 전: ", before)

# 정렬 실행
for _ in range( len(before) ):          # 1. 배열 길이만큼 반복만
    minpos = findMinIdx(before)         # 2. 최솟값의 위치 찾기
    after.append(before[minpos])        # 3. 새로운 배열에 최솟값 넣기
    del(before[minpos])                 # 4. 기존 배열에서 최솟값 제거 [ 다음 최솟값 검색시 존재 X]
print("정렬 후: ", after)