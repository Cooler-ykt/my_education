def fact(n):
    if 0==n:
        return 1
    else:
        return fact(n-1)*n

print(fact(1023))
        
