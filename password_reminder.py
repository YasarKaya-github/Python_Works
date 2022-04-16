name="yaşar"
password="1233321"
name_check=input("What is your name?").lower()
if name_check==name:
    print(f"Hello {name} the password is: {password}")
else:
    print(f"Hello {name_check} See you later")