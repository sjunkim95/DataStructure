"""
    그래프
        예) 지하철 노선도, 전기 회로도, 인맥 관계도 ('조직도'와는 반대의 개념)

        1. 여러 노드가 서로 연결된 자료구조 
        (반대로, 이진트리는 부모노드 한개당 자식노드 2개)

        2. 그래프 종류
            1. 무방향 그래프 ( 이동 방향 표기 X )
            2. 방향 그래프 ( 이동 방향 표기 O )     
"""

# 그래프 구현: 2차원 리스트를 이용한 그래프 구현
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        # 1. [ 0, 0, 0, 0 ]
        # 2. [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]
        # 2차원 리스트 [ 행1[열1,열2,열3,열4], 행2[열1,열2,열3,열4], 행3[열1,열2,열3,열4], 행4[열1,열2,열3,열4] ]

print("-------------------------무방향 그래프-------------------------")
G1 = None       # 객체 [ 클래스로부터 메모리 할당 전 = 선언만 했을경우 ]
G1 = Graph(4)   # 인스턴스 [ 선언된 객체에 해당 클래스로 메모리 할당 ]

G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

# 출력 [ 무방향 그래프 ]
for row in range(4):            # row: 행   row는 0부터 3까지 1씩 증가
    for col in range(4):        # col: 열   col는 0부터 3까지 1씩 증가
        print(G1.graph[row][col], end=" ")
    print()
    # 중첩 반복문 [ 어렵다~~~ --> 순서도 그려라]
"""
    row = 0일때
        col = 0, col = 1, col = 2, col = 3
        [0][0]   [0][1]   [0][2]   [0][3]
    row = 1일때
        col = 0, col = 1, col = 2, col = 3
        [1][0]   [1][1]   [1][2]   [1][3]
    row = 2일때
        col = 0, col = 1, col = 2, col = 3
        [2][0]   [2][1]   [2][2]   [2][3]
    row = 3일때
        col = 0, col = 1, col = 2, col = 3
        [3][0]   [3][1]   [3][2]   [3][3]
"""

print("-------------------------방향 그래프-------------------------")

# 출력 [ 방향 그래프]
G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1


for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end=" ")
    print()

"""
    무방향 vs 방향 그래프
    
    무방향 위 예시 (서로 대칭)
         A B C D      
       A 0 1 1 1
       B 1 0 1 0
       C 1 1 0 1
       D 1 0 1 0
       
    무방향 초기값
         A B C D   ->  이것이 default 값 일것     
       A 0                       B
       B   0                A         C
       C     0                   D
       D       0

    # 1. A 와 B 연결
         A B C D   ->  이것이 default 값 일것     
       A 0 1                     B
       B 1 0                   /      
       C     0               A      C
       D       0                 D
    
    # 2. A 와 C 연결
         A B C D   ->  이것이 default 값 일것     
       A 0 1 1                   B
       B 1 0                   /      
       C 1   0               A ---- C
       D       0                 D

    # 3. A 와 D 연결
         A B C D   ->  이것이 default 값 일것     
       A 0 1 1 1                B
       B 1 0                  /      
       C 1   0               A ---- C
       D 1     0              \  
                                D
    
    # 4. B 와 C 연결 / C 와 D 연결
         A B C D   ->  이것이 default 값 일것     
       A 0 1 1 1                B
       B 1 0 1 0              /   \    
       C 1 1 0 1             A --- C
       D 1 0 1 0              \   /
                                D

    그래서, 무방향은 서로 대칭관계임
    누가 누굴 연결했는지 없고, 그저 연결 상태를 이야기 하는것
-----------------------------------------------------------------

    방향 그래프 코드 예시로
    G3 = Graph(4)
    G3.graph[0][1] = 1; G3.graph[0][2] = 1
    G3.graph[3][0] = 1; G3.graph[3][2] = 1

    방향 초기값 (default값)
         A B C D            B
       A 0              A       C 
       B   0                D
       C     0 
       D       0

       # 1.  A ---> B 연결 
         A B C D            B
       A 0 1               /      
       B   0            A       C
       C     0      
       D       0            D

       # 2.  A ---> C 연결 
         A B C D            B
       A 0 1 1 0          /      
       B   0            A ----> C
       C     0      
       D       0            D

        # 3.  D ---> A 연결 
         A B C D           B
       A 0 1 1 0          /      
       B   0            A ---> C
       C     0            \  
       D 1     0           D

       # 4.  D ---> C 연결 
         A B C D           B
       A 0 1 1 0          /      
       B   0            A ---> C
       C     0            \  /
       D 1   1 0           D

       ** 이것(배열)만을 보고 그림을 그릴 수 있어야한다
"""

