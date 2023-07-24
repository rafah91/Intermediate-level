names=['ahmad','mohammad','hasan','mira']

def myfunc(n):
    return len(n)

result=list(map(myfunc,names))
print(result)

