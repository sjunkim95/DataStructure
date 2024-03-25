# 프랙탈 [ Fractal ] : 일부 작은 조각이 전체와 비슷한 형태
    # 나무줄기, 번개, 나뭇잎

def drawCircle(x, y, r):
    global count
    count += 1 # 카운트 변수 1증가

    # 원형 그리기 [ .create_oval: 원형 그리기 함수 ]
    canvas.create_oval(x-r , y-r , x+r , y+r , width=5, outline='black')
                    # 왼쪽x, 위쪽y, 오른쪽x, 아래쪽y
    canvas.create_text(x, y-r, text=str(count), font=('', 30))
    if r >= radius/2:   # 만약에 현재의 반지름이, 전체반지름의 반보다 크면
        drawCircle(x-r //2, y, r//2) # 재귀를 이용해서 보면 위에 숫자로 순서를 유추해라
        # 왼쪽 원들을 먼저 다 그린다
        drawCircle(x+r //2, y, r//2) # 위에 있는 재귀가 모두 종료되기 까지 실행 x



# 1. 원형 그리기
from tkinter import * # GUI 관련 함수 제공

window = Tk()   # GUI 객체 생성
canvas = Canvas(window, height=1000, width=1000, bg='white')    # GUI 배경

# 원형 그리기
count = 0
radius = 400 # 반지름
wSize = 1000 

# 함수 호출 (x축, y축, 반지름)
drawCircle(wSize//2, wSize//2, radius)

canvas.pack()   # 해당 Canvas를 GUI에 추가

window.mainloop()   # GUI 열기
