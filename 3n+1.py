inputt=int(input("Enter your Number here : "))
flag=1
while(inputt!=1):
    if(inputt%2==0):
        inputt=inputt/2
        flag=flag+1
    else:
        inputt=3*inputt+1
print(flag)
