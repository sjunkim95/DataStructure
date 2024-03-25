"""
    동적 계획법 [ DP : 다이내믹 프로그래밍 ]
        1. 하나의 문제를 여러 개의 작은 단위로 나누어서 결과 찾기
            - 기억하며 풀기
        2. 효율적으로 문제 해결 가능
"""
# 예 ) 피보나치 수열 VS 동적 계획법

def dp_fibo(n):
    global count_dp
    memo = [ 1, 1 ]     # 계산된 수열 저장하는 공간
    if n < 2:
        return memo[n]
    else:
        for i in range( 2, n+1 ): # 피보나치가 n이 2보다 커야함으로
            memo.append(memo[i-1] + memo[i-2]) # memo의 인덱스 1과, 0을 더한다
            count_dp += 1
        return memo[n]

def requ_fibo(n): # 재귀
    global count_requ
    count_requ += 1
    if n < 2:
        return 1
    else:
        return requ_fibo(n-1) + requ_fibo(n-2)      # 피보나치 수열 공식

# 전역변수
count_dp = 0    # DP 방식 피보나치 반복횟수
count_requ = 0  # 재귀방식 피보나치 반복횟수

# 재귀를 사용
print("30번째 피보나치 수열")

res = requ_fibo(30)
print("재귀를 이용한 피보나치 : ", res, "반복수 : ", count_requ)

# 동적 계획법
res = dp_fibo(30)
print("DP를 이용한 피보나치 : ", res, "반복수 : ",count_dp)