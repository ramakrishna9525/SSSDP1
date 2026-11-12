# Find  outputs
How  to  import   kw  list#IMPORT KEYWORD  
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....] IMPORT KEYWORD PRINT(KEYWOD.KWLIST
How  to  print  number  of  keywords  i.e.  35#IMPORT KEYWORD PRINT(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>
print(keyword . kwlist)#import keyword print(keyword.kwlist)


#  Find  outputs  (Home  work)
How  to  import   keyword  module#import keyword
How  to  print  kwlist #import keyword print(keyword.kwlist)
How  to  print  number  of  keywords#print(len(keyword.kwlist))
How  to  print  type  of kwlist# import keyword print(type(keyword.kwlist))
print(kwlist) print(keyword.kwlist) #from keyword import kwlist


# How  to  read  float  input ?
x = float(input('Enter  float  number  :  '))
print(type(x))#class float
print(x)#output is appropriate to float





'''
Input     What  does  input()   read      What  does  float(input())  return
---------------------------------------------------------------------------------------
 10.8                ‘10.8’                                    			10.8
 25                     ‘25’   					25.0
 3+4j                ‘3+4j’   					error
 True                ‘True’  					error
-----------------------------------------------------------------------------------------
# Identify  the   issue ?
x = bool(input('Enter  Boolean  input  :  '))
print(type(x))#class bool
print(x)# error 
'''
Input           input()  reads     bool(input())  returns
--------------------------------------------------------------------------
 True                     ‘True’                                TRUE
 False                   ‘False ‘                            TRUE
 <Enter key>        ‘Error ‘                           TRUE
 25                           ‘25 ‘   TRUE
 10.8                       ‘10.8’                      TRUE
 Hyd                                 ‘Hyd’                    Hyd
 <Space  bar>                     ‘ ‘                          true
-----------------------------------------------------------------------------------
'''


# How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  '))
print(type(x))#class complex
print(x)# PRINTS WHATEVER ON X VALUE
'''
Input       input() reads      complex(input())  returns
------------------------------------------------------------------------
3+4j                                    ‘3+4j’                 3+4j
4j                                            ‘4j’                         4j
J                                                  ‘j ‘                ERROR
25                                              ‘25’                   25+0J
10.8                                       ‘10.8’                   10.8+0J 
True                                             ‘1’                    error
Ten                                              ‘10’                      error
3+j4                                              3+j4          ERROR
3+4i                                             3+4i     ERROR
4j+3                                             4j+3               ERROR
---------------------------------------------------------------------------
'''

# Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))#’hyd’
hyd = 'Sec'
print(eval('hyd'))#Sec
sec = '25'
print(eval('sec'))#sec 25
print(eval(sec))#25
cyb = 10.8
print(eval('cyb'))#cyb 10.8
print(eval(cyb))#ERROR

#  Tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")'))#Hyd returns npne

#  Find  outputs  (Home  work)
print(bool('False'))#True 
print(eval('False'))#False
print(bool(''))#false
print(eval('  ""  '))# “
print(eval(''))#( )
print(eval('  " "   '))#(  )
print(eval(' '))#ERROR



# What  is  the  advantage  of  eval(input()) ?#it takes all the values and no worry about input in the form of string and it reads in the form of steing 
x = eval(input('Enter  any  input  :  '))
print(type(x))#based on given input
print(x)#prints whatever gives the input


'''
Input                             input() reads                     eval(input())  returns
--------------------------------------------------------------------------------------
  25                                        ‘25’                                                 25
  10.8                                     ‘10.8’                                          10.8
  3+4j                                    ‘3+4j’                                             3+4J 
  False                              ‘False’                                                 False
  None                              ‘None’                                                  None
  Hyd                                  ‘Hyd’                                                        ()
  'Hyd'                                     ‘Hyd’                                                  Hyd
  [25 , 10.8 , 'Hyd']            ‘[25,10.8,’Hyd’]’                              [25,10.8,Hyd]



# What  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))# length of input string
#START FROM HERE

print(a)#whatever you enters into a
b = eval(input('Enter   any  string  : '))
print(len(b))#length of you enters input
print(b)#output  of the b


# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')  #   25,10.8,Hyd
print(a , b , c , sep = '\t')#25<tab> 10.8<tab> Hyd
print(a , b , c , sep = '---')#25---10.8---Hyd
print(a , b , c , sep = '\n')#25 <newline> 10.8<newline>Hyd[I know this is next line]
print(a , b , c)# 25 10.8  Hyd
print(a , b , c , separator = ':')  #25 :10.8 :Hyd



# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')#25 <space>10.8<space>Hyd--- 
print(a , b , c , sep = ',,,')#25,,,10.8,,,Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t')#25:::10.8:::Hyd
print(a , b , c)# 25 10.8  'Hyd'



#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#25.000000
print(type(b))# class str
x = 10.8
y = '%i'  %x
print(y)# 10
print(type(y))# class str
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)# ’[10,20,15,18]’
print(type(n))#class str


# Find outputs  (Home  work)
print('Hyd')#Hyd
print()
print('Sec')#Sec
print()
print('Cyb')#Cyb

# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s) [10 , 20 , 30 , 40,] ,(10,20,30,40),{40,30,20,10}



#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)#25
print(type(b))#clas str or int
x = 10.8
y = '%i'  %x
print(y)#10.8
print(type(y))#class str of float
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)#[‘10,20,15,18]’
print(type(n))# class str or class str list or class list



# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces><3 spaces>10.93
print('%9.1f'  %a)#<5 spaces><5 spaces>10.9
print('%10.3f'  %a)#<4 spaces><4 spaces>10.927
print('%.2f'  %a)#10.920000
print('%.6f'  %a)#10.927400
print('%f'  %a)#10.927400
print('%g'  %a)#10.9274


# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)#<4 spaces>Hyd
print('%-7s'  %a)#Hyd<4 spaces>
print('%2s'  %a)#Hyd
print('%s'  %a)# Hyd
print('%s' , a)#%s<space>Hyd
print('%s'  a)#Error
print('%s' , %a)#Error
print(a)#Hyd




# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)# ‘[10 , 20 , 30 , 40]’
print('%s' , a)#%s <space> [10 , 20 , 30 , 40]
print('%s'  a) #Error
print('%s' , %a)#Error
print('%l'  %a)#Error
print(a)# [10 , 20 , 30 , 40]




#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))#25 10.9274 Hyd
print('%i    %g    %s'    %(a , b , c))# 25 10.9274  Hyd
print('%s    %s    %s'  %(a , b , c))   25 10.9274 Hyd
print('%d    %g    %s'  , a , b , c) #%d  %g   %s , 25 10.9274 Hyd
print('%d    %g      %s'   a , b , c)# '%d    %g      %s'   a , b , c
print('%d    %g    %s'  ,  %(a , b , c))#Error
print('%d    %g    %s'    %a%b%c)#Error
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)25 10.927400 Hyd


#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)#25
print(type(y))#class str
x = 10.8
y = F'{x}'
print(y)#10.8
print(type(y))#class str
x = [10,20,30,40]
y = F'{x}'
print(y)# [10,20,30,40]
print(type(y))#class str


#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#25   10.8     Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')a = 25      b =10.8      c=Hyd
print(F'{a=}  \t   {b=}   \t  {c=}') a=25    b=10.8     c=’Hyd ‘
print(F'{a:}  \t   {b:}   \t  {c:}') 25    10.8    Hyd
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')#a={a}       b={b}       c={c}
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#a=a     b=b    c=c
print(F'{x =}  \t   {y =}   \t  {z =}')# #Error


# Find  outputs
x = 9247
print(x)#9247
print(F'{x}')#9247
print(F'{x:7}')#<3 spaces>9247
print(F'{x:07}')#0009247


# Find  Outputs  (Home  work)
x = 123.9274
print(x)#123.9274
print(F'{x:8.2f}')# <2 spaces>123.93
print(F'{x:9.1f}')# <4 spaces>123.9
print(F'{x:10.3f}')#x <3 spaces>123.927
print(F'{x:.2f}')#x: 123.93
print(F'{x:.6f}')#x:123.927400
print(F'{x}')# 123.9274

#  Find  outputs  (Home  work)
x = 25
print(F'{x}')#25
print(F'{{x}}')#{x}
print(F'{{{x}}}')#{25}
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{{{x}}}}
