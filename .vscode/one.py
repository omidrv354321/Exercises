x= input();
y= input();

n=int(x);
m=int(y);

if 1<=n and n<=100 and 2<=m and m <=100:
   z =int(n) / int(m);
   l =(int(n) / int(m)) / int(m);
   if int(l) == 1 :
      print(int(n)+int(z)+int(l));
   else:
      print(int(n)+int(z))