n=int(input("Enter a num between 2 and 10^8: "))
a=0
while n!=1:
	print(n,end=" ")
	if n%2==0:
		n//=2
		a+=1
	else:
		n=(3*n)+1
		a+=1
print(1)
print("No. of steps taken to reach 1: ",a)
