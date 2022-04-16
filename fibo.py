fibo=[]
i=1
y=-1
while i<=55:
    fibo.append(i)
    i=i+fibo[y]
    y=y+1
print(fibo)