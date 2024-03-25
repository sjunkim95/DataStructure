# 구현 프로그램: 이름과 나이를 입력받아 나이순 정렬후 출력
# 1. 선형리스트 구현
# 2. 메뉴 [1. 추가 2. 삽입 3. 삭제 4. 종료]

# 1. 추가 메소드 구현
def add_data( name, age):
    namelist.append(None)
    count = len(namelist)
    namelist [count-1] = (name,age) # 마지막 인덱스에 튜플 추가
    # 길이는 1부터 // 인덱스는 0부터 // 길이가 인덱스로 변환시 -1을 해야한다

# 2. 삽입 메소드 구현
def insert_data(pos, name, age):
    if pos < 0 or pos > len(namelist): # 해당 포지션이 0보다 작지 않고, 배열의 길이보다 크면 안된다
        print("해당 인덱스가 존재하지 않습니다.")
        return
    
    namelist.append(None) # 1. 메모리 할당 우선
    count = len(namelist) # 2. 길이 체크
    for i in range(count-1, pos, -1):
        namelist[i] = namelist[i-1]
        namelist[i-1] = None
    namelist[pos] = (name, age)

# 3. 삭제 메소드 구현
def delete_data(pos):
    count = len(namelist)
    namelist[pos] = None
    for i in range(pos+1, count): # print (하나씩 찍어봐)
        namelist[i-1] = namelist[i]
        namelist[i] = None
    del(namelist[count-1])

# 4. 정렬(나이순) 함수 구현 [ .sort 구현 ]
def sort_data(): # 정렬 함수 선언
    for i in range(0, len(namelist), 1):            # i: 비교기준
        for j in range(0, len(namelist), 1):        # j: 비교대상
            if namelist[i][1] < namelist[j][1]:     # i의 숫자보다 j의 숫자가 더 크면
                # i의 인덱스 데이터와 j의 인덱스 데이터 교환 [ swap ]
                temp = namelist[i]                  # temp = 20
                namelist[i] = namelist[j]           # 20 = 30
                namelist[j] = temp                  # 30 = temp 

    print("나이순 정렬된 출력: ", namelist)         # 20 과 30 데이터가 swap!!

    # 정렬 시나리오
    # 3, 4, 2 , 5 내림차순으로 정리할때
    # 1. 각 인덱스마다 다른 인덱스와 비교
        # 1. 0 인덱스 -> 1, 2, 3
        # 2. 1 인덱스 -> 2, 3
        # 3. 2 인덱스 -> 3
        # 4. 3 인덱스 -> x [비교 당했기 때문에 비교 x]
        # 비교기준 = i // 비교대상 = j
     

# 0. 임의로 데이터값 넣어줌, tuple로
namelist=[("상준", 29), ("유진", 24)]

if __name__ == "__main__": # 메인 코드 실행 되는 부분
    while True: # 무한루프

        select = int(input("선택: 1. 추가 2. 삽입 3. 삭제 4. 정렬 5. 종료 ")) # 메뉴 출력 -> 메뉴번호 입력
        if (select == 1):
            name = input("추가 이름: ")
            age = int(input("추가 나이: "))
            add_data(name,age)
            print(namelist)

        elif select == 2:
            pos = int(input("삽입할 위치: "))
            name = input("추가 이름: ")
            age = int(input("추가 나이: "))
            insert_data(pos, name, age)
            print(namelist)

        elif select == 3:
            pos = int(input("삭제할 위치: "))
            delete_data(pos)
            print(namelist)

        elif select == 4:
            sort_data()

        elif select == 5:
            break # 가장 가까운 반복문 탈출

        else:
            print("메뉴 1~4 사이만 입력해주세요: ")
            continue # 가장 가까운 반복문 이동
