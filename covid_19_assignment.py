# BEGİN
# GET cigaratte , chronic , immune
# COMPUTE RİSK= cigaratte and cronic and immune
# print RİSK

cigaratte=input("Are you cigaratte addict yes or no? ").lower()
age=int(input("how old are you? "))
chronic=input("Do you have a severe chronic disease yes or no? ").lower()
immune=input("Is your immune system too weak yes or no? ").lower()
risk=((cigaratte=="yes") and (age>=75) and (chronic=="yes") and (immune=="yes"))
print(f"You are in risk={risk}")
