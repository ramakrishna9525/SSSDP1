'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
# p=int(input("Enter Principal:"))
# t=int(input("Enter time:"))
# r=float(input("Enter rate of interest"))
# print('rate of interest :',p * t * r/100)
# print("Compound Interest",p * (1  +  r  /  100) ** t  -  p)

p = int(input("Enter  principle  :  "))
t = int(input("Enter  time  : "))
r = float(input("Enter  rate  of  interest :  "))
print(f"Simple  Interest : {p * t * r / 100:.2f}")
print(f"Compound  Interest : {p * (1 + r / 100) ** t - p:.2f}")
