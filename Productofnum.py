lst=[1,2,3,4,5]
prod=1
for i in lst:
    prod*=i
print("Product is: ",prod)



"""Prod is initially assigned 1

step1:prod=prod*i
prod=1*1
prod=1, here 1 is stored in product

step2: prod=1*2, prod=1 and i=1 from the lst
prod=2, here 2 is stored in prod

step3: prod=2*3, as prod stored 2 and i= 3 from the lst
prod=6, here prod stores 6

step4: prod=6*4
prod=24

step5: prod=24*5
prod=120"""

