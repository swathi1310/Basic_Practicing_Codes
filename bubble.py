string = (input("Enter the string:"))
i = 0
for i in range(0, len(string)):
    for j in range(0, len(string)):
        if string[i] == string[j]:
            if j > i:
                print("$", end="")
            else:
                print(string[j], end="")
        else:
            print(string[j], end="")
    print()
'''x=input("enter the string:")
#b=x.rfind(x[0])
#print(b)
a=x[1:]
y=(x[0]+a.replace(x[0],'*'))
print(y)'''
# harika program
