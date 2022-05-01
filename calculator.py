# function that adds two numbers
def add(x, y):
    return x + y

# function that subtracts two numbers
def subtract(x, y):
    return x - y

# function that multiplies two numbers
def multiply(x, y):
    return x * y

# function that divides two numbers
def divide(x, y):
    return x / y

print("select an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. division")


while True:
    #imput from the user
    choice = input("Enter choice(1,2,3,4): ")
    
    #check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation == 'no':
            break
        
    else:
        print("Invalid Input")
            