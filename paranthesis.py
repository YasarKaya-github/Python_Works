n="()"
k="[]"
s="{}"
result=False
par=(input("Enter your paranthesis: "))
ani=par.find(n[0])
aki=par.find(k[0])
asi=par.find(s[0]) 
if par.count("(")==par.count(")") and par.count("[")==par.count("]") and par.count("{") and par.count("}"):
    if len(par)%2==0:
        if par.find(n)>-1:
            for i in range(ani+1,len(par)+1,2):
                if par[i]==")":
                    result=True
                    break
                else:
                    result=False
        else:
            resul=False
        if par.find(k)>-1:
            for i in range(aki+1,len(par)+1,2):
                if par[i]=="]":
                    result=True
                    break
                else:
                    result=False
        if par.find(s)>-1:
            for i in range(asi+1,len(par)+1,2):
                if par[i]=="}":
                    result=True
                    break
                else:
                    result=False
        
    else:
        result=False
else:
    result=False
                            
print(result)

        
    
    