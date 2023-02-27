from collections import defaultdict


n, k, q = list(map(int, input().split()))
recipes = [] 
# max_temp = 0
for _ in range(n):
    # book = 
    recipes.append(list(map(int, input().split())))
    # max_temp = max(max_temp, max(book))

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))


arr = [0]*(200000 + 2)


for left, right in recipes:
    arr[left] += 1
    arr[right + 1] -= 1

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

    if arr[i-1] >= k:
        arr[i- 1] = 1
    else:
        arr[i- 1] = 0

arr[-1] = 1 if arr[-1] >= k else 0

for i in range(1, len(arr)):
    arr[i] += arr[i-1]



for left, right in queries:
    print(arr[right] - arr[left - 1])



