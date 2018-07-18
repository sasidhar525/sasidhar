n=int(raw_input())
order=len(str(n))
su=0
temp=n
while temp>0:
    digit=temp % 10
    su+=digit**order
    temp//=10
if n==su:
    print("yes")
else:
    print("no")
