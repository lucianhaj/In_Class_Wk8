def fib(n):
    sum1 = 0
    sum2 = 1
    sum = 0
    if n == 2:
        return 1
    elif n == 1:
        return 0
    for i in range(0, n-2):
            sum = sum1 + sum2
            sum1 = sum2
            sum2 = sum
    #print("fib of", n, sum)
    return sum



def fact(x):
    num = 1
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        for i in range(1, (x+1)):
            num *= i
    #print("num", num)
    return num

    
