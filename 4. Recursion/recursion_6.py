# 시에핀스키
# 재귀함수를 이용한 시에르핀스키 삼각형 구현

# 1. 터틀을 이용한 삼각형 그리기
# 2. 삼각형 안에 3개의 삼각형 그리기

# 삼각형 ( 120 * 3 )
import turtle

def draw( length, n ):
    # length : 전체 삼각형의 길이
    # n : 삼각형 개수 (즉, 함수당 재귀의 횟수)
    if n >= 1:
        for i in range(3): # 큰삼각형 안에 들어가는 삼각형 갯수
            t.forward( length )
            t.left(120) # 즉 60도로 꺽이는것 (180-120)
            draw(length/2, n-1)

t = turtle.Turtle()
t.speed(10)

draw(100, 3)