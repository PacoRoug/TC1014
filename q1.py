def triangle(number):
    for i in list (range(number+1)):
        print ('T'*i)
    for i in reversed (list (range(number))):
        print ('T'*i)

triangle(number=int(input("Dime el tamaño del triángulo  ")))
