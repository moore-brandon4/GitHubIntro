def add(x, y):
    return x + y

def subtract(x, y):
    return x-y

#def multiply

#def divide

print("Select Operation,")
print("1.Add")
print("2.Subtract")

while True:
    choice = input("Enter choice (1,2,3,4):")
    if choice in ('1','2'):
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a second number: "))

        if choice =='1':
            print(num1,"+",num2,"=", add(num1,num2))
        break
    else:
        print("Invalid Input")

