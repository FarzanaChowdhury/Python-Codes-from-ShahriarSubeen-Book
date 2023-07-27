def find_fib(n):
    if n<= 2:
        return 1
    fib_x, fib_next = 1,1

    i=3
    while i<=n:
        i+= 1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next

def list_fib(n):
    fib_list = []
    for x in range(1,n+1):
        fib_list.append(find_fib(x))

    return fib_list

print(list_fib(10))
    