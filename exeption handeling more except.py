try:
    age=int(input('Enter your age:'))
    print(100/age)
    
except ValueError:
    print('please enter number')
    
except ZeroDivisionError:
    print('please enter number>0')
    
print('Procesing')
