import datetime
# start_time = datetime.datetime.now()
# end_time = datetime.datetime.now()
# print(end_time - start_time)

def fibo(value_number):
    fibonaci_ciag = [0, 1]
    for n in range(value_number):
        next_num = sum(fibonaci_ciag[n: n+2])
        fibonaci_ciag.append(next_num)
    return fibonaci_ciag[value_number]



def fibo2(n, fib=[0, 1]):
    if n < len(fib):
        return fib[n]
    else:
        res = fibo2(n-2) + fibo2(n-1)
        fib.append(res)
        return res


start_time = datetime.datetime.now()
print(fibo(10000))
end_time = datetime.datetime.now()
print(end_time - start_time)
start_time = datetime.datetime.now()
print(fibo2(10000))
end_time = datetime.datetime.now()
print(end_time - start_time)