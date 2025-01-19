number = int(input("Enter a number: "))
if num < 0:
    print("Square root is not possible for negative numbers ")
else:
    for  num in number/2:
        z=1
        if number==z*z:
            break
        z=z+1
    
print("root:",z)
    