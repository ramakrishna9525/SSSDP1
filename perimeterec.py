
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  ---> 2 * (length + breadth)
'''



length = float(input("Enter length : "))
breadth = float(input("Enter breadth : "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area of Rectangle : {area:.2f}")
print(f"Perimeter of Rectangle : {perimeter:.2f}")