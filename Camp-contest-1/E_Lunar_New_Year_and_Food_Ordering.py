n, m = list(map(int, input().split()))
dishes = list(map(int, input().split()))
prices = list(map(int, input().split()))

orders = []
for _ in range(m):
    orders.append(list(map(int, input().split())))

sorted_price = [[prices[i], i] for i in range(n)]
sorted_price.sort()

cheapest_pointer = 0

for kind, quantity in orders:
    kind -= 1
    cost = 0
    if dishes[kind] < quantity:

        rem =  quantity - dishes[kind]
        cost += prices[kind]*(dishes[kind])
        dishes[kind] = 0
        
        while rem and cheapest_pointer < n:
            available = dishes[sorted_price[cheapest_pointer][1]]

            if available and available < rem:
                cost += prices[sorted_price[cheapest_pointer][1]]*available
                dishes[sorted_price[cheapest_pointer][1]] = 0
                rem -= available

            elif available:
                cost += prices[sorted_price[cheapest_pointer][1]]*(rem)
                dishes[sorted_price[cheapest_pointer][1]] -= rem
                rem = 0
                break
                
            cheapest_pointer += 1

        if rem:
            cost = 0
        
    else:
        cost += prices[kind]*(quantity)
        dishes[kind] -= quantity
    
    print(cost)
        