n=int(input("Enter the numbers"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("The sum is:",sum)
