even=0
odd=0
i=1
while(i<=10):
    if(i%2==0):
        even+=1
    else:
        odd+=1
        i+=1
        print("count of even no=",even)
        print("count of odd no=",odd)