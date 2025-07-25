n=int(input("enter a number wheather it is stronge or not "))
m=n
while m>0:
   r=m%10
   fact=1
   r=r-1
sum=sum+fact
m=m//10
if sum==n:
    print("it is a stronge number")
else:
    print("it is not a stronge number")
