"""
자료구조: Data를 효율적으로 저장하는 방법

    현재까지 공부: 리스트, 스택, 큐, 트리, 그래프

    1. 선형 데이터 구조
        * 리스트(List), 스택(Stack), 큐(Queue)
        1. 순서대로 저장
        2. 단일 레벨
        3. 단순한 

    2. 비선형 데이터 구조
        * 트리, 그래프
        1. 요소 사이에 관계 저장
        2. 다단계 레벨
        3. 복잡한

    트리 : 비선형 데이터 자료구조 <---> 스택/큐
        1. 계층적 관계를 표현
            예) 조직도, 컴퓨터 폴더 등
    
    이진트리 : 나무를 거꾸로 뒤집어 놓은 형태 / 부모노드가 2개의 자식노드 가짐
        1. 뿌리(root)는 하나만 존재한다! [ 레벨 0 ]
        2. 노드(node)
            1. 부모노드(parent node): 부모노드 1개당 2개의 자식 노드(LEFT, RIGHT) 가짐
            2. 자식노드(child node):
                1. 왼쪽 노드 : 부모노드 보다 데이터 작으면 왼쪽 노드
                2. 오른쪽 노드 : 부모노드 보다 데이터 크면 오른쪽 노드
        3. 이진트리 종류
            1. 포화(FULL) 이진 트리: 모든 노드가 존재한 상태
            2. 완전(complete) 이진 트리: 일부 노드가 비어 있어도 되는 노드 [ 마지막 노드 비어있는 상태 ]
            3. 편향(skewed) 이진 트리: 왼쪽 혹은 오른쪽으로 노드가 존재하는 상태
            4. 일반 이진 트리: 그외

                        root                                ---- LEVEL 0 
            PN                      PN                      ---- LEVEL 1
        lCN      rCN             CN       CN                ---- LEVEL 2
    CN    CN

        4. 순회 종류
            1. 전위 순회
            2. 중위 순회
            3. 후위 순회
"""

""" 
~~~참고
클래스와 인스턴스 차이

    1. class: 클래스
        + 목적: 대량 생산 (ex. 아파트, 공장기계처럼)
        컴퓨터가 이해할 수 있는 설계도 [ 컴퓨터는 피로도 X ]

    2. instance: 인스턴스
        + 클래스 기반으로 메모리(DATA) 할당되는 형태

    3. object: 객체
        + 클래스 기반으로 생성된 형태
    
    * 예) 자동차
        클래스 : 자동차[ 설계만 되어있는 상태 ]
            CLASS 클래스명() :

        객체 : 클래스로 선언된 변수                                 [ 스택(STACK) 메모리 ]
            클래스명 변수 =    
        인스턴스: 클래스로 선언된 변수에 메모리 할당된 것           [ 힙(HEAP) 메모리 ]
            변수 = 클래스명()
"""

# 이진트리 구현
# 1. 이진트리형 노드 클래스( 설게도: 미리 구성된 필드(메모리) ) 선언
class TreeNode():        # 1. 클래스 선언
    def __init__(self) : # 2. 객체 초기값 [객체 생성시 기본값] 설정
        
        self.left = None    # 1. 왼쪽 자식 노드
        self.data = None    # 본인 데이터 필드
        self.right = None   # 2. 오른쪽 자식 노드

# 2. 노드 객체 생성
"""
TreeNode node1 =                # 선언된 상태가 객체
TreeNode node2 = TreeNode()     # 선언된 상태에 메모리 할당해주는것이 인스턴스

하지만, 파이썬에서는 이런 구조를 사용 X -> TreeNode가 자동적으로 들어가
"""
# 1번노드
node1 = TreeNode()  # 해당 클래스로 인스턴스화 된 객체
node1.data = "유재석"

# 2번노드
node2 = TreeNode()
node2.data = "강호동"

# 두번째 노드는 첫번째 노드의 자식노드
node1.left = node2  # 유재석 노드의 왼쪽 자식노드를 강호동 노드로 대입

# 3번노드
node3 = TreeNode()
node3.data = "신동엽"
node1.right = node3 # 유재석 노드의 오른쪽 자식노드를 신동엽 노드로 대입

"""
            유재석(parent)
    강호동(LCN)            신동엽(RCN)
"""
# 4번노드
node4 = TreeNode()
node4.data = "서장훈"
node2.left = node4

# 5번노드
node5 = TreeNode()
node5.data = "김희철"
node2.right = node5

# 6번노드
node6 = TreeNode()
node6.data = "하하"
node3.left = node6

"""
    노드객체: LEFT   DATA    RIGHT  => 이렇게 3개가 '하나 노드'라고 취급한다

                    node2 주소 / 유재석 / node3주소                         => Level 0 (유재석이 '하나의 노드'가 되는것)
    
    node4주소/ 강호동 / node5주소      node6주소 / 신동엽 / (X)             => Level 1 (강호동이 '부모'노드이자 '자식'노드가 되는것)
    
x / 서장훈 / x     x / 김희철 / x    x / 하하 / x
"""
# 3. 출력
print(node1.data, end=" ")
print()
print(node1.left.data, node1.right.data, end = " ")
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end = " ")
print()

# 4. 트리 순회 (순회란, 출력)
    # 1. 전위 순회 : data -> left -> right (Data 출력 후 왼쪽노드 출력)
def preorder(node):
    if node == None: # 만약에 노드가 존재하지 않으면
        return # 종료
    print( node.data, end="->")
    preorder(node.left)     # 재귀함수: 함수내에서 동일한 함수 재호출
    preorder(node.right)
    
    # 2. 중위 순회 : left -> data -> right 
def inorder(node) :
    if node == None:
        return
    inorder( node.left )
    print(node.data, end ="->")
    inorder( node.right )

    # 3. 후위 순회 : left -> right -> data
def postorder( node ):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = "->")

# 실행
    
# 전위 순회 실행
print("전위 순회: ", end=" ")
preorder(node1)
print("end")

# 중위 순회 실행
print("중위 순회: ", end =" ")
inorder(node1)
print("end")

# 후위 순회 실행
print("후위 순회: ", end=" ")
postorder(node1)
print("end")
