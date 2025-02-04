a=[1,2,3,4,5,6,7,8,9,10]
print("list  :  ",a)

check = int(input("enter the number to check"))
new_list = [ num for num in a if num < check]
print("Numbers less than ",check," are ",new_list)