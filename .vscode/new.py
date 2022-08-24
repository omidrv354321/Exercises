x1= input();
x2= input();

a=int(x1);
b=int(x2);
z = [ ];
for i in range(0,int(b)-1) :
   z[int(i)] = input().split(" ");
p =0;
for o in range(0,int(b)-1) :
   if z[int(o)] == 0 :
      p+=1;
   else:
      p=0;
if p > int(a):
   print("YES");
else :
   print("NO")