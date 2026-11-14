
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? ---> 1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  ---> (temp - 32) / 1.8
# ''' 
# cv=int(input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius :"))
# if cv==1:
#     temp=float(input("Enter Farenheit Temperature"))
#     cf=1.8 * temp + 32
# print(f"celsius  to  farenheit:{cf:.2f}")
# else cv==2:
# temp=float(input("Enter Farenheit Temperature"))
# fc=(temp - 32) / 1.8
# print(f"farenheit  to  celsius:{fc:.2f}") 



cv = int(input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : "))

if cv == 1:
    temp = float(input("Enter Celsius Temperature : "))
    cf = 1.8 * temp + 32
    print(f"celsius to farenheit : {cf:.2f}")
elif cv == 2:
    temp = float(input("Enter Fahrenheit Temperature : "))
    fc = (temp - 32) / 1.8
    print(f"farenheit to celsius : {fc:.2f}")