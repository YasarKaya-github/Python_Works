immune=input("is yout immune system too weak(yes/no):").lower()
cigaratte=input("Are you a cigarette addict older than 75 years old?(yes/no):").lower()
chronic=input("Do you have several chronic disease(yes/no):").lower()
if immune=="yes" or cigaratte=="yes" or chronic=="yes":
    print("You are in risky group")
else:
    print("You are not in risky group")