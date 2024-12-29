w = input("enter a word ")
w=w.lower()
vw={"a":0,"e":0,"i":0,"o":0,"u":0}
for x in w:
    print(x)
    if x in vw:
       vw[x]+=1
print(vw)