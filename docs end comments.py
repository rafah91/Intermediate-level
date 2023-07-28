#Docs and comments

try:
    age=int(input('Enter your age:'))
    print(100/age)
    #processing

    #close
    
except ValueError:
    print('please enter number and number>0')
    #close
    
except ZeroDivisionError:
    print('please enter number and number>0')
    #close
    
else:#no exceptions
    print('in else')
    
finally:#always
    print('in always...')
    
print('Procesing')
