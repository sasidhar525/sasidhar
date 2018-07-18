a,b=map(int,input().strip().split())
 for k in range(a+1,b):
    if k>1:
     for i in range(2,k):
      if(k % i)==0: 
       break
     else:
      print(k,end=" ")
