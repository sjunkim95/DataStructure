"""
    황금 미로 문제
        1. 조건:
            1. 왼쪽 상단 [ 0 , 0 ] 부터 출발해서 오른쪽[ 마지막행 , 마지막열 ]
            2. 시작부터 출구까지 지나가면서 최대 얻을 수 있는 황금 개수 세기
        
        2. 황금 미로 구조
        입구
                1개   4개   4개   2개   2개
                1개   3개   3개   0개   5개
                1개   2개   4개   3개   0개
                3개   3개   0개   4개   2개
                1개   3개   4개   5개   3개
                                                출구
                입구 -> 1개 -> 4개 -> 4개 -> 3개 -> 4개 -> 3개 -> 4개 -> 5개 -> 3개 -> 출구
"""

def printMaze(arr):
    # 2차원 리스트 출력
    for row in range(ROW): 
        for col in range(COL): 
            print("%3s" % arr[row][col] , end = " ")
            # 지나온 길을 문자로 표기하기 위해 %d -> %s [ 형식문자 ]
        print()
    print() 

def growRich():
    # 메모이제이션 [ 동적계획법 사용되는 기술 방식 ]
    memo = [ [0 for _ in range(COL)] for _ in range(ROW) ]
    memo[0][0] = goldMaze[0][0] # 입구에 있는 골드 획득~

    # 구현
    rowsum = memo[0][0]                 # 가로의 누적합계
    for i in range(1, ROW):             # i = 열
        rowsum += goldMaze[0][i]        # 누적 합계 -> i번째에 넣는다
        memo[0][i] = rowsum
    
    colsum = memo[0][0]                 # 세로의 누적합계
    for i in range(1, COL):
        colsum += goldMaze[i][0]
        memo[i][0] = colsum             # 누적 합계

    # 행/열 비교
    count = 0 # 이동횟수
    for row in range(1, ROW): # ROW를 = 2로 바꾸면 2번째줄까지 출력해서 print로 비교확인 가능
        for col in range(1, COL):
            #   아래 방향 > 오른쪽 방향
            count +=  1
            if memo[row][col-1] > memo[row-1][col]:
                # 아래방향이 더 크면
                memo[row][col] = memo[row][col-1] + goldMaze[row][col]
                print(count, "번째 아래방향 이동 : ", memo[row][col])
            else:
                # 오른쪽방향이 더 크면
                memo[row][col] = memo[row-1][col] + goldMaze[row][col]
                print(count, "번째 오른쪽방향 이동 : ", memo[row][col])


    print("---------------------메모이제이션 출력---------------------")
    printMaze(memo)
    print("---------------------지나온 경로 출력---------------------")
    row = ROW-1             # 행 : 4
    col = COL-1             # 열 : 4
    memo[row][col] = "*"      # 입구에 도착

    # 출구부터 입구까지
    while row !=0 or col !=0: # 행 이거나 열이 0이 아닐때 까지 반복 [ row 와 col 0 이면 종료 ]
        if row-1 >= 0 and col-1 >= 0:
            # 현재 기준[4][4]으로 위쪽방향, 왼쪽방향 비교
            if memo[row-1][col] > memo[row][col-1]:
                # 위쪽 방향이 더 크면
                row -= 1    # 위로 이동
            else:
                # 왼쪽 방향이 더 크면
                col -= 1    # 왼쪽 이동
        elif row-1 < 0 and col-1 >= 0: # 만약에 위쪽 방향에 인덱스가 없으면
            col -= 1  # 왼쪽 이동
        else: # 만약에 왼쪽 방향에 인덱스가 없으면
            row -= 1  # 위로 이동
            
        memo[row][col] = "*"  # 해당 row / col -> 지나온 경로의 문자표시
    
    printMaze(memo)

    return memo[ROW-1][COL-1]

    """
    # 2차원 배열[리스트] 출력하는 방식
    for row in range(0, ROW):           # 행 반복
        for col in range(0, COL):       # 열 반복
            print(memo[row][col], end = " ")
        print()
    
    return memo[ROW-1][COL-1]   # 마지막 인덱스 반환
    """
    


ROW , COL = 5 , 5   # 미로 칸
goldMaze = [
    [ 1, 4, 4, 2, 2 ],
    [ 1, 3, 3, 0, 4 ],
    [ 1, 2, 4, 3, 0 ],
    [ 3, 3, 0, 4, 2 ],
    [ 1, 3, 4, 5, 3 ],
]

macolGold = growRich()

print("최대 황금 미로에서 얻을 수 있는 황금 개수:", macolGold)

"""
순서도
    1. 메모이제이션 [ 2차원 리스트 ] 사용
    2. 입구에 있는 골드 무조건 획득
    3. 미로의 개수만큼 2차원리스트 생성
        1 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
    4. 가로의 누적합계
        1 , 5 , 9 , 11 , 13
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
        0 , 0 , 0 , 0 , 0
    5. 세로의 누적합계
        1 , 5 , 9 , 11 , 13
        2 , 0 , 0 , 0 , 0
        3 , 0 , 0 , 0 , 0
        6 , 0 , 0 , 0 , 0
        7 , 0 , 0 , 0 , 0
    6. 비교
        ROW = 1
            COL = 1
                    memo[1][0] > memo[0][1]
                        2   >   5 : false
                    memo[1][1] = memo[0][1] + 미로[1][1]
                        0 = 5 + 3
                    [1][1] = 8
            COL = 2
                    memo[1][1] > memo[0][2]
                        5   >   9 : false
                    memo[1][2] = memo[0][2] + 미로[1][2] 
                                    9 + 3  
                    [1][2] = 12
            COL = 3
                    memo[1][2] > memo[0][3]
                        12   >   11 : True
                    memo[1][3] = memo[1][2] + goldMaze[1][3] 
                                    12 + 0
                    [1][3] = 12
            COL = 4
                    memo[1][3] > memo[0][4]
                        12   >   13 : False
                    memo[1][4] = memo[0][4] + goldMaze[1][4] 
                                    13  + 4
                    [1][4] = 17
    어떻게보면 row1의 대각선 값들을 구하는 순서도
    ROW = 1값만 보고싶으면
    # 행/열 비교 -> 여기서 
    for row in range(1, 2): <--- 이렇게 바꿔서 실행해봐라!!
            ROW = 1 END 
                    1 5 9 11 13 
                    2 8 12 12 17 
                    3 0 0 0 0 
                    6 0 0 0 0 
                    7 0 0 0 0 
            ROW = 2 END 
                    1 5 9 11 13 
                    2 8 12 12 17 
                    3 10 16 19 19 
                    6 0 0 0 0 
                    7 0 0 0 0            
            ROW = 3 END 
                    1 5 9 11 13 
                    2 8 12 12 17 
                    3 10 16 19 19 
                    6 13 16 23 25 
                    7 0 0 0 0 
            ROW = 4 END
                    1 5 9 11 13 
                    2 8 12 12 17 
                    3 10 16 19 19 
                    6 13 16 23 25 
                    7 16 20 28 31   
"""

"""
지나온 경로 순서도
    row = 4 col = 4
    row - 1 >= 0 and col - 1 >= 0 일때,
                [3][4] > [4][3] : 
"""