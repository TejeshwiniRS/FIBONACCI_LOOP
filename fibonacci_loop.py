num=int(input("Enter the range of fibonacci series: "))
i=0
n1,n2=0,1
if(num<=0):
    print("please enter the proper range")
elif(num==1):
    print(n1)
else:
    while(i<num):
        print(n1)
        n=n1+n2
        #updation
        n1=n2
        n2=n
        i+=1
