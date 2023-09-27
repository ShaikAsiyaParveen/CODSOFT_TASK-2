f=("Welcome to python calculator")
print(f)
while True:
    print('Enter  \nO for Addition  \n1 for Subraction  \n2 for Multiplication  \n3 for Division ')
    print("continue for yes/quit for no")
    n=input("Choose yes/no:")
    if (n =='yes'):
        operation = input("Enter the operation you want to perform: ")
        x =input("Enter the first number : ")
        y =input("Enter the second number : ")
        if operation == '0':
            print("The addition is", int(x) + int(y))
        elif operation == '1':
            print("The subtraction is", int(x) - int(y))
        elif operation == '2':
            print("The multiplication is", int(x) * int(y))
        elif operation == '3':
            print("The division is", int(x) / int(y))
    
        else:
            print("Invalid operation")
    else:
        quit()