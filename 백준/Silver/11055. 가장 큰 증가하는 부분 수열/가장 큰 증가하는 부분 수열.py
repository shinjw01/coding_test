import copy
n = int(input())
a = list(map(int,input().split()))

dp = copy.deepcopy(a)

for i in range(n):
  for j in range(i):
    if a[j] < a[i]:
      dp[i] = max(dp[i], dp[j]+a[i])
print(max(dp))