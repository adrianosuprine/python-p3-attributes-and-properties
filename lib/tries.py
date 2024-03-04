def sum_mul(n, m):
    if m <= n:
        return "INVALID"
    else:
        print(sum(i for i in range(n,m,n)))
        # print(sum)
        print(n)
    
    
sum_mul(0, 15)
sum_mul(4,-17)
       
             