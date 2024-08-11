
list1=[5,6,7,8,10]
for n in list1:
    print(f"n= {n}")

n=0
in_cmd = True
while in_cmd:
    print(f"n= {n}")
    n = n+1
    input_key = input("Do you want to stop? (y/n) :")
    if input_key == 'y':
        in_cmd=False


print("End of program")
