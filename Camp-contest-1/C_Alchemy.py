n = int(input())
time = list(map(int, input().split()))

left = 0
right = n - 1

ed = al = 0


for i in range(sum(time)):
    if left <= right and i == ed:
        ed += time[left]
        left += 1
    if left <= right and i == al:
        al += time[right]
        right -= 1
    

print(left, n - 1 - right)