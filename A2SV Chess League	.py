# https://codeforces.com/gym/430380/problem/E

def merge(list1, list2):
    global k
    merged = []
    ptr_1 = ptr_2 = 0
    
    
    while ptr_1 < len(list1) and ptr_2 < len(list2) and list1[ptr_1][0] < list2[ptr_2][0] - k:
        ptr_1 += 1
    
    while ptr_1 < len(list1) and ptr_2 < len(list2) and list2[ptr_2][0] < list1[ptr_1][0] - k:
        ptr_2 += 1

    while ptr_1 < len(list1) and ptr_2 < len(list2):
        
        if list1[ptr_1][0] < list2[ptr_2][0]:
            merged.append(list1[ptr_1])
            ptr_1 += 1
        
        else:
            merged.append(list2[ptr_2])
            ptr_2 += 1
    
    merged.extend(list1[ptr_1:])
    merged.extend(list2[ptr_2:])

    return merged


def mergeSort(left, right, arr):
    
    if left >= right - 1:
        return [arr[left]]
    
    mid = left + (right - left)//2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid, right, arr)

    return merge(left_half, right_half)



n, k = map(int, input().split())
ratings = [ (val, ind + 1) for ind, val in enumerate(map(int, input().split()))]


ans = []
for rate, ind  in mergeSort(0, len(ratings), ratings):
    ans.append(ind)
    
ans.sort()
print(*ans)


