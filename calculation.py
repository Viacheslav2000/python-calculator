#calculation funktion
def plus(x,y):
 return x + y
def minus(x,y):
 return x - y
def multiply(x,y):
 return x * y
def divide(x,y):
 return x / y

#cicle
while True:

    
    #user menu
    print('Calculator')
    print('1 Plus')
    print('2 Minus')
    print('3 Myltiply')
    print('4 Divide')
    choice = input('Choose Number (1-4):')


    if choice == 'q':
     print('Goodbye')
     break

    #Entering Numbers
    x = float(input('x'))
    y = float(input('y'))

    if choice == '4' and y == 0:
     print('Error: Division by zero is not allowed.')
    else:

        #Checking result
        if choice == '1':
            result = plus(x,y)

        elif choice == '2':
            result = minus(x,y)

        elif choice == '3':
            result = multiply(x,y)

        elif choice == '4':
            result = divide(x,y)
        

        else:
            print('Error304')
        print(result)
        print('-'*30)
