
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''


x=25
y=10
print(f"Before swap : x = {x}, y = {y}")
x = x+y #25+10=35
x= x-y #35-10=25
x=x-y#35-25=10
print(f"After swap : x={x},y={y}")




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  reference

Hint: One  multiplication  and  two  divisions

x = 25
y =  10


'''


x=25
y=10
print(f"Before swap: x={x},y={y}")
x=x*y      # 25 *10 = 250
y = x//y     #250//10 = 25
x= x//y      #250//25 = 10
print(f"After swap: x={x},y={y}")