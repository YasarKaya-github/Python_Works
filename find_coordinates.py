coor=["right 123","right 17","left 50","up 90","down 20"]
x=0
y=0
for i in coor:
    if i.startswith("r"):
        x=x+int((i.split())[1])
    elif i.startswith("l"):
        x=x-int((i.split())[1])
    elif i.startswith("d"):
        y=y-int((i.split())[1])
    elif i.startswith("u"):
        y=y+int((i.split())[1])
print(x,y)