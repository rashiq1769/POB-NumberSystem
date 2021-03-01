def decimalToBinary(n):
	return format(n,'08b')
#return binary value of pixel
def nCr(n,r):

	return (fact(n) / (fact(r) *fact(n-r)))
	
#Return factorial of n
def fact(n):
	res=1
	for i in range(2,n+1):
		res= res*i
	return res
	
if_name_=='_main_':
	
	print("Enter Pixel Value")
	pixel=int(input())
	n=bin(pixel).replace("0b","")
	nl=list(map(int, str(n)))
	length=len(nl)
	num=(decimalToBinary(pixel))
	print("Binary Value is:"+num)
	res=list(map(int,str(num)))
	count=0
	p=[0,0,0,0,0,0,0,0]
	q=[0,0,0,0,0,0,0,0]
	for i in range(0,8):
		j=7-id
		if res[j]==0:
			p[j]=1
		else:
			count=count+1
			if count%2==0:
				p[j]=1
			else:
				p[j]=0
	k=8-length
	for i in range (0,k):
		p[i]=0
	print("P1 is"+str(p))
	p1=p1
	count1=0
	count2=0
	for i in range(0,8):
		if(p[i]==res[i]):
			q[i]=0
		else:
			q[i]=1
	print("P2 is "+str(q))
	p2=q
	#insertion of bit to make 9 bit number
	list.reverse(p1)
	for i in range(0,8):
		if p1[i]==1:
			count1=count1+1
	p1.insert(count1-1,1)
	list.reverse(p1)
	print("P1 value after inserting a bit\n"+str(p1))
	list.reverse(p2)
	for i in range(0,8):
		if p2[i]==1:
			count2=count2+1
	p2.insert(count2-1,1)
	list.reverse(p2)
	print("P2 value after inserting a bit\n"+str(p2))
	list.reverse(p1)
	sum=0
	count=0
	for i in range(0,9):
		if p1[i]==1:
			n=i
			count=count+1
			r=count
			if n>=r:
				sum=sum+int(nCr(n,r))
	print("Share2 value is "+str(sum))
	list.reverse(p2)
	sum=0
	count=0
	for i in range(0,9):
		if p2[i]==1:
			n=1
			count=count+1
			r=count
			if n>=r:
				sum=sum+int(nCr(n,r))
	print("Share2 value is "+str(sum))
	
share2=sum
print("Share value is"+str(sum))
print("\n     Reconstruting image           \n")
print("Applying POB on share1:"+str(share1))
list.reverse(p1)
list.reverse(p2)
print(p1)
prinr("Applying POB on share2:"+str(share2))
print(p2)
del p1[count1]
del p2[count2]
print(p1)
print(p2)
b=[0,0,0,0,0,0,0,0]
for i in range(0,8):
		if(a1[i]==a2[i]):
			b[i]=0
		else:
			b[i]=1
			
print("Binary value is"+str(b))
print("The pixel value is:"+str(pixel))
		
	
		
			
	