#SORU BİR

# word=input("Enter a word: ")
# y=len(word)
# i=0
# while i<y:
#     print(word[i])
#     i=i+2

#SORU İKİ

# num=input("Enter a number: ")
# print(num[len(num)::-1])

#SORU ÜÇ

# for i in range(1,5):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)

#SORU DÖRT

# word=set(input("Enter a word: "))
# numbers={"1","2","3","4","5","6","7","8","9","0"}
# print(f"amount of letters is {len(word-numbers)}")
# print(f"amount of number is {len(word.intersection(numbers))}") 

#SORU BEŞ

# num=int(input("Enter your number: "))
# check="Prime"
# for i in range(2,num):
#     if num%i==0:
#         check="not Prime"
#         break
#     else:
#         continue
# print(f"This number is {check}")


# def missing_char(word, n):
#     missing=word.replace(word[n],"")
#     return(missing)
# print(missing_char('kitchen', 1))

# def my_function(a,b):
#     hypotenuse = (a**2 + b**2)**0.5
#     return(hypotenuse)
# print(my_function(3,4))

# while True:

#     try:
#         no_one = int(input("The first number please : "))
#         no_two = int(input("The second number please : "))        
#         division = no_one / no_two  # normal part of the program
#     except ZeroDivisionError:
#         print("You can't divide by zero! Try again.")  # executes when division by zero
#     else:
#         print("The result of the division is : ", division)  # executes if there is no exception
#     finally:
#         print("Thanks for using our mini divison calculator! Come again!")
#         break  # exits the while loop



# fruit=["banana","mango","pear","apple","kiwi","grape"]
# while True:
#     try:
#         x=int(input("Enter a index number: "))
#         print(fruit[x])
#         break
#     except IndexError:
#         print("out of the index range")
#     except ValueError:
#         print("Please enter a integer")

# a = 9
# b = 6
# while a:
#   b, a = a, b%a
# print(b)

# with open("rumi.txt", "r", encoding="utf-8") as file :
#   print(file.read(33))
#   print(file.read(15))
#   print(file.tell())
#   file.seek(0)
#   print(file.read(33))
#   print(file.tell())
  
# with open("rumi.txt", "r",encoding="utf-8") as sea:
#   s=(sea.readlines())



# print(s)

# for x in s:
#   print(x)

# import os
# yasar=os.listdir()
# print(yasar)

# with open("fruitss.csv", "r", newline="", encoding="utf-8") as file:
#     csv_rows = csv.reader(file)
#     for row in csv_rows:
#         print(row)

# with open("fishes.txt","r",encoding="utf-8") as file:
#   for i in file:
#     print(i)


# with open("my_file.txt","w",encoding="utf-8") as file:
#   file.write("this is the first line of my text file")

# with open("my_file.txt","w",encoding="utf-8") as file:
#   file.write("this is changed")

  
# with open("my_file.txt","r",encoding="utf-8") as file:
#   print(file.read())




# fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
# x="\n".join(fruits)

# with open("fruits.txt","w",encoding="utf-8") as file:
#   file.write(x)


# with open("fruits.txt","r",encoding="utf-8") as file:
#   fruits2=file.readlines()

# print(fruits2)
  
# with open("fruits.txt","w",encoding="utf-8") as file:
#   file.writelines(fruits)

# with open("fruits.txt","r",encoding="utf-8") as file:
#   print(file.read())


# with open("istiklal.txt","r",encoding="utf-8") as file:
#   x=file.readlines()

# y=0
# with open("istiklal.txt","w",encoding="utf-8") as file:
#   for i in x:
#     y+=1
#     if y%4==0:
#       file.write(i + "\n")
#     else:
#       file.write(i)


# with open("istiklal.txt","r",encoding="utf-8") as file:
#   print(file.read())

# with open("titanic.csv","r") as file:
#   print(file.read())

# x=[1,3,6,3,2,5,1,74,2,1,3,3,3,3,]
# # print(max(x,key=x.count(*x)))
# print(max(x,key=x.count))


