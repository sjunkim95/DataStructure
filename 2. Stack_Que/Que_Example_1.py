"""
    스택:
        vs
    큐:

"""

# 1. 리스트를 이용한 큐 구현
queue = [ None, None, None ]
front = -1  # 출구의 현재 위치
rear = -1   # 입구의 현재 위치

# 큐 출력
def queue_print():
    print("[출구]<------", end = ' ')
    for i in range(0, len(queue), 1):
        print(queue[i], end = ' ')
    print("<------[입구]")
# 2. 큐에 데이터 추가
rear += 1
queue[rear] = "유재석"
queue_print()

rear += 1
queue[rear] = "강호동"
queue_print()

rear += 1
queue[rear] = "신동엽"
queue_print()

# 3. 큐에 데이터 추출
front += 1
queue[front] = None
queue_print() # 먼저 들어온 유재석이 먼저 나간다

front += 1
queue[front] = None
queue_print()

front += 1
queue[front] = None
queue_print()

