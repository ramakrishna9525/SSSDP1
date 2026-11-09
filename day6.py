SSSSDP DAY 5
# Find  outputs (Home  work)
a = print('Hyd') , 
print('Sec') ,  
print('Cyb') 
print(type(a)) #class TUPLE
print(a)  # None
print(len(a))#1


#  Find  outputs
print({10 , 20}  |  {30 , 20})#{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#10:’Hyd’,20:’Vja’,30:’Cyb’
print(range(4) | range(5))#Range won’t do concatenates
print([10 , 20]  |  [30 , 20])#ERROR


#  Relational  operators  demo  program (Home  work)
print(9 >= 5) #   True
print(9 >= 9)  #  True
print(9 >= 12)  #  False
print(6 <= 8)#True
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)# True
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#True
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#Error

Can  complex  numbers   be  compared ?   --->  Yes  with  ==  and  !=  but  not  with  > , <  , >=  and  <=


#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  'm'  >  'j'  is  True
print('Rama'  <  'Sita')  #   'R' < 'S'  is  True
print('Hyd'  ==  'Hyd')#’H ==’H’ is True
print('Rama'  <=   'Ramana') #True
print('Rama  Rao'  >=  'Rama') #True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#True


'''
Can  complex  numbers   be  compared ?   --->  Yes  with  ==  and  !=  but  not  with  > , <  , >=  and  <=
'''

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30) #   True
print(10 >= 20 < 30) #  False
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#True
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#True

#  and  operator  demo  program
print(True  and  False)  #  False
print(False  and  True)  #  False
print(False  and   False) #  False
print(True  and  True)  #  True
print(10  and  20)  #   20
print(0  and  20)  #  0
print(-25  and  0)#0
print(''  and  25)#”
print(6j  and  'Hyd')’Hyd
print(0j  and  'Sec')#0j
print('Hyd'   and  10.8)#10.8
print(10  and  20  and  30)#30



'''
and  operator
----------------
1) When  is  the  result  of  and  operator  False ?  ---> When  at  least  one  operand  is  False
    When  is  the  result  of  and  operator  True ?  ---> When  both  the  operands  are  True

2) What  is  the  result  of  op1  and  op2  when  op1  is  True ?  ---> op2
    What  is  the  result  of  op1  and  op2  when  op1  is  False ?  ---> op1

3) Is  0  True  (or)  False  ?  --->  False
     What  about  Non-zero ? ---> True

4) Is  ''  True  (or)  False  ?   --->  False  due  to  empty  string
     What  about  non-empty  string ?  ---> True

5) What  is  0j  --->  False  due  to  zero  imag
    What  is  4j  ---> True  due  to  non-zero  imag
    What  is  3 + 0j ?  ---> True  due  to  non-zero  real
'''



# or  operator  demo program
print(True  or  False)  #  True
print(False  or  True)  #  True
print(True  or  True)  #  True
print(False  or   False)  #  False
print(10  or  20)  #  10
print(0   or  20)  #  20
print(-25  or  0)# This concept is not clear even though trying to answer#-25
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#3+4j
print('Hyd'   or   10.8)#’Hyd’



# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25)#False
print(not  0)# True
print(not  'Hyd')# False
print(not  '')#True
print(not  -10)#False
print(not  not  'Hyd')#  True


'''
not  operator
----------------
1) What  does  not  operator  do ?  ---> Complement  operation

2) Is  not  a  unary  operator  ?  ---> Yes  becoz  it  has  single  operand
    What  about  and ,  or ? --->  Binary  operators  becoz  they  have  two  operands

3) What  is  the  associativity  of  unary  operators ?  ---> Right  to  Left
    What  is  the  associativity  of  binary  operators ?  ---> Left  to  Right  except  for  **
'''

# Tricky  program
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)#True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#True 


'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  --->  When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  --->	op1

3) and ,  or  operators  are  quite  opposite
'''


#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)#25
b =  a
print(b)#25
print(a  is  b) #True
x = 4
y = 5
z = x + y * 6
print(z)#34
25 = a#Error no reference at all 
a + b = x + y# Error

# Find outputs (Home work)
a = b = c = 25
print(id(a))#address of the object 25
print(id(b))#address of the object 25
print(id(c)) #address of the object 25
print(a , b , c)#25



# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)#25
print(y)#10.8
print(z)#’Hyd’


# Find outputs (Home work)
a , b , c = 3 , 4 , 5
print(a , id(a)) #3 address of the object 25
a *= b + c #17
print(a , id(a))#9 address of the object a


# Find outputs (Home work)
a = 20
print(a , id(a)) #20 address of the object 25
a %= 3 + 2 * 4 
print(a , id(a))#9 address of the object a


# Find outputs (Home work)
a = 3
print(a , id(a)) #3 , address of the object a
a **= 4  
print(a , id(a))#81 address of the object a



# Tricky  program
#  Find  outputs
a = [10 , 20 , 30]
b = [40 , 50 , 60]
print(a , id(a))# [10 , 20 , 30] address of the object a
a += b  #Error 
print(a , id(a)) = [10 , 20 , 30,40 , 50 , 60] address of the object a



#  Tricky  program
# Find  outputs
a = [10 , 20 , 30]
b = [40 , 50 , 60]
print(a , id(a))# [10 , 20 , 30]
a = a +  b   #  [10 , 20 , 30,40 , 50 , 60]
print(a , id(a))# [10 , 20 , 30,40 , 50 , 60] address of the object a 

#  Tricky  program
# Find  outputs
a = (10 , 20 , 30)
b = (40 , 50 , 60)
print(a , id(a)) #(10 , 20 , 30)
a += b  #(10 , 20 , 30,40 , 50 , 60)

print(a , id(a)) #(10 , 20 , 30,40 , 50 , 60)  address iof the object a


#  Tricky  program
# Find  outputs
a = (10 , 20 , 30)
b = (40 , 50 , 60)
print(a , id(a)) #(10 , 20 , 30)
a = a +  b #(10 , 20 , 30,40 , 50 , 60)

print(a , id(a)) #(10 , 20 , 30,40 , 50 , 60)  address of the object a


# Identity operators demo program
a = 25
b = 25
print(a  is  b)#Yes
print(a  is  not  b)#False
print(a == b)#True



# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)#False
print(a is not b)#True
print(a == b)#True


# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)#True
print(a  is  not  b)#false
print(a == b)#True
print()


x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) #False
print(x  is  not  y)#True
print(x == y)#True
print()

m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)#True
print(m  is  not  n)#False
print(m == n)#True



# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  #False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  #True
m = range(5)
n = range(5)
print(m == n)# True


# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  #False
print(a  ==  b)#True


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#True
print(19 in list)#False
print(14 not in list)#True
print(15 not in list)#False
s = 'Hyd is green city'#
print( 'is' in s)#True
print('was' in s)#False
print('g' in s)#True
print('z' in s)#False
print(' ' in s)#True
print('gre' in s)#True
print('yd i' in s)#True
print('' in s)#False
print('' not in s)#True

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = +25  = 25
print(a++)  #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1) = a + 1 = 25 + 1 = 26
print(--a)# -(-a) = +a = +25 =25
print(a--) # a-)- =a+ = 25+ error
print(a--1)# a- (-1) = a+1 = 25+1 = 26
print(-a)#-25 
print(+-a)#-25
print(-+a)#-25

#  Semicolon  demo  program
print('One');# In python semi colon not mandatory #One
print('Two');#Two
print('Three');#Error
print('Hyd')  ;   print('Sec')  ;  print('Cyb')#Error



# pow()  function  demo  program
import  math
print(math . pow(2 , 3))#8.0
print(math . pow(-2 , -3))# 0.125
print(math . pow(10 , -2))#0.01
print(math . pow(4 , math . pow(3 , 2)))#262144




'''
pow()  function
-----------------
1) What  does  pow(a , b)  do ?  ---> Returns  a ^ b

2) What  is  the  result  of  pow(5 , 2) ?  ---> 25.0  but  not  25

3) In  other  words,  pow()  function  returns  float  result

4) Where  is  pow()  function  defined ?  ---> In  math  module

5) What  are  the  two  ways  to  obtain  a ^ b ? --->  a ** b  and  pow(a , b)

6) How  to  call  function  of  a  module ?  --->  module . function(args)

7) Can  a  module  be  used  without  import ?  ---> No

8) What  is  the  pre-requisite  to  use  a  module ?  ---> It  needs  to  be  imported

9) pow(a , pow(b , c))
    What  is  a  nested  call ?  --->  A  function  call  inside  another  function  call					
    Which  call  is  executed  first ?  --->	Inner  call  is  executed  before  outer  call
    What  is  the  result  ?  ---> a ^ b ^ c	

10) math . pow(a , b , c)
      Is  it  valid ?  ---> No  becoz  pow()  function  expects  2-args  but  3-args  are  passed
'''

# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) #5.0
print(math . sqrt(10)) #3.something
print(math . sqrt(6.25))  #2.something
print(math . sqrt(True)) #1.0
print(math . sqrt(3+4j)) #Error
print(math . sqrt(math . sqrt(256)))#16.0  -4.0
print(math . sqrt(math . pow(3 , 4)))  #3 power 4 81.0
print(math . sqrt(-16))#Error
print(sqrt(49)) #Errror because of no import 


'''
sqrt()  function
-------------------
1) What  does  sqrt(x)  do ?  ---> Returns  square  root  of  'x'

2) What  is  the  result  of  sqrt(9) ?  ---> 3.0  but  not  3

3) In  other  words,  sqrt()  function  returns  float  result

4) Where  is  sqrt()  function  defined ?  --->  In  math  module

5) math . sqrt(x)
    Where  is  sqrt()  function  searched ?  ---> In  math  module

6) sqrt(x)
    Where  is   sqrt()  function  searched ? ---> In  current  module  (or)  program

7) Can  sqrt(-ve  value)  be  determined ?  --->  No  and  it  leads  to  error

8) math . sqrt(math . pow(x , y));
    Which  function  is  executed  first ? ---> Inner  function  is  executed  before  outer  function
'''



# fabs()  function  demo   program
import  math
print(math . fabs(-10)) #10.0 
print(math . fabs(-25.6)) #25.6
print(math . fabs(20)) #20.0
print(math . fabs(35.8))  #35.8
print(fabs(-25))  #25.0


'''
fabs()  function
-------------------
1) What  does  fabs(-ve  value)  do ?  --->  Returns  +ve   value
    What  does  fabs(+ve  value)  do ?  ---> Returns  same  value

2) What  is  the  result  of  fabs(integer (or) float)  ---> Always  float  irrespective  of  the  argument

3) Where  is  fabs()  function  defined ?  --->  In  math  module
'''





# floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #  11
print(math . floor(25.0)) #25
print(math . ceil(25.0))   #25
print(math . floor(-3.5))#-4 
print(math . ceil(-3.5)) #-3
print(math . floor(-9.0)) #-9
print(math . ceil(-9.0)) #-9
print(math . floor(25.1)) #25 
print(math . ceil(25.1)) #25
print(floor(3.5)) #Error no import
print(ceil(3.5)) #Error bcoz no import


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  ---> Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  ---> In  math  module
'''


# exp()  function demo program
import  math
print(math . exp(1))# e power 1-
=2.718281828459045
print(math . exp(2)) # e power 2 --          
e^2=2.71828×2.71828

print(math . exp(0)) # e power 01.0
print(math . exp(-2))#     a power -n formula      e power -2 = 1/ e power 2=1/7.389056  0.135335


'''
exp()  function
-----------------
1) What  does  exp(x)  do ?  ---> Returns  e ^  x

2) What  is  the  value  of  'e' ?  --->  2.71828
'''
