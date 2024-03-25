"""
    문제 :
    1. 설명
        수학 포기자한 학생이 시험보는데 1번부터 마지막 문제까지 정답을 찍는다.

        유재석 : 1 2 3 4 5 1 2 3 4 5 ~     모든 문제를 찍는다 -> 난수 생성
        강호동 : 2 1 2 3 2 4 2 5 2 1 ~     모든 문제를 찍는다 -> 난수 생성
        신동엽 : 3 3 1 1 2 2 4 4 5 5 ~     모든 문제를 찍는다 -> 난수 생성

        1번 문제부터 마지막 문제까지 정답이 순서대로 들은 배열이 있을때

        가장 많은 문제를 맞힌 사람 결과 찾기
    2. 조건
        시험은 최대 10,000문제 있음
        정답은 1~5 중 하나
        정답지는 문제 개수만큼 난수로 생성

    3. 입출력 예
        정답지 예 [ 1 , 2 , 3 , 4 , 5 ]     1등 : 유재석
        정답지 예 [ 1 , 3 , 2 , 4 , 2 ]     1등 : 유재석 강호동
"""
import random

def solution(answer_list):  # 순차검색
    counter = [0, 0, 0]     # 맞힌 개수 저장하는 리스트
    size = len(answer_list) # 문제 개수

    for i in range(size):                       # 문제 개수만큼 반복처리
        if answer_list[i] == student1_list[i]:  # 만약에 i번째 문제가 s1의 i번째 같으면
            counter[0] += 1                     # student1 정답개수 증가
        if answer_list[i] == student2_list[i]:
            counter[1] += 1                     # student2 정답개수 증가
        if answer_list[i] == student3_list[i]:
            counter[2] += 1                     # student3 정답개수 증가
    print("체점 결과: ", counter)

    best = max(counter) # 가장 많이 맞춘 수
    result = []         # 결과

    for i in range(3):
        if counter[i] == best:              # 가장 많이 맞춘 수 와 인덱스가 동일하면
            result.append(str(i+1)+"번")    # 1등에 추가
    return result

answer_list = [ random.randint(1, 5) for _ in range(10) ]   # 1. 문제 정답 10개 난시 생성
student1_list = [ random.randint(1, 5) for _ in range(10) ] # 2. 1번 학생이 찍은 문제 번호
student2_list = [ random.randint(1, 5) for _ in range(10) ] # 3. 2번 학생이 찍은 문제 번호 
student3_list = [ random.randint(1, 5) for _ in range(10) ] # 4. 3번 학생이 찍은 문제 번호

print("시험 정답지: ", answer_list)
print("1번 학생이 찍은 정답 : ", student1_list)
print("2번 학생이 찍은 정답 : ", student2_list)
print("3번 학생이 찍은 정답 : ", student3_list)

print("1등 :", solution(answer_list), "학생")