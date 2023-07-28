#exception handeling:


try:
    age=int(input('Enter your age:'))
    print(100/age)
    
except Exception:
    print('please enter number and number>0')
    
    
print('Procesing')
