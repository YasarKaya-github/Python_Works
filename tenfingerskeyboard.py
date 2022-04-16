sol_el_kume={"q","a","z","w","s","x","e","d","c","r","f","v","t","g","b"}
sag_el_kume={"y","h","n","u","j","m","ı","k","ö","o","l","ç","p","ş","ğ","i","ü"}
kelime=input("Kelimeyi girin:")
kelime_kume=set(kelime)
sol=kelime_kume.intersection(sol_el_kume)
sag=kelime_kume.intersection(sag_el_kume)
toplam=sol_el_kume.union(sag_el_kume)
isaret=kelime_kume - toplam
print(isaret)
print(sol)
print(sag)
comf=(sag!=set())and(sol!=set())and(isaret==set())
print(comf)   