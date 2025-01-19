number = int(input("Enter a number: "))
if number < 0:
    print("Square root is not possible for negative numbers ")
else:
    z=1
    for  num in range(number):
      
        if number==z*z:
            break
        z=z+1
    
print("root:",z)
    