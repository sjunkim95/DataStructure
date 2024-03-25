import random       # import: 현재 py 파일 외 다른 미리 만들어진 파일[클래스] 불러오기
    # 1. 난수 관련 메소드 제공
# 제품 판매 중복체크 [ 이진트리 구현 ]

# 1. 이진트리 노드 선언
class TreeNode(): # 왼쪽과 오른쪽이 존재해야 이진트리인것
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 2. 전역변수
memory = []
root = None
datalist = ["참치김밥", "삼양라면", "서울우유", "신라면", "육개장", "치즈버거", "빅맥"]

# 랜덤으로 datalist에서 제품명을 선택해서 selllist에 50개 저장
selllist = [random.choice(datalist) for _ in range(50) ]
print("오늘 판매된 물건(중복o) ---> : ", selllist)

# 3. 메인 실행
node = TreeNode()       # 노드 생성
node.data = selllist[0] # 판매된 첫번째 제품
root = node             # root node 선정 (판매된 첫번째 제품을)
memory.append(node)     

for name in selllist[1:]:   # 판매리스트에서 1인덱스부터 마지막인덱스까지 반복처리 (0번 인덱스는 부모노드임으로)
    node = TreeNode()
    node.data = name

    current = root          # current: 현재 위치
    while True:
        if name == current.data:        # 만약에 해당 인덱스(selllist)의 data와, '현재위치(current)'의 data가 동일하다면
            break                       # 추가하지 않는다
        if name < current.data:         # 만약에 해당 인덱스의 data가 현재위치의 data보다 더 작으면 (보통 가나다 순으로)
            if current.left == None:    # 만약에 왼쪽 자식노드가 없으면
                current.left = node     # 왼쪽 자식노드에 추가
                memory.append(node)
                break
            current = current.left      # 부모노드보다 데이터가 작으면 왼쪽에 배치

        else:                           # 만약에 해당 인덱스의 data가 현재위치의 data가 더 크면
            if current.right == None:   # 만약에 오른쪽 자식노드가 없으면
                current.right = node    # 오른쪽 자식노드에 추가
                memory.append(node)
                break
            current = current.right     # 부모노드보다 데이터가 크면 오른쪽 배치

# 전위 순회
def preorder( node ):
    if node == None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

print()
print("오늘 판매된 물건(중복x) ---> : ",  end =" ") # 이어서 출력하기 위해
preorder(root)