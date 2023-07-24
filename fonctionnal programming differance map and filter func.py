numbers=list(range(1,11))
def myfilter(n):
    if n%2==0:
        return n
result = list(filter(myfilter,numbers))
print(result)
result2 = list(map(myfilter,numbers))
print(result2)
