# 백준 - 설탕배달

N = int(input()) # 설탕 무게
dp = [-1] * 30
dp[3] = dp[5] = 1
# 점화식
for i in range (6, N+1):
    if i % 3 == 0: 
        dp[i] = dp[i-3] + 1 # 3kg 일 때 한 개
    elif i % 5 == 0: 
        dp[i] = dp[i-5] + 1 # 5kg 일 때 한 개
    elif dp[i-3] > 0 and dp[i-5] > 0:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    
for i, j in enumerate(dp):
    print(i, "-> ", j)
print(dp[N])
