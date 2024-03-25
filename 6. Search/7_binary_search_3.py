# 판매제품별 판매수량의 정렬과 검색
import random

def binarySearch(array, fdata):
    start = 0
    end = len(array)-1

    while (start<=end):
        mid = (start+end)//2
        if fdata == array[mid]:
            return mid
        elif fdata > array[mid]:
            start = mid + 1
        else:
            end = mid -1
    return -1

# 전역변수
# 제품 목록
dataArray = ['나이키', '아디다스', '리복', '휠라', '뉴발란스', '언더아머']

# 제품목록 20개의 랜덤으로 판매
sellArray = [ random.choice(dataArray) for _ in range(20) ]

print("중복O 정렬X", sellArray)
sellArray.sort()
print("중복O 정렬O", sellArray)

# 중복제거
sellProduct = list(set(sellArray)) # set에는 동일한 데이터를 넣을 수 없다 [ 중복제거 ]
print("중복X", sellProduct)

# 만약에 나이키 3개 중복이면 (나이키:3) -> 이진 탐색 이용

countList = [] # 제품별 판매수량 배열 [ 리스트 ]
for product in sellProduct: # 판매목록 반복문 실행
    count = 0               # 제품별 판매수량 저장되는 변수
    pos = 0                 # 검색된 결과의 인덱스 저장되는 변수
    while pos != -1:        # 찾을 데이터가 없을때까지 [ 검색결과가 없을때 까지 반복 ]
        pos = binarySearch(sellArray, product) # (판매목록, 검색제품)함수에 넣고. 중복제거(검색제품for문)된 리스트에서 -> 기존 리스트로 가서 중복 체크하는것
        if pos != -1:       # 검색을 성공했다면, -1이 아니라는것 -> 찾았다는 것
            count += 1      # 판매수량 증가
            del(sellArray[pos]) # 검색된 데이터는 판매목록에서 제거
    countList.append((product,count)) # 해당 제품의 검색이 끝났을때 제품별 판매수량 배열에 추가

print("결산 결과", countList)