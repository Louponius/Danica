 a="ffffffffffffffff ffffffffffffffff ffffffff ffffffffffffff fffffffffffffffffff"
 c=input(">")
 
 i = str.lower(c)
 
 if "f" in i:
   if i.startswith(a):
     b=str.split(i,"ffffffffffffffff ffffffffffffffff ffffffff ffffffffffffff fffffffffffffffffff ")
     for x in b:
       print(x)
