'''
자료구조 : 1. 스택 / 2. 큐
    메모리에 데이터(data) 저장하는데 저장 되는 방법!!!
    1. 스택 (Stack)
        예) 동전케이스, ctrl + z (뒤로가기)
        Last in First out => LIFO
        Push : 데이터 추가
        Pop : 데이터 추출
        top : 입출구 위치(인덱스)
        
        1. 입구, 출구 동일
        2. input == output

                        -------------------------
        DATA(Push) ---->
                        메모리
        <----DATA(Pop)
                        -------------------------
    
        VS

    2. 큐 (Que)
        예) 지하철
        First in First out => FIFO
        enqueue : 데이터 추가
        dequeue : 데이터 추출
        rear : 데이터 추가되는 위치(인덱스)
        front: 데이터 추출되는 위치(인덱스)

                        -------------------------
                    Rear                        Front
        DATA(Enqueue) ---->       메모리       ----> DATA(Dequeue)
                        -------------------------
    
'''

# 리스트를 이용한 스택 구현

# 1. 스택 [ = 리스트 구현 ] 선언
stack = [ None, None, None, None, None ] # 리스트 선언
# None = 데이터 없다 표시 # " " vs None vs 0 

# 2. 스택 push      # 리스트의 인덱스는 0부터 시작한다 !!!
top = -1    # top의 역할: 현재 데이터를 추가할 수 있는 위치 [ 비어있는 stack은 top = -1 ]
SIZE = 5    # SIZE: 스택에 데이터를 저장 할 수 있는 최대 개수

"""                     스택 = 사이즈 (5)
                        top = 5     스택 Full
        |       |       top = 4
        |       |       top = 3
        |       |       top = 2     신동엽
        |       |       top = 1     강호동
        |       |       top = 0     유재석
        =========       top = -1    [ -1 인덱스 존재 X ]
"""

# 스택 출력 함수
def stack_print():
    global top
    print("----------- 스택 상태 확인 -----------")
    print("top 위치: " , top)
    for i in range(len(stack)-1, -1, -1): # 스택의 길이만큼 반복 for loop
        print(stack[i])

# 스택 안에 비어있는 공간이 있는지 체크
def isStackFull():
    global SIZE, top
    if ( top >= SIZE ):
        print("스택이 모두 찼습니다")
        return True
    else:
        print("비어 있는 자리가 존재합니다.", (SIZE - top) -1, "개 남았습니다.")
        False

stack_print()
isStackFull()

top += 1
stack[top] = "유재석"
stack_print()
isStackFull()

top += 1
stack[top] = "강호동"
stack_print()
isStackFull()

top += 1
stack[top] = "신동엽"
stack_print()
isStackFull()

# 3. 스택 pop
stack[top] = None
top -= 1
stack_print()
isStackFull()

stack[top] = None
top -= 1
stack_print()
isStackFull()

stack[top] = None
top -= 1
stack_print()
isStackFull()





