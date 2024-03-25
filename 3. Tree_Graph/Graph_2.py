# 최단거리 찾기 [ 그래프 구현 ]
    # 조건: 춘천, 서울, 속초, 대전, 광주, 부산
    # 조건: 지역 이동간 걸리는 시간 [ 임의 ]
    # 문제: 춘천 --> 부산까지의 최단거리

# 1. 그래프 클래스 선언 [ 2차원 리스트를 이용한 그래프 구현 ]
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.Graph = [ [0 for _ in range(size)] for _ in range(size) ]

# 그래프 출력 함수
def graph_print( g ):
    print("   ", end=" ")                   # 1. 첫번째 출력 줄 (가로 제목 출력)
    for v in range( g.SIZE ):               # 지역개수만큼 반복문
        print(LocationList[v], end=" ")
    print()
    for row in range( g.SIZE ):
        print(LocationList[row], end=" ")   # 2. 세로제목 출력 부분
        for col in range( g.SIZE ):
            print("%3d" % g.Graph[row][col], end=" ")
            # %3d: 정수 세자리 자리차지
                # 정수 세자리가 아닐경우 공백으로 채움
            # %03d : 정수 세자리 차지
                # 정수 세자리가 아닐경우 0으로 채움
        print()
    print()

# 2. 전역변수
G1 = None
LocationList = ["춘천", "서울", "속초", "대전", "광주", "부산"]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5       # 인덱스 번호 미리 넣어둔 것

# 3. 실행
LocationSize = len(LocationList)    # Graph()에서 size에 할당할 길이 선언
G1 = Graph(LocationSize)

# 지역 이동간 걸리는 시간 [ 임의 설정 ]
G1.Graph[춘천][서울] = 10; G1.Graph[춘천][속초] = 15
G1.Graph[서울][춘천] = 10; G1.Graph[서울][속초] = 40; G1.Graph[서울][대전] = 11; G1.Graph[서울][광주] = 50
G1.Graph[속초][춘천] = 15; G1.Graph[속초][서울] = 40; G1.Graph[속초][대전] = 12
G1.Graph[대전][서울] = 11; G1.Graph[대전][속초] = 12; G1.Graph[대전][광주] = 20; G1.Graph[대전][부산] = 30
G1.Graph[광주][서울] = 50; G1.Graph[광주][대전] = 20; G1.Graph[광주][부산] = 25
G1.Graph[부산][대전] = 30; G1.Graph[부산][광주] = 25

# 지역별 고속도로간 걸리는 시간 출력
graph_print(G1)

# 가중치 간선
edgeList = []   # 고속도로가 존재하는 거리만 리스트 선언
for i in range(LocationSize):
    for k in range(LocationSize):
        if G1.Graph[i][k] != 0:     # 거리가 존재한다면 (즉, 0이라는건 고속도로가 없다)
            edgeList.append([G1.Graph[i][k], i, k])
                            # 걸리는 시간, 출발지, 도착지
            
print("정렬 전: ", edgeList)

# 정렬 [ 정렬 클래스를 이용한 정렬 ]
from operator import itemgetter
edgeList = sorted(edgeList, key=itemgetter(0), reverse=True)
        # sorted(리스트, key=itemgetter(인덱스), reverse=True: 내림차순 / 생략시 오름차순이 됨)
                        # 즉 [G1.Graph[i][k], i, k] 중에서 누구를 인덱스를 쓰고싶냐

print("정렬 후(이동시간): ", edgeList)

# 무방향은 대칭관계 so -> 단방향으로 본다
newarray = []
for i in range(0, len(edgeList), 2): # 0 인덱스부터 마지막인덱스까지 2씩 증가 (즉, 왕복으로 돌아오는건 안보고, 편도로만 보겠다)
    newarray.append(edgeList[i])

print(newarray)     # 단방향 리스트 생성

# 거리 계산 함수
def find_distance(g, location):
    stack = []              # 지점을 지나는 스택
    visited_array = []      # 방문한 지역

    current = 0             # 시작 지점
    stack.append(current)
    visited_array.append(current)

    while(len(stack) != 0):
        next = None # 다음 지점 선언
        for var in range(LocationSize):
            if g.Graph[current][var] != 0:
                if var in visited_array: # 방문한 적이 있는 지점이면 (x)
                    pass
                else:                    # 방문한 적이 없으면 (next = var)
                    next = var           # 다음에 방문하겠다 추가
                    break
        if next != None:                 # 다음에 방문할 지점이 있을 경우
            current = next               # 현재위치를 다음위치로 바꿈
            stack.append(current)           # 스택에도 추가
            visited_array.append(current)   # 방문목록에 기록을 남김
        else:                            # 다음에 방문할 지점이 없을경우
            current = stack.pop()
    
    if location in visited_array:
        return True
    else:
        return False
    
# 거리 계산
index = 0   # 거리 순서의 변수
while  (len(newarray) > LocationSize-1):        # 간선의 개수가 마지막 지역까지 반복처리
    start = newarray[index][1]              # 출발지
    end = newarray[index][2]                # 도착지
    saveCost = newarray[index][0]           # 걸리는 시간

    G1.Graph[start][end] = 0                # 초기값 설정    
    G1.Graph[end][start] = 0

    startYN = find_distance(G1, start)
    endYN =  find_distance(G1, end)

    if startYN and endYN:
        del(newarray[index]) # -> start와 end가 같다면 추가할필요 X
    else:                    # 하나라도 True 라면 진행한다, 즉, False라면
        G1.Graph[start][end] = saveCost
        G1.Graph[end][start] = saveCost
        index += 1
    
print("춘천 ---> 부산까지의 최단 거리 : ")
graph_print(G1)

"""
# 문제: 춘천 --> 부산까지의 최단거리

            춘천
        10        15
    서울     40     속초
        11        12
    50      대전
        20        30
    광주     25     부산
"""
