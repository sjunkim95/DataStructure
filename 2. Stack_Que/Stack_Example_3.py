# 과제: 입력받은 문자열 거꾸로 출력하는 프로그램 Stack으로

def push(char):
    global top
    top += 1
    String.append(char)
    return

def pop():
    global top
    data = String[top]
    String[top] = None
    top -= 1
  #  print(data)
    return data

String = []
# 전역변수

top = -1    # 스택내 인덱스의 현재 위치

while True:
    char = input("1개 문자입력(*입력시 종료) : ")
    if char == "*":
        print("프로그램 종료 ")

        # 지금 입력받은 문자들을 거꾸로 출력
        for i in String:
            ans = pop() 
            print(ans, end="")

        break

    else:
        push(char)

