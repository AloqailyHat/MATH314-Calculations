# -*- coding: utf-8 -*-
"""MATH314.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vglrWa4Emauq2J2PsQlb2J36Rrz9PQyD
"""
###################################################

# function for multiplying two binary digtis 
def mult_Binary(num1, num2):
  # convert the input number to int 
  num1_int = int(num1, 2)  
  num2_int = int(num2, 2)
  # multiply the two numbers 
  num_result = num1_int * num2_int
  # convert the int result number to binary by using the bin built in function 
  result_bin = bin(num_result)[2:] # we didi the slicing because the built in function bin adds 0 by default and the slicing will remove it 
  return result_bin

######################################################

# finction for adding two binary numbers 
def add_binary(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize the result
    result = ''
    # Initialize the carry
    carry = 0
    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        # Compute the carry.
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result.zfill(max_len)

###########################################################

# function for converting a number from deciaml to binary, octal or hexadecimal.

m=[]                                #a list to hold the result
def expansion1(n,base):
    q = n
   # k = 0
    if base==16:                    #in case of hexadecimal.
     while q != 0:
        o=q % b
        if o==10:
          m.append('A')
        elif o==11:
          m.append('B')
        elif o==12:
          m.append('C')
        elif o==13:
          m.append('D')
        elif o==14:
          m.append('E')
        elif o==15:
          m.append('F')
        else:
          m.append(o)
        q = int(q / base)
    else:                       #the two other cases.
      while q != 0:
        m.append(q % base)
        q = int(q / base)
       # k += 1
    return m.reverse()          #reverse to correct the order of the result.
                                #ask user to enter
print("Please enter a number in decimal :")
n=int(input())
print("Please enter the base: ")
b=int(input())

expansion1(n,b)
print(n,'base 2 =',' '.join(str(n) for n in m),'base',b)    # print as a string 

##here to convert from binary,octal or hexadecimal to decimal .

b = int(input("Enter a binary number: "), 2)  #2 is the base.
print("binary equivalent: ", b)




############################################################

# function for ....








############################################################


#main program
print("welcome to MATH314 project!")
x = "y"
while(x == "y"):
    print("chose what operation you want to do(enter number):\n1-binary addtion\n2-binary multiplicatin")
    o = input()
    if o == "1":
        print("enter first binary number:")
        a = input()
        print("enter second binary number:")
        b = input()
        print("the result is: \n", add_binary(a, b))
    elif o == "2":
        print("enter first binary number:")
        a = input()
        print("enter second binary number:")
        b = input()
        print("the result is: \n", mult_Binary(a, b))

    print("want to do another operation? y/n")
    x = input()
    
print("thank you")
