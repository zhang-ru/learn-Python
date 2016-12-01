def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

a = queue_time([2,4,3,4,2,3], 2)
print(a)