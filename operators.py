##Operators: symbol(command) to perform operation on data(operands)

    ##types:
        #Arithmatic operators(+,-,*,/,%(Modulus),**(exponent),//(floor division))
        #Assignement operators(=,+=,-=,*=,%=,/=,**=,//=)
        #comaprision operators(<,>,<=,>=,==,!=)
        #logical operators(and, or,not)
        #Mmembership operators(in,not,in)
        #identity operators(is,is not)
        #Bitwise operators(&(bitwise and),|(bitwise or),^(exor),<<(left shift),>>(right shift))

#i=5
#j=6
#k=i+j
#print(k)       #11   
#print(i-j)     #-1
#print(i*j)     #30
#print(i/j)     #0.8
#print(i%j)     #5
#print(i**2)    #25
#print(i//j)    #0


#a=5000
#b=a
#print(a,b)

#a+=b
#print(a)

#a-=b
#print(a)

### Logical operators(and,or,not)

#print(True and True)
#print(True and False)
#print(False and True)
#print(False and False)


#print(True or True)
#print(True or False)
#print(False or True)
#print(False or False)


#print(not True)
#print(not False)

#user="abcd"
#password="1234"

#username=input("enter username:")
#pswd=input("enter password:")

#print(username==user and password==pswd)

#i=int(input("press 1 or 0:"))
#print(i==1 or i==0)


##Membership operators(in,not in)

#li=[1,2,3,4,5,6]

#print(8 in li)
#print(3  in li)



### Identity operators(is,is not)

   #i=5
   #j=5
   #print(id(i),id(j))
   #print(i is not j)

##bitwise operators(&,|,^,<<,>>)

i=23     #010111
j=37     #100101
         #110111
#      64   32    16    8     4      2     1
# 

    # print(i&j) #5
    # print(i|j)
    # print(i^j)
    # print(i>>2)
    # print(i<<2)

# 0 ^ 0 - 0
# 1 ^ 0 - 1
# 0 ^ 1 - 1
# 1 ^ 1 - 0


#meter=float(input("enter distance in meter:"))
#print("Distance in feet:",3.28*meter,"feet")


#n=int(input("enter a number:"))
#print("Even:",n%2==0)
