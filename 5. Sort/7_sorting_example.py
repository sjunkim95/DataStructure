# 성적별 조 만들기
# 조 2명 [ 성적이 높은 순, 낮은 순 ]
# 95 70     63 50
# 98-50 1조
# 70-63 2조
# 즉 1등과 꼴등, 2등과 뒤에서 2등과 조를 짠다

# 정렬 함수 구현
def sortScore(array):
    for end in range(1, len(array)):
        for current in range(end, 0, -1): # 뒤에서부터 거꾸로 내려오는 것
            if array[current - 1][1] > array[current][1]: # 이름기준 [0], 성적 기준 [1]
                array[current][1], array[current - 1][1] = array[current - 1][1], array[current][1]
    return array

scoreArray = [ ['유재석', 88], ['강호동', 99], ['신동엽', 71], ['하하', 78], ['김희철', 67], ['김영철', 92] ]

# 정렬 실행
print("정렬 전: ", scoreArray)
scoreArray = sortScore(scoreArray)
print("정렬 후: ", scoreArray)

# 조 만들기
for i in range( len(scoreArray)//2 ):                                   # 1. 배열의 길이 나누기 2만큼 반복처리
    print(scoreArray[i][0], ':', scoreArray[len(scoreArray)-1-i][0])
    # i = 0 일때 scoreArray[i][0]->이름: 마지막인덱스[len-1] - 1
    
'''
def insertionSort(array):
    for end in range(1, len(array)):
        for current in range(end, 0, -1):
            if array[current - 1] < array[current]: # 오름차순
                array[current], array[current - 1] = array[current - 1], array[current]
    return array

'''