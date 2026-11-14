m=int(input("Enter 1st input:"))
n=int(input("Enter 2nd input:"))
o=int(input("Enter 3rd input:"))
Largest=m if m>n and m>o else n if n>m and n>o else o
print("Largest input is:",Largest)