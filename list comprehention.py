names=['ahmad','ali','hassan','mohammad']
result=[]
for n in names:
    result.append(len(n))
print(result)

result2=[len(n) for n in names]
print(result2)
even=[n for n in range(1,101) if n%2==0]
print(even)

even=[even for n in range(1,101) if n%2==0]
print(even)

even=[f'{n} even' for n in range(1,101) if n%2==0]
print(even)

even=[f'{n} even' if n%2==0 else f'{n} odd' for n in range(1,101)]
print(even)

students={'ahmad':60,'ali':70,'hassan':80}
result={k:v*2 for (k,v) in students.items()}
print(result)
