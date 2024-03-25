import time # 시간에 관련된 함수 제공
import random # 난수에 관련된 함수 제공

# 재귀함수 예시1: 팩토리얼 구현 숫자!
def factorial(num):
    if num <= 1:
        print("[종료] 1반환")
        return 1
    print("%d * %d 호출" % (num, num-1))
    val = factorial(num-1)
    print("%d * %d = %d 반환" %(num, num-1, val))
    return num * val
#   return num * factorial(num-1)

num = int(input("팩토리얼 수: "))
print(factorial(num))
print("-----------------------------------------")

# 재귀함수 예시2: 카운트 다운 구현
def countDown(n):
    if n == 0:
        print("시작!!!")
    else:
        print(n,"초")
        time.sleep(1) # time.sleep(초) : 해당 초만큼 일시중지
        countDown(n-1)
countDown(3)
print("-----------------------------------------")

# 재귀함수 예시3: 별찍기
def starprint(n):
    if n > 0:
        starprint(n-1)
        print("*"*n)
starprint(5)
"""
    !!재귀의 특징!!
    * 별을 찍으면서 들어가는 것이 아닌, 나오면서 별을 찍는것*
    순서도
    1. 함수호출(3) -> 조건:true -> 재귀함수(2)
        2. 함수호출(2) -> 조건:true -> 재귀함수(1)
            3. 함수호출(1) -> 조건:true -> 재귀함수(0)
                4. 함수호출(0) -> 조건:false  -> 돌아간다
            3. print("*")
        2. print("**")
    1. print("***")
"""
print("-----------------------------------------")

# 재귀함수 예시4: 구구단
def gugudan(dan, num):
    print("%d x %d = %2d" %(dan, num, dan*num), end="   ")
    if dan < 9:
        gugudan(dan+1, num) # 재귀호출

for num in range(1, 10):
    gugudan(2, num) # 2단부터 시작되는것
    print()

"""
    print에서 사용되는 형식(모양=포멧)문자 = 서식문자 = 함수.format()
        print( "형식문자1 형식문자2" % 값1, 값2 )
        %d 정수             %2d : 2칸 자리 차지  [ 해당 자릿수에 수가 없으면 공백 ]
        %o 8진수            %02d : 2칸 자리 차지 [ 해당 자릿수에 수가 없으면 0으로 대입 ]
        %x 16진수
        %f 실수
        %c 단일 문자
        %s 문자열
"""
print("-----------------------------------------")

# 재귀함수 예시5: N제곱 구하기
tab = ' '
def pow(x, n):
    global tab
    tab += '     '
    if n == 0:
        return 1
    print(tab+"%d*%d^(%d-%d)" %(x, x, n, 1))
    return x * pow(x, n-1)

print(pow(2, 4))
print("-----------------------------------------")

# 재귀함수 예시 6: 배열 총합계

def arraysum(arr, n):
    if n <= 0:
        return arr[0]
    return(arraysum(arr, n-1) + arr[n])

# 배열내 10~20정도의 난수 값(0~255)을 저장하는 배열
array = [random.randint(0,255) for _ in range(random.randint(10,20))]
# random.randint(난수 시작, 난수 끝)

print(arraysum(array, len(array)-1)) # 배열의 총 합계를 구하는 것
# 반복문으로 충분히 가능하지만, 재귀로도 가능하다라는것을 보여주는 것.

print("-----------------------------------------")

# 재귀함수 예시 7: 피보나치 수열
    # 공식 : fibo(n-1) + fibo(n-2)
    # 1 2 3 5 8 13 21 34
    # 어떤 항이 앞에 두항의 더한값과 같은 상태
    # 1 + 2 = 3
    #     2 + 3 = 5
    #         3 + 5 = 8
    #             5 + 8 = 13
    #                 8 + 13 = 21
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
                    # 앞항 + 앞앞항
print("피보나치 수열 -> ", end = ' ')
for i in range(2, 20):
    print(fibo(i), end= ' ')
    