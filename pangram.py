n = input("enter a number ")
nu={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
for x in n:
    if x in nu:
        nu[x]+=1
print(nu)
pangram=True
for y in nu.values():
    if y==0:
        pangram=False
if pangram==True:
    print("It is a pangram :)")
else:
    print("It is not a pangram :(")