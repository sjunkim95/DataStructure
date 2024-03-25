# 자판기 프로그램

# 1. push 함수: 스택에 데이터 넣기
def push( data ):
    global top # 함수 안으로 전역변수 가져오기
    if (isStackFull()):
        print("재고가 모두 찼습니다.")
        return # 함수 종료
    top += 1
    stack[top] = data

# 2. pop 함수: 스택에 데이터 빼기
def pop(): # data입력 필요없음
    global top
    if isStackEmpty(): # isStackEmpty가 True라면
        print("재고가 존재하지 않습니다.[구매불가]")
        return # 함수 종료
    data = stack[top]   # 삭제된 데이터 임시저장
    stack[top] = None   # 현재 위치 None 변경
    top -=1             # 현재 위치 -1
    return data         # 삭제된 데이터 반환

# 3. peek: 현재 top 위치의 데이터 확인
def peek():
    global SIZE, top
    if isStackEmpty():
        print("재고가 모두 비어 있습니다. ")
        return None
    return stack[top] # stack의 현재 위치 확인


# 4. isStackFull
def isStackFull():
    global SIZE, top
    if top >= SIZE-1:    # top: 인덱스[0~] size: 길이[1~]
        return True
    else:
        return False

# 5. isStackEmpty
def isStackEmpty():
    global SIZE, top
    
    if top == -1:       # 만약에 top이 -1이면 stack내 데이터 존재 X
        return True
    else:
        return False
    
# 0. 전역변수
SIZE = int(input("자반기 제품의 재고 최대 개수 ==> ")) # 입력받기
stack = [ None for _ in range(SIZE) ]
    # data for _ in ragne(리스트) : 리스트내 모든 인덱스에 해당 data 추가
top = -1 # 스택내 에 data 현재 위치

# 프로그램 실행
while True: # 무한루프
    select = int(input("1. 재고추가 2. 구매 3. 재고확인 4. 종료 중 선택 : "))
    if select == 1:
        print("재고 추가합니다.")
        data = input("제품명: ")
        push(data) # 입력받는 값을 push 함수 인수로 전달
        print("스택 상태: ", stack)
    elif select == 2:
        # 구매시 stack 구조이기 때문에 마지막에 구매한 물품이 구매될것. Last in First out (LIFO)
        print("구매 합니다.")
        data = pop()
        print(data, "를 구매했습니다.")
        print("스택 상태: ", stack)
    elif select == 3:
        print("재고 확인합니다.")
        data = peek() # 왜지?
        print("확인 제품: ", data)
        print("스택 확인: ", stack)
    elif select == 4:
        print("프로그램 종료합니다.")
        break # 가장 가까운 반복문을 종료
    else:
        print("알 수 없는 번호입니다. [ 다시선택 ]")


