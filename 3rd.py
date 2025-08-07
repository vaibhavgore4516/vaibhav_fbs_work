n=int(input("enter the emp no"))

total_sallary=0
for i in range(1,n+1):
    basic_salary=int(input("enter the basic salary"))
    if(basic_salary<2000):
        da=basic_salary*0.10
        ta=basic_salary*0.12
        hra=basic_salary*0.15
    else:
        da=basic_salary*0.15
        ta=basic_salary*0.18
        hra=basic_salary*0.20
    total_sallary=basic_salary+da+ta+hra
    print(total_sallary)
    

