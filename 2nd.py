num=int(input("enetr the three digit number"))

a=num%10
num=num//10
b=num%10
c=num//10
print(a,"first digit")
print(b,"second digit")
print(c,"third digit")
if(c==b*b):
 print("yes you have done")
elif(c==b/2):
  print("yes you have done")
else:
  print("please try next time")

