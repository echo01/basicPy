x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x > y) & (x > z):
    if y > z:
        print("x is maximum and z is minimum")
    elif y < z:
        print("x is maximum and y is minimum")
    else:
        print("x is maximum and y,z is minimum")
elif (y > x) & (y > z):
    if x > z:
        print("y is maximum and z is minimum")
    elif x < z:
        print("y is maximum and x is minimum")
    else:
        print("y is maximum and x,z is minimum")
elif (z > x) & (z > y):
    if x > y:
        print("z is maximum and y is minimum")
    elif x < y:
        print("z is maximum and x is minimum")
    else:
        print("z is maximum and x,y is minimum")
else:
    print("x=y=z")
