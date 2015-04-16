def triangle(a):
	for i in list(range(a+1)):
		print('T'*int(i))
	
	for i in reversed (range(a)):
		print('T'*int(i))
	

triangle(int(input("dime")))
