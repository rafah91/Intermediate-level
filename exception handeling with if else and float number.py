#exception handeling with float and if else condition:
import math
age=input('Enter Age:')
if age.replace('.','').isnumeric():
    if float(age)>0:
        print(round(100/float(age),2))
        print(math.floor(100/float(age)))
        print(math.ceil(100/float(age)))
else:
    print('please enter number')
    
print('procesing')
