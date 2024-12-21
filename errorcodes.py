errorcodes={}
errorcodes["404"]="not found"
errorcodes["403"]="forbidden"
errorcodes["418"]="i'm a teapot"
errorcodes["502"]="bad gateaway"

i = input("which errorcode do you want: 404,403, 418, 502 ")

if i in errorcodes:
    print(errorcodes[i])