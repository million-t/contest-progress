from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    zeros = 0
    start = False
    
    for i, num in enumerate(nums[:-1]):

        if num:
            start = True
        if start and not num:
            zeros += 1

    print(zeros + sum(nums[:-1]))
    