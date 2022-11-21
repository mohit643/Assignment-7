"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""

print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for divition")
user=str(input("enter the key "))
if user in ("+","-","*","/"):
    
 match user:
    case user if user=="+":
        a=int(input("Enter the first no:= "))
        b=int(input("Enter second no:= "))
        print(a+b)
    case user if user == "-":
        a=int(input("Enter the first no:= "))
        b=int(input("Enter second no:= "))
        print(a-b)
    case user if user == "*":
        a=int(input("Enter the first no:= "))
        b=int(input("Enter second no:= "))
        print(a*b)
    case user if user == "/":
        a=int(input("Enter the first no:= "))
        b=int(input("Enter second no:= "))
        print(a/b)
                   
else :
    print("enetr valid key")




