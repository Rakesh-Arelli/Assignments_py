##Solve without using builtin methods:
##_____________________________________
##
##1. WAP to print middle charector of the string
'''st="Rakesharellispothugal"
a=len(st)
print(st[a//2])
#op:l
>>> 
'''
##2. WAP to print half reverse of the string
##Input: KNOWLEDGE
##Output: EGDELKNOW
'''
inp="KAKATIYA"
a=len(inp)//2
f_haf=inp[:a]
s_haf=inp[a:]
s_haf_rev=s_haf[::-1]
print(s_haf_rev+f_haf)
O/P:AYITKAKA
'''


##3. WAP to remove all the vouels from the given string
'''st="Rakesharelli"
vow="aeioiAEIOU"
for i in st:
    if i not in vow:
        print(i,end="")
o/p:Rkshrll
 '''   

##4. WAP to insert * in front of every vouels in the string.
##Input: BANANA
##Output: B*AN*AN*A
'''st="BANANA"
vow="aeioiAEIOU"
for i in st:
    if i in vow:
        print("*",i,end="")
        continue
    else:
        print(i,end="")

op/=B* AN* AN* A'''

##5. WAP to count number of words in the string.

'''st="BANANA"
for i in st:
    print(st.count(i),end="")

op/=132323'''

##6. WAP to remove extra space from the given string 
'''
st="Ojas innovative technologies"
for i in st:
    if i==" ":
        continue
    else:
        print(i,end="")

o/p:Ojasinnovativetechnologies'''

##7. WAP to insert string in between the given string
##Input: Ojas technologies 
##Output: Ojas innovative technologies
'''In="Ojas technologies"
x=In.index(" ")
print(In[:x]+" innovative"+In[x:])
op/=Ojas innovative technologies'''

##8. WAP to find the ascci value of given char
for i in input("Enter String "):
    print(i," : ",ord(i))
'''
#output
Enter String A
A  :  65
Enter String a
a  ->  97
'''
##9. insert ojas in front of every string 
'''a="innovative"
print("ojas"+" "+a)

op/=ojas innovative'''

##10. insert ojas in every extra space in the string
'''
In=input("enter a string : ")
for i in In:
    if i == " ":
        print(" ojas",i,end="")
        continue
    else:
        print(i,end="")
o/p:enter a string : kakatiya university warangal
kakatiya ojas  university ojas  warangal
'''

