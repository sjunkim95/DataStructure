# 구현 프로그램 : 회원들의 전화번호부
    # 1. 연결리스트 구현

# 1. 노드 클래스 선언
class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 2. 노드 추가 함수 구현
def add_node( info ):

    # 전역변수 호출
    global head, current, pre

    node = Node()       # 1. 노드 객체 선언
    node.data = info    # 2. 노드에 데이터[입력받은 정보] 추가
    # 2-1.
    if ( head == None ) :   # 만약에 헤드가 없으면 [ 첫 노드 생성!!! ]
        head = node         # 방금 만들어진 노드를 헤드 노드로 설정
        return              # 함수 종료
    
    # 2-2. 이름으로 정렬할시 [0], 전화번호 정렬시에는 [1] (여기서는 head만 바꿔주는것)
    if head.data[0] > info[0] : # 만약에 헤드노드내 이름이 새로 입력받은 노드의 이름보다 크면 (반대로하면 내림차순)
        node.link = head        # 헤드 노드 교체
        head = node          
        return
    # head강호동 > new 신동엽
    # new신동엽 -> 강호동
    # head = 새로운 노드
    
    # 2-3. 이름으로 정렬할시 [0], 전화번호 정렬시에는 [1]
    current = head              # 현재위치노드 = 헤드노드 [ 헤드부터 검사 ]
    
    while current.link != None :        # 만약에 마지막 노드까지 반복처리
        pre = current                   # 이전노드에 현재노드 대입
        current = current.link          # 현재 노드에 다음노드 대입
        if current.data[0] > info [0]:  # 만약에 다음노드와 새로입력받음 비교
            pre.link = node             # 이전노드에 새로운 노드
            print(pre.link) # print로 중간중간 확인하라
            node.link = current         # 새로운노드 -> 다노드
            return
        # head 강호동 -> 하하
        # new 신동엽
            # current = head강호동
            # pre = 강호동, pre.link=하하      # current 하하
        # 하하 > 신동엽
            # pre.link = 신동엽
            # 신동엽.link = 하하
        # 강호동 -> 신동엽 -> 하하
    
    # 2-4. 그외 [ 마지막 노드에 새로운 노드 추가 ]
    current.link = node         # 헤드는 다음 노드
    
# 3. 노드 출력 함수 구현
def node_print():
    current = head
    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()

# 전역변수
head = None     # 가장 앞에 있는 노드
current = None  # 현재 위치 노드
pre = None      # 이전 위치 노드

# 메인 코드 실행
if __name__ == "__main__":
    while True:
        name = input("회원명 : ")                       # 1. 이름 입력받기
        if name == "" or name == None:  # 만약에 입력받은 데이터 없으면
            print("정확한 회원명을 입력해주세요! ")
            continue

        phone = input("연락처 : ")                      # 2. 전화번호 입력받기
        add_node( (name, phone) )                       # 튜플 ( 이름, 전화번호 ) 노드추가 함수로 전달
        node_print()                                    # 모든 노드 함수 출력

