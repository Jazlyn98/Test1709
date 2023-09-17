global_var = 10
def outer_function():
    outer_var = 20
    def inner_function():
        inner_var = 30

        print(inner_var)

    print(outer_var)
    inner_function()
print (global_var)
outer_function()

string='hom nay toi met'
str=string.split(" ")
count={}
for i in str:
    if i in count:
        count [i]+=1
    else:
        count[i]=1
for i in sorted(count, key=count.get, reverse=False):
       print(i, count[i])

name1 = ('anie', 'ashe', 'wukong', 'anivia')
name = ('riven', 'yasuo', 'katarina', name1)
print(name)

str = "python"
for i in str:
    print(i)


values=range(5)
for i in values:
    print (i)
for i in range (0,5,2): # (start,end,step)
    print (i)

for i in range(0,5):
    if i==3:
        continue
    print (i)

for i in range (0,5):
    s='*'*i
    print (s)

n=5
for i in range (1,n):
    s=n-i
    k=s* " "
    print (k, end=" ")
    print (((2*i)-1)*'*')

n=0
sum=0
while n<8:
    sum= sum+n
    n=n+1
print ('total:', sum)

i=1
n=5
while i<=n:
    print (i)
    i=i+1

n=9
while n<10:
    print('true')
    n=n+1
else:
    print ('false')

i=1
while i<=10:
    print (i)
    if i>=5:
        break
    i=i+1

for i in range (5):
    if i >=3:
     continue
    print (i)

def add_number (sum1=4,sum2=5):
    sum = sum1+sum2
    print ('sum:',sum)
add_number()

myfamily={
    "child1":{
        "name":"Jazlyn",
        "year": 1998
    },
    "child2": {
        "name": "Crish",
        "year": 2023
    },
    "child3":{
        "name": "Hugh",
        "year": "2000"
    }
}
print (myfamily["child2"]["name"])

def greet():
    print ("Say Hello")
greet()
print ("Ms Jazlyn")

import math
square_root=math.sqrt (4)
print("can bac 2 cua 4 is",square_root)
power=pow (2,3)
print ("2 ngu 3 la",power)

def outer():
    message='Hello'
    def inner():
        message='Hi'
        print (message)
    inner()
    print ('outer:',message)
outer()

import math
print ('gia tri so pi:',math.pi)

try:
   x=10
   y=0
   result=x/y
   print(result)
except:
    print("in ra toi")

values=input("Nhập vào các giá trị:")
l=values.split(",")
t=tuple(l)
print (l)
print (t)

class Myclass:
    name=" "
    age= 0
Myclass1 = Myclass()
Myclass1.name= "Jazlyn"
Myclass1.age= 25
print(f"{Myclass1.name} is {Myclass1.age} year old")

list_ex = [1, 5, 8, 2, 8, 5, 5]
print (list_ex)

set_ex = {1, 2, 2, 5, 8}
print(set_ex)
set2 = set(list_ex)
list2 = list(set2)
print(sorted(list2))


dict_ex = {"first": 1, "second": 3}
print(dict_ex["first"])
print(dict_ex.keys())
print(dict_ex.values())
print(list(dict_ex.keys()))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print (self.name + ",", self.age, "year old")

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def info(self):
        print(self.name + ",", self.age, "years old, salary:", self.salary)
jazlyn = Person("Jazlyn",25)
jazlyn.info()
jazlyn = Teacher("Jazlyn",25,"5000000")
jazlyn.info()


class Inc:
    name=" "
    age= 0
tran1=Inc()
tran1.name="Jazlyn"
tran1.age= 25
print (f"Name:{tran1.name}, Age: {tran1.age}")

class Student:
    count = 1
    def __init__ (self):
        Student.count= Student.count + 1
s1= Student()
s2= Student()
s3= Student()
print ("the number of student:", Student.count)

class room:
    length = 0.0
    breadth = 0.0
    def calculate_area(self):
        print ("Area of room:",self.length* self.breadth )
study_room= room()
study_room.length=42.5
study_room.breadth=30
study_room.calculate_area()

class Animal:
    name=""
    def eat (self):
        print ("I can eat")
class Dog (Animal):
    def eat (self):
        super().eat()
        print ("I like eat bones")
Goggy=Dog()
Goggy.eat()

class Mammal:
    def mammal_info(self):
        print ("mammals can give direct birth")
class WingedAnimal:
    def winged_animal_info(self):
        print ("winged animals can flap")
class Bat(Mammal,WingedAnimal ):
    pass
b1= Bat ()
b1.mammal_info()
b1.winged_animal_info()


class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def __gt__(self,other):
        return self.age > other.age
p1= Person ("Jazlyn", 25)
p2= Person ("Hugh",20)
print (p1==p2)
print (p1>p2)

class PowTwo:
    def __init__(self,max=0):
        self.max= max
    def __iter__(self):
        self.n= 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result= 2** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
numbers = PowTwo(3)
i = iter(numbers)
for i in PowTwo(3):
    print (i)

#closure

def calculate():
    num=1
    def inner_func():
        nonlocal num
        num+=2
        return num
    return inner_func
#call outer function
odd= calculate()
#call inner function
print (odd())
print (odd())
print (odd())
odd2= calculate()
print (odd2())

def outer(x):
    def inner(y):
        return x+y
    return inner
add = outer(5)
result= add(4)
print (result)

def greeting (name):
    def hello():
        return "Hello," + name
    return hello
greet= greeting ("Jazlyn")
print (greet())

def make_pretty(func):
    def inner():
        print ("I got it")
        func()
    return inner
@make_pretty # decorate the ordinary function
def ordinary():
    print ("I am ordinary")
ordinary()

import random
print (random.randint(0,10))

km= float(input("Enter value in kilometers: "))
conv_fac=0.621
miles= km*conv_fac
print ('{0} km is equal {1}'. format(km,miles))

import datetime #get the current date and time
now= datetime.datetime.now()
print (now)

import datetime #get the current date
current_date = datetime.date.today()
print (current_date)

from datetime import date #date object of today's date
today= date.today()
print ("current date=",today.year)
print ("current month=",today.month)

from datetime import datetime
now = datetime.now()
t= now.strftime("%m/%d/%Y,%H:%M:%S")
print (t)

import time
while True:
    localtime= time.localtime()
    result=time.strftime('"%I:%M:%S %p", localtime')
    print (result)
    time.sleep(2)
    break

import threading
import time
def print_hello():
    for i in range(4):
        time.sleep(0.5)
        print("Hello")
def print_hi():
    for i in range(4):
        time.sleep(0.7)
        print("Hi")
t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_hi)
t1.start()
t2.start()

import json
x= '{ "name":"Nathan", "age":30, "city":"New York"}'
y= json.loads(x)
print (y["name"])

print ('\a')

