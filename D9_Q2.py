def fib(n):
    if n <= 1:
        return 1 
    else : 
        return fib(n-1) + fib(n-2)


n = 10 
ans = fib(n)
print(ans)

