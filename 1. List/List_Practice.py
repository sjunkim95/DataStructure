# 2일차 정리
# 자료구조 리스트
    # 1. 선형 리스트[ Linear List ] : 예제1 , 예제2
        # 1. 배열 [ ] 사용
        # 2. 인덱스 존재
        # 3. 검색 속도가 빠르다 .
    # 2. 싱글 연결리스트[ Signly Linked List ]  : 예제3 ,  예제4
        # 1. 노드 사용 [ 노드(클래스) 직접 구현 ]
        # 2. 인덱스 x -> link 사용
        # 3. 중간 삽입/삭제 빠르다.
    # 3. 원형 연결리스트[ Circular Linked List ]  : 예제5
        # 1. 싱글 연결리스트 와 매우 유사
        # 2. (차이점) END node like -> START node

# 과제 : 식당 웨이팅 프로그램 구현 [ 버전 : 1.선형리스트 버전  2. 연결리스트 버전 ]
    # 요구사항
        # 식당이 오픈 전
        # 1. 이름 , 전화번호 , 인원수 입력받는다 . [ 현재시간 자동 입력받기 ]
        # 2. 등록된 웨이팅을 리스트에 담는다 .
        # 3. 사용자에게 순서대기 번호 알려준다. [ 인덱스번호 혹은 노드 순서번호 ]
        # 변수 요구 : 이미 시간대 별로 웨이팅 이 존재하는데 중간에 예약이 된다..
        #       어플 예약 : 이름 , 전화번호 , 인원수 , 예약 시간 입력받는다 .
        #       어플 예약 등록 되었을때 예약 시간보다 더 큰 시간은 뒤로 한칸씩 대기번호 증가
        # 4. 관리자가 입장 하면  가장 앞에 있는 순서대기부터 삭제처리 한다. [ 한칸씩 인덱스,노드 당겨짐 ]
        # 예)
        #       강호동 030 3 1:13
        #       신동엽 010 2 2:20
        #                           어플 예약 : 유재석 020 2 1:30
        #       강호동 유재석 신동엽
        # 예)
        #     입장시 강호동부터 입장처리 [ 삭제 ]
        # 5. 1. 웨이팅 등록   2. [관리자]입장

# 1. 노드 클래스( 데이터, 링크 ) 선언
class Node():               # 1. Node라는 이름으로 클래스 선언
    def __init__(self):     # 2. Node 구조
        self.data = None    # 3. 필드1 = 데이터
        self.link = None    # 3. 필드2 = 링크

# 전역변수
head = None     # 가장 앞에 있는 노드
current = None  # 현재 위치 노드
pre = None      # 이전 위치 노드

# 손님 대기 등록함수
def add_customer( name ):

    global head, current, pre
    
    node = Node()
    node.data = name

    if head is None:
        head = node
        head.link = head  # 노드가 자기 자신을 가리키도록 설정
    else:
        current = head
        while current.link != head:
            current = current.link

        current.link = node  # 현재 마지막 노드의 링크를 새로운 노드로 설정
        node.link = head     # 새로운 노드가 첫 번째 노드를 가리키도록 설정
        head = node          # head를 새로운 노드로 업데이트

# 손님 입장 함수
def entrance_customer():
    global head

    if head is None:
        print("대기 중인 손님이 없습니다.")
        return

    print("(관리자) {} 님, 입장하십시오.".format(head.data))

    if head.link == head:
        # 대기 중인 손님이 한 명뿐인 경우
        del head
        head = None
    else:
        # 대기 중인 손님이 여러 명인 경우
        current = head
        while current.link != head:
            pre = current
            current = current.link

        pre.link = current.link  # 첫 번째 손님을 대기 목록에서 제거
        del current

    node_print()
        

# 노드 함수 출력
def node_print():
    global head, current, pre

    current = head
    while True:
        print(current.data)
        current = current.link
        if current == head:  # 현재 노드가 head일 경우 루프 종료
            break

def start() :
    while True :
        select = int( input( ' 1.(손님)대기 등록  2.[관리자]입장  3.종료하기 ') )
        if select == 1 :
            print("*(손님) 대기 등록 합1니다. *")
            name = str(input("손님 성함을 입력해주세요: "))

            add_customer( name )
            
        elif select == 2:
            print("*(관리자) 대기번호 1 입장. *")
            # 코드 작성 [ 함수 ]
            


        elif select == 3:
            print("*")
            # 코드 작성 [ 함수 ]
            node_print()
            break

        else :
            print("*알수 없는 번호입니다. 다시 입력해주세요~ ")
start()