t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    bit_string = input()
    bit_string = [int(bit) for bit in bit_string]
    
    for op in range(m):
        changes = False
        bits = bit_string.copy()
        
        for i in range(n):
            if (not bit_string[i]) and bit_string[max(0, i - 1)] + bit_string[min(n-1, i + 1)] == 1: 
                bits[i] = 1
                changes = True
                
        bit_string = bits
                
        if not changes:
            break
    
    print("".join(list(map(str, bits))))