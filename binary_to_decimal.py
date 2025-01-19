binary =input("give the binary digits:")
position=0
decimal=0
for num in binary[::-1]:
    decimal += int(num) *(2**position)
    position+=1
print("decimal: ", decimal )