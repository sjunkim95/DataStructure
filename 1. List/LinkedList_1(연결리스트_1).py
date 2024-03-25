# 선형리스트 [ Linear List ]
# 연결리스트 [ 1. 싱글 연결리스트( Singly Linked List) 2. 원형 연결리스트]

# 선형 vs 연결리스트
    # 1. 순서대로 vs 연결식
    # 2. 인덱스 사용 vs 노드 사용
        # 인덱스 형식 : [1, 2, 3, 4]
            # 2-1. 인덱스(저장되는 순서) 이용한 검색 속도 빠름
            # 2-2. 추가 빠름
        # 노드 형식: 1 --> 2 --> 3 --> 4
            # 2-2. 연결형식: 중간 삽입/삭제 빠름
    # 3. 서로 인덱스 간 메모리 위치 근접 vs 서로 메모리 위치 무관

# 시나리오
    # 1. 연결리스트 노드 방식 사용

# 1. 노드 클래스( 데이터, 링크 ) 선언
class Node():               # 1. Node라는 이름으로 클래스 선언
    def __init__(self):     # 2. Node 구조
        self.data = None    # 3. 필드1 = 데이터
        self.link = None    # 3. 필드2 = 링크

# 2. 데이터 추가
node1 = Node()                                      # 객체 선언
node1.data = "유재석"                               # 첫번째 노드 선언 [ 연결 리스트 시작 위치 = head ]
#print( node1.data, end=' ')                         # 헤더 출력

node2 = Node()
node2.data = "강호동"
node1.link = node2                                  # head.링크 ---> 강호동
#print( node1.link.data, end=' ')                    # 헤더의 링크 출력

node3 = Node()
node3.data = "신동엽"
node2.link = node3                                  # 강호동 링크 ---> 신동엽
#print( node1.link.link.data, end = ' ')             # 헤더의 링크 -> 링크 출력

node4 = Node()
node4.data = "서장훈"
node3.link = node4                                  # 신동엽 링크 ---> 서장훈
#print( node1.link.link.link.data, end = ' ')        # 헤더의 링크 -> 링크 -> 링크 출력

node5 = Node()
node5.data = "김희철"
node4.link = node5                                  # 신동엽 링크 ---> 서장훈
#print( node1.link.link.link.link.data, end = ' ')   # 헤더의 링크 -> 링크 -> 링크 -> 링크 출력

# 모든 노드 출력
def node_print():
    current = node1
    print(current.data, end=' ')
    while current.link !=None: # 헤더의 링크가 없을때까지 반복
        current = current.link
        print(current.data, end=' ')

node_print()

# 중간 노드 삽입 [ 3번에 하하 데이터 ]
newnode = Node()
newnode.data = '하하'
    # 유재석 -> 강호동 -> 신동엽 -> 서장훈 -> 김희철
    #
    #               newnode: 하하
    #
newnode.link = node2.link   # 강호동이 갖고있는 신동엽 link를 하하에게 전달
node2.link = newnode        # 강호동은 하하의 주소(link)를 가진다

node_print() # 유재석 -> 강호동 -> 하하 -> 신동엽 -> 서장훈 -> 김희철

# 중간 노드 삭제 [ 4번에 신동엽 데이터 ]
# 유재석 -> 강호동 -> 하하 -> 신동엽[X] -> 서장훈 -> 김희철

newnode.link = node3.link   # 신동엽이 가지고 있던 서장훈 주소(링크)를 하하에게 대입
del(node3)                  # 신동엽 메모리 초기화

node_print() # 유재석 강호동 하하 서장훈 김희철
