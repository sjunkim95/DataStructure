# 자료구조: 리스트
#1. 선형리스트(Linear List/ Ordered List), 2. 연결리스트(Linked List)  3. 원형리스트(Circular Linked List)
'''
1. 선형리스트
	1. 데이터를 일정한 순서로 나열한 자료구조
	2. 입력한 순서대로 저장하는 데이터에 해당
	3. 메모리도 차례로 저장된다
	예) 식당: 웨이팅 // 코로나선별소: 코로나 검사 대기줄 등등
	비슷: 파이썬(list 유사) // 자바(arraylist 클래스) // : 일반적인 객체지향 언어에서 이미 구현 객체가 존재
	-> 파이썬 리스트를 사용해서 자료구조 리스트를 구현하는것
'''	
# 선형리스트 구현
	# 시나리오: 학생명 등록하는데 등록순서대로 저장!!
    # 1. 학생들을 저장할 배열 선언
    # 2. 학생 등록시 배열내 메모리 할당 [None]: 메모리 효율성 높일 수 있다.
    # 3. 만약에 배열내 중간 삽입 할 경우 -> insert 구현
        # 1. 해당 위치를 입력받는다. [position]
        # 2. 해당 위치에 있던 기존 데이터 한칸씩 뒤로 이동
        # 3. 해당 position까지 None 한칸씩 이동
    # 4. 만약에 배열내 중간 삭제 있을경우 -> delete 구현
        # 1. 해당 위치를 입력받는다
        # 2. 해당 위치에 데이터 None 변경 후
        # 3. 해당 위치 뒤 인덱스를 앞으로 한칸씩 이동
        # 4. 마지막 인덱스 메모리 지운다. [초기화]
"""
            1. [강호동, 유재석, 신동엽] : 배열
            만약에 강호동 뒤로 '하하' 삽입 [position:1, data:하하]
            2. [강호동, None, 유재석, 신동엽]
            해당 position 뒤에 인덱스가 한칸씩 이동
"""

names = [] # 전역변수 배열 선언

def add_data(name) : # 학생등록 함수 (append 구현개념)
    
    names.append(None) # 1. 배열에 메모리 할당 [None = 공백할당] -> null 값과는 다르다, 메모리가 들어가서 길이가 생김
    count = len(names) # 2. 배열내 길이 변수
    names[ count - 1 ] = name # 3. 해당 배열의 마지막 인덱스에 데이터 추가

def insert_data(position, name): # 학생등록시 해당 위치에 저장 함수 [리스트 메소드중 .insert() 직접 구현]
    # 만약에 position 0보다 작으면 [0보다 작은 인덱스 존재 X: 인덱스 0부터 시작]
    # 이거나 만약에 position 현재 배열의 마지막 인덱스보다 크면 존재 X
    
    if position < 0 or position > len(names):
        print("Data is out of range[인덱스가 없습니다].")
        return # 함수 종료(아래 코드가 실행되지 않는다!!!)

    names.append(None) # 1. 배열에 메모리 할당 [ None ]
    # names에 먼저 메모리를 공백으로 준다.
    # 그 이유는 메모리의 효율성을 높이기 위하여 (아껴쓴다)

    count = len(names) # 2. 배열의 길이 체크

    for i in range(count-1, position, -1): # 3. 해당 position 뒤 인덱스 데이터 한칸씩 이동
        # i가 배열의 길이부터 position까지 이동
        names[i] = names[i-1] # 인덱스 = 인덱스-1
        names[i-1] = None # 인덱스 -1 = None
    
    names[position] = name # 해당 position에 데이터 넣기

def delete_data(position): # 해당 위치에 데이터 삭제 [ .remove 구현 ]
    if position < 0 or position > len(names):
        print("데이터를 삽입할 위치가 벗어났습니다[인덱스가 없습니다]")
        return
    count = len(names)
    names[position] = None # 1.해당 position에 데이터 공백 대입
    print("삭제함수 loop 전: ", names)

    for i in range( position+1, count): # 2. position 인덱스 부터 마지막 인덱스까지
        names[i-1] = names[i]   # 인덱스-1 = 인덱스
        names[i] = None         # 인덱스 = None
        print("삭제함수 loop 후: ", names)
    del(names[count-1])         # 마지막 인덱스 메모리 초기화 [ 메모리 삭제 메소드 = del()]
    # delete할때는 인덱스 위치에서 앞으로 간다
    # 반대로, insert할때는 맨마지막에서 앞으로 뺀다.



add_data('유재석')
add_data('강호동')
add_data('신동엽')
add_data('서장훈')
add_data('김희철')

insert_data(3, '하하')
    # 알고리즘 = 순서도
        # 1. insert_data 함수 실행
        # 2. position, data 인수로 넘기기
        # 3-1. 만약에 position이 배열의 길이에 벗어나면 함수종료
        # 3-2. 아니면 배열에 길이 추가
        # 4. 반복문 [마지막 인덱스부터 position까지 1씩 이동]
            # 1. 5부터 -> position 2까지 -1씩 이동한다
                # names[5] = names[4] # None = 김희철 대입
                    # [ 유재석, 강호동, 신동엽, 서장훈, 김희철, None ]
                    # [ 유재석, 강호동, 신동엽, 서장훈, 김희철, 김희철 ]
                # names[4] = None
                    # [ 유재석, 강호동, 신동엽, 서장훈, None, 김희철 ]
            # 2. i = 4일때
                # names[4] = names[3] # None = 서장훈
                    # [ 유재석, 강호동, 신동엽, 서장훈, 서장훈, 김희철 ]
                # names[3] = None
                    # [ 유재석, 강호동, 신동엽, None, 서장훈, 김희철 ]
            # 3. i = 3일때
                # names[3] = names[2] # None = 서장훈
                    # [ 유재석, 강호동, 신동엽, 신동엽, 서장훈, 김희철 ]
                # names[2] = None
                    # [ 유재석, 강호동, None, 신동엽, 서장훈, 김희철 ]
            # 4. i = 4일때 반복문 종료
                # names[2] = 하하
                # [ 유재석, 강호동, 하하, 신동엽, 서장훈, 김희철 ]
print(names)


# 3번째 자리에 하하 삭제
delete_data(3)

print(names)