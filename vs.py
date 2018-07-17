x = int(input("Enter a number: "))  
  
if x > 1:  
   for i in range(2,x):  
       if (x % i) == 0:  
           print(x,"is not a prime number")  
           print(i,"times",x//i,"is",x)  
           break  
   else:  
       print(x,"is a prime number")  
         
else:  
   print(x,"is not a prime number")  
