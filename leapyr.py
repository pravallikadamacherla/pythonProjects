p=int(input())
if(p%400==0):
    print ("yes")
elif(p%4==0):
    print ("yes")
elif(p%100!=0):
    print ("yes")
else:
   	print("no")
