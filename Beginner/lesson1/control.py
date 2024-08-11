x = 5
y=10
z=6

if(x>y) and (y>z):
    print("x>z")
elif (y>x) and (y>z):
    print(f"y is maximum value")
elif (z>x) and (z<y):
    print("z is between x and y")
else:
    print("ไม่ประมวลผล")
