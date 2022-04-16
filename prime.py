def prime(num):
    check=True
    for i in range(2,num):
        if num%i==0:
            check=False
            break
        else:
            continue
    return(check)


prime_num=[]
lim=int(input("Enter a limit value:"))
for y in range(2,lim):
    if prime(y):
        prime_num.append(y)
print(prime_num)
