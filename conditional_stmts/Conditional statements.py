"""
#1.Print First 10 natural numbers using while loop
'''n=10
i=1
while(i<=n):
    print(i,end=" ")
    i+=1
   ''' 
#2.Calculate the sum of all numbers from 1 to a given number
'''n=int(input("Enter a number: "))
ssum=0
for i in range(1,n+1,1):
    
    ssum=ssum+n
    print("sum of all numbers:",ssum)
'''

#3.Write a program to print multiplication table of a given number
'''n=int(input("Enter a num: "))
i=1
for i in range(1,11):
    print(n*i,end=" ")
'''
#4.Display numbers from a list using loop

'''a=["rakesh","nagarjuna","shubham", "apple"]
for x in a:
    print(x)
'''
#5.Count the total number of digits in a number
''';n=int(input("Enter any number: "))
count=0
while n!=0:
    n//=10
    count+=1
print("total no.of digits",str(count))
'''#6.Print list in reverse order using a loop
'''
lst=[12,23,34,45,6,78,]
lst1=[]
i=len(lst)-1
while i>-1:
    lst1.append(lst[i])
    i=i-1
print(lst1)
#output:[78, 6, 45, 34, 23, 12]'''

#7.numbers from -10 to -1 using for loop Display
'''for i  in range(-10,0,1):
    print(i)'''
#8.Use else block to display a message “Done” after successful execution of for loop
'''n=11
for i in range(n):
    print(i)
else:
    print(":Done")
'''
#9.Write a program to display all prime numbers within a range
'''lower=1
upper=20
for n in range(lower,upper+1):
    
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            
             print(n)
#output:
2
3
5
7
11
13
17
19
'''
#10.Display Fibonacci series up to 10 terms 
'''n=10
n1,n2=0,1
if n<=0:
    print("enter positive integer")
elif(n==1):
    print(n,end=" ")
print(n1,n2,end=" ")
for i in range(2,n):
        n3=n1+n2
        print(n3,end=' ')
        n1=n2
        n2=n3'''

    
#Find the factorial of a given number
'''n=int(input("Entera number:"))
factorial=1
if(n>=1):
        for i in range(1,n+1):
            factorial=factorial*i
        print("factorial of given number",factorial)
#output:
        Entera number:4
factorial of given number 24        
'''
# Reverse a given integer number
'''num=int(input("Enter a number: "))

while num>0:
    
    print(num%10,end="")
    num=num//10
   
'''

# Find the sum of the series upto n terms
'''n=int(input("Enter number :"))

print("series_nterms:",n*(n+1)/2)
'''
#14.Calculate the cube of all numbers from 1 to a given number 
'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(ni**3,end=" ")'''
#15.Use a loop to display elements from a given list present at odd index positions
'''lst=[1,2,3,4,5,6,7]
i=1
while i<=len(lst)-1:
    if i%2==0:
        print(lst[i],end=" ")
    i=i+1
#output:3 5 7'''
#16.Name the keyword which helps in writing code involves condition.
'''elif
#17.Write the syntax of simple if statement.
if(condition):
    block of code


# 18.Is there any limit of statement that can appear under an if block.
no
#19.Write a program to check whether a person is eligible for voting or not. (accept age from user)
age=int(input("enter your age:"))

if(age>17):
    print(age,"Your eligible for voting")
else:
    print(age,"your not eligible")
#20.Write a program to check whether a number entered by user is even or odd.
n=int(input("Enter a number:"))
while n>0:
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
        '''
#21.a program Write to check whether a number is divisible by 7 or not.
'''n=int(input("Enter a number:"))
while n>0:
    if n%7==0:
        print(n," number is divisible by 7")
    else:
        print(n," number is not divisible by 7")
#22.Write a program to display "Hello" if a number entered by user is a multiple of five ,otherwise print "Bye".
n=int(input("Enter a number"))        
while n>0:
    if n%5==0:
        print("Hello")
    else:
        print("Bye")'''
#23.Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
'''
            Unit                                                     Price   

First 100 units                                               no charge 

Next 100 units                                              Rs 5 per unit 

After 200 units                                             Rs 10 per unit 

units=int(input("Enter units: "))
if units<101:
    print("No charge")
elif units>100 and units<200:
    print((units-100)*5,"Rupees ")
else:
    print(500+(units-200)*10)
'''
#24.Write a program to display the last digit of a number. 

#(hint : any number % 10 will return the last digit)

'''n=int(input("Enter a number:"))
digit=n%10
print(digit)
'''
#25.Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
'''n=int(input("Enter a number: "))
digit=n%10
if digit%3==0:
    print("is divisible by 3")
else:
    print("not is divisible by 3")
#26.Write a program to accept percentage from the user and display the grade according to the following criteria: 

 

        Marks                                    Grade 

         > 90                                         A 

         > 80 and <= 90                       B 

        >= 60 and <= 80                       C 

         below 60                                  D 

''' 
'''n=int(input("enter a percentage: ")
if(n<90): 
    print(" A Grade",n)
elif(80<n and n>=90):
    print("B Grade",n)
elif(60<n and n>=80):
    print("C Grade",n)
else:
    print("D Grade",n)
'''
#27.Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
'''
     

        Cost price (in Rs)                                       Tax 

        > 100000                                                  15 % 

        > 50000 and <= 100000                          10% 

        <= 50000                                                  5%


n=int(input("Enyter ur price: "))
if n>100000:
    print((n*15)/100,"Rupees tax")
elif(n>50000 and n<= 100000):
    print((n*10)/100,"Rupees tax")
else:
    print((n*5)/100,"Rupees tax")
'''
#28.Write a program to check whether an years is leap year  or not
'''year=int(input("Enter a year: "))
if(year%400==0)and(year%4==0):
    print("is a leap year",(year))
elif(year%4==0)and(year%100!=0):
    print("is a leap yrear",(year ))
else:
    print("is not a lreap lear",(year))

 # output  Enter a year: 100
is not a lreap lear 100
Enter a year: 1900
is not a lreap lear 1900
Enter a year: 2000
2000  is a leap year'''

#29.Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

'''n=int(input("Enter a number: "))
if n==1:
    print("Sunday")
elif(n==2):print("monday")
elif(n==3):print("tuesday")
elif(n==4):print("wednesday")
elif(n==5):print("Thursday")
elif(n==6):print("Friday")
elif(n==7):print("Saturday")
else:print("NA")
#output: Enter a number: 3
tuesday
'''

#30.Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on 

'''
n=int(input("Enter a number from 1 to 12: "))
if n==1:print("January")
elif n==2:print("Febreury")
elif n==3:print("March")
elif n==4:print("April")
elif n==5:print("May")
elif n==6:print("june")
elif n==7:print("july")
elif n==8:print("August")
elif n==9:print("September")
elif n==10:print("October")
elif n==11:print("November")
elif n==12:print("December")
else:print(n)
====== RESTART: C:\Users\ra22222\AppData\Local\Programs\Python\Python39\26july task.py ======
Enter a number: 3
tuesday
'''
#31.What do you mean by statement
'''A statement is an instruction that a Python interpreter can execute.
So, in simple words, we can say anything written in Python is a statement.

#32.Write the logical expression for the followi
       City                                 Monument 

                  Delhi                               Red Fort 

                  Agra                                Taj Mahal 

                  Jaipur                              Jal Mahal

ct=str(input("Enter a city: "))
if (ct=="delhi"):
    print("Red Fort")
elif(ct=="Agra"):print("Taj Mahal ")
elif(ct=="Jaipur"):print("Jal Mahal")
#output:Enter a city: delhi
Red Fort

'''  
#33.Write the output of the following if a = 9 
a=9
if(a>5 and a<=10):
    print("Hello")
else:
    print("Bye")
#output:Hello

#35.Write a program to check whether a number entered is three digit number or not.'''
'''
n=int(input("Enter a number:  "))
if n>=100 and n<1000:
    print(n,"is three digit number")
else:
    print(n,"is not three digit number")
#output:Enter a number:  125
125 is three digit number
#36.Write a program to check whether a person is eligible for voting or not.(voting age >=18)
age=int(input("Enter your age: "))
if age>=18:
    print(" person is eligible for voting")
else:print(" person is not eligible for voting")'''
#output:
'''Enter your age: 18
 person is eligible for voting
#37.Write a program to check whether a person is senior citizen or not.
age=int(input("Enter your age: "))
if age>=60:
    print(" person is senior citizen")
else:print(" person is not senior citizen")
#output:
Enter your age: 59
 person is not senior citizen
 '''
#38.Write a program to find the lowest number out of two numbers excepted from user.
'''a=23
b=34
if a<b:
    print(a)

else:print(b)'''

#output:23
#39.Write a program to find the largest number out of two numbers excepted from user
'''a=23
b=34
if a>b:
    print(a)

else:print(b)'''

#output:34
#40.Write a program to check whether a number (accepted from user) is positive or negative.
'''n=int(input("Enter a number: "))
if n>0:
    print(n,"is positive ")
elif(n<0):print(n,"is negative")
else:
    print("is 0")
Enter a number: 2
2 is positive
'''
#41.Write a program to check whether a number is even or odd. 
'''n=int(input("Enter a number: "))

if n%2==0:
    print("even")
elif(n%2!=0):
    print("odd")
else:
    print("zero")


#output:
Enter a number: 4252 even'''
#42.Write a program to whether a number (accepted from user) is divisible by 2 and 3 both. 
'''
n=int(input("number: "))
if n%2==0 and n%3==0:print(n,"is divisible by 2 and 3 both")
else:print(n,"is not divisible by 2 and 3 both")
# output: number: 24
24 is divisible by 2 and 3 both'''

#43.Write a program to find the largest number out of three numbers excepted from user
'''a=(int(input("number: ")))
b=(int(input("number: ")))
c=(int(input("number: ")))

if a>b and a>c:
   print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
'''
#44.Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC.
'''temp=int(input("Enter temp: "))
if temp>=100:
    print("is boiling")
else:print("is not boiling")
#output:
Enter temp: 100
is boiling'''
#45.the age of 4 people and display the youngest one and oldest one? Accept
'''a=24
b=26
c=30
d=32
if a>b and a>c and a>c:
   print(a)
elif b>a and b>c and b>d:
    print(b)
elif c>a and c>b and c>d:
    print(c)
elif d>a and d>b and d>c:
    print(d)
if a<b and a<c and a<c:
   print(a)
elif b<a and b<c and b<d:
    print(b)
elif c<a and c<b and c<d:
    print(c)
else:
    print(d)

#output:
    32
24
'''

#46.Accept the following from the user and calculate the percentage of class attended: 

 
'''
n1=     Total number of working days 

 

n2=     Total number of days for absent 
n=30
n1=20
n2=10
print((n1*100)/n)
#output: 66.66666666666667
#47.Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle. 

 

Note : 

 

An equilateral triangle is a triangle in which all three sides are equal. 

 

A scalene triangle is a triangle that has three unequal sides. 

 

An isosceles triangle is a triangle with (at least) two equal sides.'''
'''side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1==side2 and side1==side3:
    print("Eqvilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("Issoceless triangle")
else:
    print("Scallen triangle")
10
10
10
Eqvilateral triangle'''
