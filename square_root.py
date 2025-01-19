number = int(input("Enter a number: "))
if number < 0:
    print("Square root is not possible for negative numbers ")
else:
    z=1
    for  num in range(number):
      
        if number==z*z:
            break
        z=z+1
    z = (z + number / z) / 2
    err = abs(number - z**2)
    if err==0:
        print("the square root of",number,"is:",z)
    else:
        print("it is not a perfect square")
    