# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:24:53 2021

@author: NITRO
"""
#1-amaliyot
cars=['toyota','huyundai','mazda','gm','kia']
for car in cars:
    if car=='gm':
        print(car.upper())
    else:
        print(car.title())
        
        
#2-amaliyot
for car in cars:
    if car !='gm':
        print(car.title())
    else:
        print(car.upper())
        

#3-amaliyot
login=input("Loginingizni kiriting: ")
if login.lower()=='admin':
    print("Xush kelibsiz, Admin foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")


#4-amaliyot
a=int(input('1-sonni kriting: '))
b=int(input('2-sonni kriting: '))
if a==b:
    print('Ikkala son teng ekan')
    
#5-amaliyot
c=int(input('Istalgan son kiriting: '))
if c>0:
    print(f"{c} musbat son")
else:
    print(f"{c} manfiy son")
    
#6-amaliyot
d=int(input('son kiriting: '))
if d>0:
    print(d**0.5)
else:
    print('musbat son kriting!')