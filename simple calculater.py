def calculator():
    print("Welcome to simple calculator")
    
    try:
        num1=float(input("Enter your 1st number: "))
        num2=float(input("Enter your 2nd number: "))
    except ValueError:
        print("Invalid input. Enter your number again")
        return
    print("\n Choose an operation: ")
    print("\n 1. Addition '+'")
    print("\n 2. Subtraction '-'")
    print("\n 3. Multiplication '*'")
    print("\n 4. Division '/'")
    
    choice = int(input("Enter your choice (1,2,3,4): "))
    
    if choice==1:
        result= num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif choice==2:
        result= num1-num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif choice==3:
        result= num1*num2
        print(f"\nResult: {num1} x {num2} = {result}")
    elif choice==4:
        if num2==0:
            print("Cannot divide by zero")
        else:
            result= num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        ("Invalid choice. Choose from 1,2,3,4")
    

calculator()



    



        