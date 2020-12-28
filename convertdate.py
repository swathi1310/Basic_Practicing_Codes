Date=input("Enter the date:")
list=["January","February","March","April","May","June","July","August","September","October","November","December"]
if Date[-5]=='/':
    M,D,Y=Date.split("/")
    print("{}/{}/{}".format(D,M,Y))
else:
    M,Date=Date.split(" ")
    D,Y=Date.split(",")
    if M in list:
        M=list.index(M)+1
        print("{}/{}/{}".format(D,M,Y))


