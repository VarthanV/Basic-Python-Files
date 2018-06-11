class Node:
	def Node(self,data,next):
		
		self.data=data
		self.head=null
		self.next.data=next
a=Node()
head=Node(5)
b=Node(4)
c=Node(3)
d=Node(6)
head.nex.data=b
b.next.data=c
c.next.data=d
count=0
while(head.nex.data==0):
	count=count+1
	print(count)
