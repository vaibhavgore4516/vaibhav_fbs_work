p=int(input("enter the amount"))
t=int(input("enter the years"))
r=float(input("enter the rate"))
compound_intrest=p*(1+r/100)**t-p
print("compound interst",compound_intrest)
