SSSSPD DAY 5

#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') , 
		print('Cyb')   
     }  
print(type(a)) #set 
print(a)  #None 
print(len(a))#1


#  Anonymous  object  demo  program
_ = 25 
print(_) # 25
print(type(_)) #class int
print(id(_)) # address of the object
a , _ , c = 10 , 20 , 30  
print(a) #10
print(_) #unanonymus
print(c) #30
for  _  in  range(5):
	print(_ , 'Hello')# 0 Hello
1 Hello
2 Hello
3 Hello
4 Hello 


#  Find  outputs
a = 25
print(a , id(a))#25, address of the object 25
a = 35
print(a , id(a))  ))#35, address of the object 35 and previous objects get deleted



# Find  outputs (Home  work)
a = 25.7
print(a , id(a))# 25.7 address f the object 25.7
a = 35.6
print(a , id(a))#35.6 address of the object 35.6 and previous object is deleted
b = True
print(b , id(b))#True or 1 address of object True
b = False
print(b , id(b))# False address of the object  and deleted previous b
c = None
print(c , id(c))#None Address of the object None
c = None
print(c , id(c))# None address of the object c and deleted previous 



# Find  outputs  (Home  work)
a = 'Hyd' 
print(a , id(a)) #Hyd address of the object Hyd
a[1] = 'e'
a = 'Sec'  
print(a , id(a))  #Error
b = (10 , 20 , 15 , 18) 
print(b , id(b))# (10 , 20 , 15 , 18) address of the object b
b[2] = 19 
b = (30 , 40 , 35 , 32) 
print(b , id(b))  Error
c = range(5)  #
print(id(c))  #address of the object c
c[3] = 10 
c = range(5) 
print(id(c))#address of the object c


# Find  outputs  (Home  work)
a = 25 
b = 25  
print(a  is  b) #Yes
c = 'Hyd'  
d = 'Hyd'  #Yes
print(c  is  d)  
e = False   
f = False   #Yes
print(e  is  f) 
g = range(10) 
h = range(10) 
print(g  is  h)#no


# Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)# No different there is different address of a and b
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)#No
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)#yes
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)#No

# Find outputs (Home work)
print(10 + 20) #30
print(10.8 + 20.6) #31.4
print(3 + 4j + 5 + 6j) #8+10j
print(True + False) #1
print('Hyder' + 'abad')#Hyderabad 
print('Sankar' + 'Dayal' + 'Sarma')  #SankarDayalSarma
print('10' + '20') #1020
print([10 , 20 , 30] + [1 , 2 , 3])#[10,20,30,1,2,3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) #(25 , 10.8 , 'Hyd', 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) #error
print({10 : 'Hyd'} + {20 : 'Sec'}) #error
print(range(4) + range(5)) #error
print(10 + '20') #error
print([10 , 20 , 30] + 5) #error 
print([10 , 20 , 30] + (40 , 50 , 60))#error


# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#-9+38j
print(3 + 4j * 5 + 6j)#3+26j
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)#HydHydHydHyd
print([10 , 20 , 15] * 2)# 10 , 20 , 15,10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3)# ((25, 10.8, 'Hyd', True.25, 10.8, 'Hyd', True,25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)#Error
print({10 , 20 , 15} * 2)#Error
print({10 : 20 , 30 : 40} * 2)#Error
print([10] * [20])#Error


# Find outputs (Home work)
print(25 * 3)#75
print(10.8 * 25.6)#276.48
print(True * False)#0
print((3 + 4j) * (5 + 6j))#-9+38j
print(3 + 4j * 5 + 6j)#3+26j
print('25' * 3)#252525
print(3 * '25')#252525
print('Hyd' * 4)# HydHydHyd
print([10 , 20 , 15] * 2)#[10,20,15,10,20,15]
print((25, 10.8, 'Hyd', True) * 3)# ((25, 10.8, Hyd, True,25, 10.8, Hyd, True,25, 10.8, Hyd, True)
print([10 , 20 , 15] * 3.0)#error
print({10 , 20 , 15} * 2)#Error
print({10 : 20 , 30 : 40} * 2)#Error
print([10] * [20])#error


#  /  operator  demo  program
print(9.0 / 2)  #  4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.5
print(10 / 3)#3.0
print(10 / 2)#5.0


'''
What  does  /  operator  do  ?  ---> Peforms  division   and  returns  float  quotient
'''

# //  operator  demo  program
print(9 // 2)  #   prev(4.5) = 4
print(9.0 // 2)  #  prev(4.5) = 4.0
print(9 // 2.0)  #  prev(4.5) = 4.0
print(9.0 // 2.0)#4.0
print(10.5 // 2)#5.0
print(10 // 3)#3
print(10.0 // 3)#3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)-#-5
print(-(18 // 4))#-4


'''
//  operator
--------------
1) What  is  the  result  of  integer // integer ?  ---> Integer  quotient
    What  is  the  result  of  integer // float ?  --->  Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  ---> 	Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

2) What  is  the  result  of  integer / integer ?  ---> Float  quotient
    What  is  the  result  of  integer / float ?  ---> Float  quotient
    What  is  the  result  of  float / integer ?  ---> Float  quotient
    What  is  the  result  of  float / float ?  ---> Float  quotient

3) What  does  /  operator  do ?  ---> Performs  division  and  returns  float  quotient
     What  does  //  operator do ?  ---> Same  as  /  operator  except  that  it  returns  previous-integer(/  operator)

4) When  is  the  result  of  //  operator  integer ?  ---> When  both  the  operands  are  integers
    When  is  the  result  of   //  operator  float  with  .0 ?  ---> When  at  least  one  operand  is  float
'''

# Find outputs
print(7 / 0)# error
print(7 // 0)#error
print(7 % 0)#error


# ** operator demo program
print(3 ** 4)# 3 POWER 4   81
print(10 ** -2)# 1/100 => 0.01
print(4 ** 3 ** 2)# first 3 power 2 that is 9 then 4 power 9 =>262144
print(3 + 4 * 5 - 32 / 2 ** 3) #         3+4*5-32/8 => 3+20-32/8=>23-4.0=>19.0



'''
**  operator
---------------
1) What  is  **  operator  called ?  ---> Power  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a ** b  ** c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  ---> Left  to  right




