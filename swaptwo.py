'''
Tricky  program
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  reference

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x=25
y='Hyd'
x,y=y,x
print(f"x={x}",f"y={y}",sep='\n')