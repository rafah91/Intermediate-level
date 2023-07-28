#exception handeling double except:


try:
    age=int(input('Enter your age:'))
    print(100/age)
    
except (ValueError,ZeroDivisionError):
    print('please enter number')
    
    
print('Procesing')



    
