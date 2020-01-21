fte = input("Choose what file to execute> ")

def lts(s):  
  str1 = " "   
  return (str1.join(s)) 

with open(fte) as fte2:
  for line in fte2:
    if "ffffffffffffffff ffffffffffffffff ffffffff ffffffffffffff fffffffffffffffffff" in line:
      b=str.split(line,"ffffffffffffffff ffffffffffffffff ffffffff ffffffffffffff fffffffffffffffffff ")
      x3=b[1].rstrip("\n")
      print(x3)

    if "fff fffffffffffffff fffffffffffff ffffffffffffffff f ffffffffffffffffff fffff" in line:
      b=str.split(line,"fff fffffffffffffff fffffffffffff ffffffffffffffff f ffffffffffffffffff fffff ")
      x3=lts(b)
      c=str.split(x3, " ") 
      if c[1] == c[2]:
        print("true")
      else:
        print("False")

    if "fffffffffffffffff fffff f ffff" in line:
      b=str.split(line, "fffffffffffffffff fffff f ffff ")
      x3=lts(b)
      c=str.split(x3, " ")
      c1=c[1].rstrip("\n")
      if c1 != "ffffffffffffffffff":
        f=open(c1,"r")
        print(f.read())
        f.close()

    if "fffffff ffffffffffffffffff fffff f ffffffffffffffffffff fffff ffffffffffffffffff" in line:
      b=str.split(line, "fffffff ffffffffffffffffff fffff f ffffffffffffffffffff fffff ffffffffffffffffff ")
      x3=lts(b)
      c=str.split(x3," ")
      if c[2] < c[1]:
        print("true")
      else:
        print("false")

    if "fffffffffffffffffff fffffffffffff f ffffffffffff ffffffffffff ffff ffffffffffffffffff" in line:
      b=str.split(line, "fffffffffffffffffff fffffffffffff f ffffffffffff ffffffffffff ffff ffffffffffffffffff ")
      x3=lts(b)
      c=str.split(x3, " ")
      if c[1] > c[2]:
        print("true")
      else:
        print("False")
