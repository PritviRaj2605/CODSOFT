opt=0
while opt==0:
    num1=int(input('Enter number 1:'))
    num2=int(input('Enter number 2:'))
    opr=input('Enter =,-,*,/ to perform arithemetic operations:')
    if opr=='+':
        add=num1+num2
        print('Addition of two numbers:',add)
    elif opr=='-':
        sub=num1-num2
        print('Subtraction of two numbers:',sub)
    elif opr=='*':
        mul=num1*num2
        print('Multiplication of two numbers:',mul)
    elif opr=='/':
        if num2==0:
            print('Zero division error')
        else:
            div=num1/num2
            print('Division of two numbers',div)
    else:
        print('Invalid option!')
    opt=int(input('Enter 0 to perform more operations or 1 to exit:'))
if opt==1:
    print('Exiting...')
            
