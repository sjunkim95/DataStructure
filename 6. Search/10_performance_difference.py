# 순차검색 vs 이진검색 성능차이
# 생각해보기
# 1. 난수 100만개 저장되어 있는 배열
# 2. 순차검색 [ 비정렬 ] 이용한 검색 ( 비교 횟수 출력 )
# 3. 순차검색 [ 정렬 ] 이용한 검색 ( 비교 횟수 출력 )
# 3. 이진검색 [ 정렬 ] 이용한 검색 ( 비교 횟수 출력 )

# 전역변수
import random

# 순차검색 구현
def seqSearch(array, fdata):
    global count
    pos = -1
    for i in range(len(array)):
        count += 1
        if array[i] == fdata:
            pos = i
            break
    return pos

# 이진검색 구현
def binarySearch(array, fdata):
    global count
    start = 0
    end = len(array)-1
    while(start <= end):
        count += 1
        mid = (start+end) // 2
        if fdata == array[mid]:
            return mid
        elif fdata > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

dataArray, sortedArray = [], []
findData = 9000
count = 0

dataArray = [ random.randint(0 , 999999) for _ in range(1000000) ]
dataArray.insert( random.randint(0 , 1000000) , findData )
sortedArray = sorted( dataArray )

# 배열내 앞에 5개와 뒤에 5개 출력
print("비정렬 배열(순차검색) ---> ", dataArray[0:5], "~~~", dataArray[-5:len(dataArray)])
print("정렬 배열 --->", sortedArray[0:5], "~~~",sortedArray[-5:len(dataArray)])

# 성능 비교
# 순차검색 [ 비정렬 ]
count = 0
pos = seqSearch(dataArray, findData)
if pos != -1:
    print("순차검색[비정렬 데이터] ---> ",count,"회")

# 순차검색 [ 정렬 ]
count = 0
pos = seqSearch(sortedArray, findData)
if pos != -1:
    print("순차검색[정렬 데이터] ---> ",count,"회")

# 이진검색
count = 0
pos = binarySearch(sortedArray, findData)
if pos!= -1:
    print("이진검색[정렬 데이터] --->", count, "회")
