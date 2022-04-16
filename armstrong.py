new_num=0
num=input("Enter a number: ")
if num.isdigit()==True:
    print(num)
    l_num=(len(str(num)))
    for i in range(0,l_num):
        new_num=new_num+int((num[i]))**l_num
    if str(new_num)==num:
        print(f"{num} is armstrong number")
    else:
        print(f"{num} is not armstrong number")
else:
    print("You write wrong type")

  