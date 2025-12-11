#arithmetic operators
a=40
b=5
print("ADDITION:",a+b)
print('SUBTRACTION:',a-b)
print('MULTIPLICATION:',a*b)
print('DIVISION:',a/b)
print('FLOOR DIVISION:',a//b)
print('MODULUS:',a%b)
print('EXPONENTIATION:',a**b)
print("")

#assignment operators 
a=40
a+=5  #a=a+5
print(a)
a-=5  #a=a-5
print(a)    
a*=5  #a=a*5
print(a)
a/=5  #a=a/5
print(a)
a//=5  #a=a//5
print(a)    
a**=5  #a=a**5
print(a)
a%=5  #a=a%5
print(a)
print("")

#Comparison Operators
a=40
b=5
print("EQUAL TO:", a==b)
print('NOT EQUAL TO:', a!=b)
print("greater than:",a>b)
print("LESS THAN:",a<b)
print("GREATER THAN OR EQUAL TO:",a>=b)
print("LESS THAN OR EQUAL TO:",a<=b)
print("")

# Logical Operators
x = True
y = False
print("AND:", x and y)  # False
print("OR:", x or y)    # True
print("NOT x:", not x)   # False
print("NOT y:", not y)   # True
print("")

#example
a=5
print(" a is greater than 3 and a is less than 10:",a>3 and a<10)
print(" a is greater than 3 or a is less than 4:",a>3 or a<4)
print(" a is not equal to 5:",not(a==5))
print("")

#bitwise operators
a=4 # in binary:  0100
b=5 # in binary:  0101
print("AND:", a&b)  
print("OR:", a|b)
print("XOR:",a^b)
print("NOT", ~a)
print("LEFT SHIFT:",a<<2)
print("RIGHT SHIFT:",b>>2)
print("")

#membership operators
list1=[1,2,3,4]
print(2 in list1)      # True
print(5 in list1)      # False
print(3 not in list1)  # False
print(7 not in list1)  # True
print("")

#identity operators
x = ["apple","banana","cherry"]
y=x
z = ["apple","banana","cherry"]
print(x is y)  #true
print(x is z) #false
print(x is not y) #false
print(x is not z) # true
print(x==z) #true
print(x!=z) #false
