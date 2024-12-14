pw={"Anjali":"jl1234","Aryan":"jlABCD","Bob":"password","User4":"JL1236"}
un=input("Enter your username")
if(un in pw):
    passw=input("Enter your password") 
    if(passw==pw[un]):
        print("You succesfully logged in")
    else:
        print("Wrong password")
else:
    print("Username not found")
